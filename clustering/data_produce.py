import pandas as pd
import json

def extract_instruction_from_md(md_path):
    # 读取并解析 Markdown 文件以提取 Task 部分
    task_content = ''
    with open(md_path, 'r') as file:
        capture = False
        for line in file:
            if line.strip() == '# Task':
                capture = True
            elif line.strip().startswith('#') and capture:
                break
            elif capture:
                task_content += line
    return task_content.strip()

def generate_training_data(question_files, dataset_path, output_json_path):
    # 初始化 JSON 数据数组
    json_data = []
    
    # 加载包含背景提示的数据集
    background_df = pd.read_csv(dataset_path)

    # 遍历每个问题文件
    for class_label, file_info in question_files.items():
        # 从 Markdown 文件中提取指令
        instruction = extract_instruction_from_md(file_info['md_path'])
        
        # 读取问题文件
        questions_df = pd.read_csv(file_info['csv_path'])
        # 筛选以 'Q' 开头的列，这些列包含问题编号
        question_columns = [col for col in questions_df.columns if col.startswith('Q')]

        # 为该类别的每个问题生成条目
        for col in question_columns:
            question_text = questions_df.iloc[0][col]  # 假设问题描述在第一行
            for index, row in background_df.iterrows():
                # 检查问题编号列是否在背景提示数据集中
                if col in background_df.columns:
                    # 构建条目
                    entry = {
                        "instruction": instruction,
                        "input": row['Background_Prompt'] + " " + question_text,
                        "output": f"{row[col]}\n"
                    }
                    json_data.append(entry)
    
    # 将所有条目保存为 JSON 文件
    with open(output_json_path, 'w') as file:
        json.dump(json_data, file, indent=4, ensure_ascii=False)

# 问题文件的路径和相应的说明
question_files = {
    "class4": {
        "csv_path": "/scratch/wd2148/prompt_optimization/data/field1_class4_Q1-Q6.csv",
        "md_path": "/scratch/wd2148/prompt_optimization/prompts/field1_class4_Q1-Q6.md"
    }
    ,
    "class2": {
        "csv_path": "/scratch/wd2148/prompt_optimization/data/field1_class2_Q7-Q17.csv",
        "md_path": "/scratch/wd2148/prompt_optimization/prompts/field1_class2_Q7-Q17.md"
    }
}
# 背景提示数据集路径
dataset_path = "/scratch/wd2148/cluster0_test/clustered_data_label_0_test.csv"

# 指定输出 JSON 文件的路径
output_json_path = "/scratch/wd2148/cluster0_test/test_1205.json"

# 生成 training_data.json
generate_training_data(question_files, dataset_path, output_json_path)
