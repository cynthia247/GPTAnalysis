import pandas as pd
import openai 

import csv

df = pd.read_csv("../dataset/TestData.csv")
openai.api_key = '<YOUR-API-KEY'

df = df.iloc[100:101, :]
print(df[['Question']].head(5))

def analyze_gpt4(text):
    messages = [
        # {"role": "system", "content": """You are trained to analyze and detect the sentiment of given text. 
        #                                 If you're unsure of an answer, you can say "not sure" and recommend users to review manually."""},
        {"role": "user", "content": f"""Give me a solution: {text}"""}
        ]

    response = openai.chat.completions.create(
        model="gpt-4",
        messages = messages,
        max_tokens=6000,
        n=1,
        stop=None,
        temperature=0)
    
    response_text = response.choices[0].message.content.strip().lower()

    return response_text


ratings = []

csv_file = 'Out.csv'
header = ['Question','GPTGenerated']

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)


for index, row in df.iterrows():
    sent = analyze_gpt4(row['Question'])
    print(sent)
    ratings.append(sent)

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([row['Question'],sent])

# df['predicted_gpt35'] = df['Body'].apply(analyze_gpt35)
# df['GPTGenerated'] = ratings

# print(df.head(10))

# # df.to_csv('SO_Stackoverflow_Data.csv', index=False)
