import requests
import os
import evaluators
import concurrent.futures
from tqdm import tqdm
import time
import json
import argparse
import scorers
import tasks
import predictors
import optimizers
import torch.multiprocessing as mp
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def get_task_class(task_name):
    if task_name == 'multi':
        return tasks.MultiTask
    else:
        raise Exception(f'Unsupported task: {task_name}')


def get_evaluator(evaluator):
    if evaluator == 'bf':
        return evaluators.BruteForceEvaluator
    elif evaluator in {'ucb', 'ucb-e'}:
        return evaluators.UCBBanditEvaluator
    elif evaluator in {'sr', 's-sr'}:
        return evaluators.SuccessiveRejectsEvaluator
    elif evaluator == 'sh':
        return evaluators.SuccessiveHalvingEvaluator
    else:
        raise Exception(f'Unsupported evaluator: {evaluator}')



def get_scorer(scorer):
    if scorer == '01':
        return scorers.Cached01Scorer
    elif scorer == 'll':
        return scorers.CachedLogLikelihoodScorer
    else:
        raise Exception(f'Unsupported scorer: {scorer}')


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', default='multi')
    ############# 把路径改成train，test存的路径 ###################
    parser.add_argument('--data_dir', default='/scratch/wd2148/prompt_optimization/data')
    ##############
    
    parser.add_argument('--question_num', default='7,17,2') #第一个是从第几个问题开始，第二个是到第几个问题，第三个是class的个数 第一个问题到底6个问题 4是类别 不包括中立 不能有空格
    ########### 把路径改成自己的prompt路径（prompt md文件名严格遵守field1_class （多少个类别，不包括neutral)_Qn-Qm (从第n个问题到第m个问题)） ##############################
    parser.add_argument('--prompts', default='/scratch/wd2148/prompt_optimization/prompts/field1_class2_Q7-Q17.md')#注意更改prompt
    ###############
    
    ############### 改成每个lable连续排列，严格遵守格式 'xxxx,xxxxx,xxx,最后一个加上neutral', 且要严格遵循给定prompt md里的label顺序 ###################
    parser.add_argument('--categories', default= "Mentioned,Not Mentioned,Neutral") #注意没有空格 手动加入Neutral
    ##############
    
    # parser.add_argument('--config', default='default.json')
    ############# 可以随意设置想要生成output的文件名 ##################
    parser.add_argument('--out', default='/scratch/wd2148/prompt_optimization/result/Q7-Q17_14out_score2.txt') #存output
    ###############
    
    parser.add_argument('--max_threads', default=32, type=int)
    parser.add_argument('--temperature', default=0.1, type=float)

    parser.add_argument('--optimizer', default='nl-gradient')
    parser.add_argument('--rounds', default=4, type=int)
    parser.add_argument('--beam_size', default=4, type=int)
    parser.add_argument('--n_test_exs', default=400, type=int)

    parser.add_argument('--minibatch_size', default=1, type=int)
    parser.add_argument('--n_gradients', default=4, type=int)
    parser.add_argument('--errors_per_gradient', default=20, type=int)
    parser.add_argument('--gradients_per_error', default=1, type=int)
    parser.add_argument('--steps_per_gradient', default=1, type=int)
    parser.add_argument('--mc_samples_per_step', default=2, type=int)
    parser.add_argument('--max_expansion_factor', default=8, type=int)

    parser.add_argument('--engine', default="chatgpt", type=str)

    parser.add_argument('--evaluator', default="bf", type=str)
    parser.add_argument('--scorer', default="ll", type=str)
    parser.add_argument('--eval_rounds', default=8, type=int)
    parser.add_argument('--eval_prompts_per_round', default=8, type=int)
    # calculated by s-sr and sr
    parser.add_argument('--samples_per_eval', default=32, type=int)
    parser.add_argument('--c', default=1.0, type=float, help='exploration param for UCB. higher = more exploration')
    parser.add_argument('--knn_k', default=2, type=int)
    parser.add_argument('--knn_t', default=0.993, type=float)
    parser.add_argument('--reject_on_errors', action='store_true') 
    # distance matrix
    #parser.add_argument('--label_score', default=[[0,1.15203679,6.55604839,6.39737463,3.05714488,6.52050209,4.06814671],[1.15203679,0,5.40446234,5.24589634,1.90531814,5.36942339,2.91624689],[6.55604839,5.40446234,0,0.15971078,3.49920917,0.08388866,2.4958086],[6.39737463,5.24589634,0.15971078,0,3.340734,0.13565817,2.33871031,],[3.05714488,1.90531814,3.49920917,3.340734,0,3.4647429,1.01585019],[6.52050209,5.36942339,0.08388866,0.13565817,3.4647429,0,2.46586895],[4.06814671,2.91624689,2.4958086,2.33871031,1.01585019,2.46586895,0]], type=list)
    # score
    
    ################### label score改成对应task的score，格式为一个list ########################
    parser.add_argument('--label_score', default=[2.17518908,0.71264771,0.62908727], type=list)
    ####################
    
    args = parser.parse_args()

    return args

