"""
https://oai.azure.com/portal/be5567c3dd4d49eb93f58914cccf3f02/deployment
clausa gpt4
"""

import time
import string
import config
from openai import OpenAI
import warnings
warnings.filterwarnings("ignore")

# 使用 OpenAI SDK 初始化客户端对象
client = OpenAI(
    base_url="https://vllm.ml1.ritsdev.top/v1/",
    api_key="token-abc123",
)
# 获取模型名称
LLM_MODEL_NAME = client.models.list().data[0].id

def parse_sectioned_prompt(s):
    """
    将包含多个段落的提示语按 # header 进行分割，返回一个字典对象
    """
    result = {}
    current_header = None

    for line in s.split('\n'):
        line = line.strip()

        if line.startswith('# '):
            # 处理 header 名称，去除标点符号
            current_header = line[2:].strip().lower().split()[0]
            current_header = current_header.translate(str.maketrans('', '', string.punctuation))
            result[current_header] = ''
        elif current_header is not None:
            result[current_header] += line + '\n'

    return result

def chatgpt(prompt, temperature=0.7, n=1, top_p=1, stop=None, max_tokens=1024, 
                   presence_penalty=0, frequency_penalty=0, logit_bias={}, timeout=10):
    """
    使用 OpenAI API 的 chat.completions 端点来获取对话模型的回复。
    """
    messages = [{"role": "user", "content": prompt}]
    
    response = client.chat.completions.create(  # 使用 client 调用
        model=LLM_MODEL_NAME,
        messages=messages,
        temperature=temperature,
        n=n,
        top_p=top_p,
        stop=stop,
        max_tokens=max_tokens,
        presence_penalty=presence_penalty,
        frequency_penalty=frequency_penalty,
        logit_bias=logit_bias,
    )
    
    #print(response)
    return [choice.message.content for choice in response.choices]

def instructGPT_logprobs(prompt, temperature=0.7):
    """
    使用 OpenAI API 的 completions 端点来获取 logprobs（对数概率）。
    """
    response = client.chat.completions.create(  # 使用 client 调用
        # model="text-davinci-003",
        model=LLM_MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],  # 适配成 chat API
        temperature=temperature,
        max_tokens=1,
        logprobs=1,
        # echo = True
    )

    # 返回生成的所有内容，包括 logprobs 信息
    return response.choices

# import time
# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch
# import torch.nn.functional as F
# import string

# # 加载 Hugging Face 的 Llama 模型和分词器
# model_name = "meta-llama/Meta-Llama-3.1-8B-Instruct"
# tokenizer = AutoTokenizer.from_pretrained(model_name, token="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")
# model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", torch_dtype=torch.float16)

# def parse_sectioned_prompt(s):
#     result = {}
#     current_header = None
#     for line in s.split('\n'):
#         line = line.strip()
#         if line.startswith('# '):
#             current_header = line[2:].strip().lower().split()[0]
#             current_header = current_header.translate(str.maketrans('', '', string.punctuation))
#             result[current_header] = ''
#         elif current_header is not None:
#             result[current_header] += line + '\n'
#     return result

# def chatgpt(prompt, temperature=0.7, n=1, top_p=1, stop=None, max_tokens=1024, 
#                   presence_penalty=0, frequency_penalty=0, logit_bias={}, timeout=10):
#     inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
#     outputs = model.generate(
#         **inputs,
#         max_length=1024,
#         num_return_sequences=n,
#         do_sample=True,
#         temperature=0.7,
#         top_p=top_p,
#     )
#     generated_texts = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
#     return generated_texts

# def instructGPT_logprobs(prompt, temperature=0.7):
#     inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
#     outputs = model(**inputs)
#     logits = outputs.logits[:, -1, :]  
#     probs = F.softmax(logits / temperature, dim=-1)  
#     top_prob, top_token = torch.max(probs, dim=-1)
#     logprobs = torch.log(top_prob)
#     decoded_token = tokenizer.decode([top_token.item()])
#     return {
#         'token': decoded_token,
#         'logprob': logprobs.item()
#     }