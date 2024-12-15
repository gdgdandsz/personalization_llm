import requests
import json
import pandas as pd
from openai import OpenAI
from tqdm import tqdm

#need to modify the address
csv_path = 'dataset/train16.csv'
data = pd.read_csv(csv_path)

# question list
questions = [
    "How strongly does respondent agree or disagree that One of my main goals in life has been to make my parents proud?",
    "How strongly does respondent agree or disagree that When a mother works for pay, the children suffer?",
    "How strongly does respondent agree or disagree that On the whole, men make better political leaders than women do?",
    "How strongly does respondent agree or disagree that A university education is more important for a boy than for a girl?",
    "How strongly does respondent agree or disagree that On the whole, men make better business executives than women do?",
    "How strongly does respondent agree or disagree that Being a housewife is just as fulfilling as working for pay?"
]

def summarize_text(text):
    messages = [{"role": "user", "content": f"Summarize the following respondent information into a concise description:\n{text}"}]
    
    response = client.chat.completions.create(
        model=LLM_MODEL_NAME,
        messages=messages,
        temperature=0.3,
        n=1,
        top_p=1,
        stop=None,
        max_tokens=200,
        presence_penalty=0,
        frequency_penalty=0,
        logit_bias={},
    )
    
    try:
        summarized_info = response.choices[0].message.content
        
        return summarized_info
    except KeyError as e:
        print(f"Error: Missing expected field in response - {e}")
        return "Error during summarization."

data_entries = []
for index, row in tqdm(data.iterrows(), total=data.shape[0], desc="Processing Respondents"):
    respondent_info = row[78]
    summarized_info = summarize_text(respondent_info)
    
    for j, question in enumerate(questions):
        entry = {
            "instruction": "Evaluate the statements based on the respondent's demographic profile, taking into account how their age, occupation, education level, and family status may influence their opinions. Choose a response from strongly agree, agree, disagree, or strongly disagree for each statement, considering the potential impact of the respondent's background on their agreement or disagreement.",
            "input": f"Respondent Info: {summarized_info}\n\nQuestion: {question}",
            "output": int(data.iloc[index, j + 29]) if pd.api.types.is_integer_dtype(data.iloc[index, j + 29]) else data.iloc[index, j + 29],
        }
        data_entries.append(entry)

final_data = [{"instruction": entry["instruction"], "input": entry["input"], "output": entry["output"]} for entry in data_entries]

output_path = "train_summarized_16.json"
with open(output_path, "w") as f:
    json.dump(final_data, f, indent=2)

print(f"Saved to {output_path}！")