#数据格式
#llama


if __name__ == '__main__':
    mp.set_start_method('spawn', force=True)
    args = get_args()

    config = vars(args)

    config['eval_budget'] = config['samples_per_eval'] * config['eval_rounds'] * config['eval_prompts_per_round']
    categories = args.categories.split(',')
    question_num = args.question_num.split(',')
    task = get_task_class(args.task)(categories, question_num, args.data_dir, args.max_threads)#可能需要function，demo暂时保持
    scorer = get_scorer(args.scorer)()#使用ll为了多种score，01只有两种
    #也可以作为数据优化的方法
    evaluator = get_evaluator(args.evaluator)(config)#使用多种evaluator选择
    bf_eval = get_evaluator('bf')(config)
    #gpt4 = predictors.BinaryPredictor(config)#使用gpt4进行二分类推理，需要大改
    llama = predictors.MultiPredictor(config, categories) #不用加新的score
    label_score = args.label_score
    optimizer = optimizers.ProTeGi(#使用gpt4，需要大改
        config, evaluator, scorer, args.max_threads, bf_eval)

    train_exs = task.get_train_examples()
    test_exs = task.get_test_examples() 

    if os.path.exists(args.out):
        os.remove(args.out)

    # print(config)

    with open(args.out, 'a') as outf:
        outf.write(json.dumps(config) + '\n')

    candidates = [open(fp.strip()).read() for fp in args.prompts.split(',')]
    candidate_res = []
    score_avg = []
    for round in tqdm(range(config['rounds'] + 1)):
        print("STARTING ROUND ", round)
        start = time.time()

        # expand candidates
        if round > 0:
            #candidates = optimizer.expand_candidates(candidates, task, gpt4, train_exs)
            candidates = optimizer.expand_candidates(candidates, task, llama, train_exs, label_score)
        # score candidates
        #scores = optimizer.score_candidates(candidates, task, gpt4, train_exs)
        scores = optimizer.score_candidates(candidates, task, llama, train_exs, label_score)
        scores_test = optimizer.score_candidates(candidates, task, llama, test_exs, label_score)
        [scores, candidates] = list(zip(*sorted(list(zip(scores, candidates)), reverse=True)))
        [scores_test, candidates] = list(zip(*sorted(list(zip(scores_test, candidates)), reverse=True)))
        # select candidates
        candidates = candidates[:config['beam_size']]
        scores = scores[:config['beam_size']]
        scores_test = scores_test[:config['beam_size']]

        # record candidates, estimated scores, and true scores
        with open(args.out, 'a') as outf:
            outf.write(f"======== ROUND {round}\n")
            outf.write(f'{time.time() - start}\n')
            outf.write(f'{candidates}\n')
            outf.write(f'{scores}\n')
            outf.write(f'{scores_test}\n')
        metrics = []
        # for candidate, score in zip(candidates, scores):
        #     #f1, texts, labels, preds = task.evaluate(gpt4, candidate, test_exs, n=args.n_test_exs)
        #     f1, texts, labels, preds = task.evaluate(llama, candidate, test_exs, n=args.n_test_exs)
        #     metrics.append(f1)
        # with open(args.out, 'a') as outf:  
        #     outf.write(f'{metrics}\n')
            
    #     if round != 0:
    #         score_avg.append(np.mean(scores))
    #         for idx in range(len(scores)):
    #             if scores[idx] == np.max(scores):
    #                 candidate_res.append(candidates[idx])

    # score_max = np.max(score_avg)
    # for idx in range(len(candidate_res)):
    #     if score_max == score_avg[idx]:
    #         res = candidate_res[idx]
            
    # with open(args.out, 'a') as outf:
    #     outf.write(f'{res}\n')
    print("DONE!")
