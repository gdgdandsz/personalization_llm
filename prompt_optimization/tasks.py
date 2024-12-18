import requests
import json
import concurrent.futures
from abc import ABC, abstractmethod
from typing import List, Dict, Callable
from tqdm import tqdm
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, classification_report
import numpy as np
class DataProcessor(ABC):
    def __init__(self, categories, question_num, data_dir, max_threads=1):
        self.question_num = question_num
        self.data_dir = data_dir
        self.max_threads = max_threads
        self.categories = categories

    @abstractmethod
    def get_train_examples(self):
        pass

    @abstractmethod
    def get_test_examples(self):
        pass

    @abstractmethod
    def evaluate(self, predictor, test_exs, label_score):
        pass

    @abstractmethod
    def stringify_prediction(self, pred):
        pass

def process_example(ex, predictor, prompt):
    pred = predictor.inference(ex, prompt)
    return ex, pred


class ClassificationTask(DataProcessor):
    def __init__(self, categories, question_num, data_dir, max_threads=1):
        super().__init__(categories, question_num, data_dir, max_threads)
        self.question_num = question_num
        self.data_dir
        self.max_threads = max_threads
        self.categories = categories
    def run_evaluate(self, predictor, prompt, test_exs, label_score, n=100):
        labels = []
        preds = []
        texts = []
    
        with concurrent.futures.ProcessPoolExecutor(max_workers=self.max_threads) as executor:
            futures = [executor.submit(process_example, ex, predictor, prompt) for ex in test_exs[:n]]
            for i, future in tqdm(enumerate(concurrent.futures.as_completed(futures)), total=len(futures), desc='running evaluate'):
                ex, pred = future.result()
                texts.append(ex['text'])
                labels.append(ex['label'])
                preds.append(pred)  

        # accuracy = accuracy_score(labels, preds)
        # f1 = f1_score(labels, preds, average='macro')
        if labels and labels != [None] and preds != [None]:
            l = []
            for point in range(len(labels)):
                l.append(np.abs(label_score[int(labels[point])] - label_score[int(preds[point])])**2)
            return np.mean(l), texts, labels, preds
        else:
            return 0, texts, labels, preds

    def evaluate(self, predictor, prompt, test_exs, label_score, n=100):
        while True:
            try:
                f1, texts, labels, preds = self.run_evaluate(predictor, prompt, test_exs, label_score, n=n)
                break
            except (concurrent.futures.process.BrokenProcessPool, requests.exceptions.SSLError):
                pass
        return f1, texts, labels, preds


class BinaryClassificationTask(ClassificationTask):
    categories = ['No', 'Yes']

    def stringify_prediction(self, pred):
        return BinaryClassificationTask.categories[pred]

# 新增多类classification的类
class MulticlassificationTask(ClassificationTask):
    def __init__(self, categories, question_num, data_dir, max_threads=1):
        super().__init__(categories, question_num, data_dir, max_threads)
    def stringify_prediction(self, pred):
        return self.categories[pred]

# class DefaultHFBinaryTask(BinaryClassificationTask):
#     categories = ['No', 'Yes']

#     def get_train_examples(self):
#         exs = []
#         for i, row in enumerate(open(self.data_dir + '/train.jsonl')):
#             row = json.loads(row.strip())
#             exs.append({'id': f'train-{i}', 'label': row['label'], 'text': row['text']})
#         return exs
    
#     def get_test_examples(self):
#         exs = []
#         for i, row in enumerate(open(self.data_dir + '/test.jsonl')):
#             row = json.loads(row.strip())
#             exs.append({'id': f'test-{i}', 'label': row['label'], 'text': row['text']})
#         return exs
    
class MultiTask(MulticlassificationTask):
    def __init__(self, categories, question_num, data_dir, max_threads=1):
        super().__init__(categories, question_num, data_dir, max_threads)
    def get_train_examples(self):
        categories = self.categories
        exs = []
        df_response = pd.read_csv(self.data_dir + '/cluster_14_train.csv').loc[:, ['Background_Prompt'] + ['Q' + str(i) for i in range(int(self.question_num[0]), int(self.question_num[1]) + 1)]]
        df_question = pd.read_csv(self.data_dir + "/field1_" + "class" + str(self.question_num[2]) + "_Q" + str(self.question_num[0]) + "-Q" + str(self.question_num[1]) + ".csv")
        # df_response = df_response.replace({-1: int(self.question_num[2]) + 1, -3: int(self.question_num[2]) + 2, -4: int(self.question_num[2]) + 2, -5: int(self.question_num[2]) + 3})
        df_response = df_response.replace({-1: int(self.question_num[2]) + 1, -3: int(self.question_num[2]) + 1, -4: int(self.question_num[2]) + 1, -5: int(self.question_num[2]) + 1})
        exs, dic = [], {}
        for index, row in df_response.iterrows():
            for col in row.index:
                if col[0] == 'Q':
                    dic['text'] = df_question[col] + ' ' + row['Background_Prompt']
                    dic['label'] = int(row[col]) - 1
                    exs.append(dic)
                    dic = {}
        return exs
    
    def get_test_examples(self):
        exs = []
        df_response = pd.read_csv(self.data_dir + '/cluster_14_test.csv').loc[:, ['Background_Prompt'] + ['Q' + str(i) for i in range(int(self.question_num[0]), int(self.question_num[1]) + 1)]]
        df_question = pd.read_csv(self.data_dir + "/field1_" + "class" + str(self.question_num[2]) + "_Q" + str(self.question_num[0]) + "-Q" + str(self.question_num[1]) + ".csv")
        # df_response = df_response.replace({-1: int(self.question_num[2]) + 1, -3: int(self.question_num[2]) + 2, -4: int(self.question_num[2]) + 2, -5: int(self.question_num[2]) + 3})
        df_response = df_response.replace({-1: int(self.question_num[2]) + 1, -3: int(self.question_num[2]) + 1, -4: int(self.question_num[2]) + 1, -5: int(self.question_num[2]) + 1})
        exs, dic = [], {}
        for index, row in df_response.iterrows():
            for col in row.index:
                if col[0] == 'Q':
                    dic['text'] = df_question[col] + ' ' + row['Background_Prompt']
                    dic['label'] = int(row[col]) - 1
                    exs.append(dic)
                    dic = {}
        return exs

