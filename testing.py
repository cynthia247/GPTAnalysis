import pandas as pd
import re

def selectDataframeAndChangingColumnName():
    df = pd.read_csv('../dataset/SO_Data.csv')
    df = df.iloc[0:1000,:]
    df = df[['Body', 'Body.1']].copy()
    df = df.rename(columns={'Body': 'Question', 'Body.1': 'Human_answer'})
    # df.to_csv('../dataset/TestData.csv')


def RemovingHTMLTags():
    df = pd.read_csv('../dataset/TestData.csv')

    # Define a function to clean the text
    def clean_text(text):
        clean = re.compile('<.*?>')
        cleaned_text = re.sub(clean, '', text)
        return cleaned_text

    # Apply the clean_text function to the "Question" column
    df['Question'] = df['Question'].apply(clean_text)
    df['Human_answer'] = df['Human_answer'].apply(clean_text)

    # Replace multiple consecutive whitespaces with a single space in the "Question" column
    df['Question'] = df['Question'].replace(r'\s+', ' ', regex=True)
    df['Human_answer'] = df['Human_answer'].replace(r'\s+', ' ', regex=True)

    # Print the DataFrame with the cleaned "Question" column
    print(df.head(5))
    df.to_csv('../dataset/TestData.csv', index=False)

RemovingHTMLTags()