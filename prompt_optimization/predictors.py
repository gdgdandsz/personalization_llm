from abc import ABC, abstractmethod
from typing import List, Dict, Callable
from liquid import Template
import string
import utils  # 调用修改后的 llama utils.py
import tasks  # 根据需要保留或修改
import warnings
warnings.filterwarnings("ignore")
class LLamaPredictor(ABC):  # 修改类名称为 LLamaPredictor
    def __init__(self, opt):
        self.opt = opt

    @abstractmethod
    def inference(self, ex, prompt):
        pass

class BinaryPredictor(LLamaPredictor):  # 确保它继承新的 LLamaPredictor
    categories = ['No', 'Yes']

    def inference(self, ex, prompt):
        # 渲染 prompt，类似之前 GPT-4 版本
        prompt = Template(prompt).render(text=ex['text'])

        # 使用 llama 的 chatgpt 函数替换原来的 GPT-4 调用
        response = utils.chatgpt(
            prompt, max_tokens=4, n=1, timeout=2, 
            temperature=self.opt['temperature'])[0]
        
        # 基于 LLaMA 模型的输出预测二分类结果
        pred = 1 if response.strip().upper().startswith('YES') else 0
        return pred
    
    
class MultiPredictor(LLamaPredictor):  # 确保它继承新的 LLamaPredictor
    def __init__(self, opt, categories):  # Add custom_param as a new parameter
        super().__init__(opt)
        self.categories = categories
        
    def inference(self, ex, prompt):
        # 渲染 prompt，类似之前 GPT-4 版本
        prompt = Template(prompt).render(text=ex['text'])
        pred = -1
        # 使用 llama 的 chatgpt 函数替换原来的 GPT-4 调用
        response = utils.chatgpt(
            prompt, max_tokens=4, n=1, timeout=2, 
            temperature=self.opt['temperature'])[0]
        response_cleaned = response.translate(str.maketrans('', '', string.punctuation)).strip().upper()
        # 判断响应包含某个字段 (判断是否包含某些关键词)
        for res_idx in range(len(self.categories)):
            if self.categories[res_idx].strip().upper() == response_cleaned:
                return res_idx