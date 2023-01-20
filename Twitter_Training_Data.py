import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk import word_tokenize
#read tweets_training_data.csv with latin-1 encoding
df = pd.read_csv('/Users/ryanbetz/Library/CloudStorage/OneDrive-Personal/tweets_training_data.csv', encoding='latin-1')
#create a new header column for the csv
df.columns = ['target', 'ID', 'Date', 'Flag', 'User', 'Tweet']
#change column "target" to "Positive" when the value is 4 and "Negative" when the value is 0 and "Neutral" when the value is 2
df['target'] = df['target'].replace(4, 'Positive')
df['target'] = df['target'].replace(0, 'Negative')
df['target'] = df['target'].replace(2, 'Neutral')
#tokenize the tweets
df['Tweet'] = df['Tweet'].apply(word_tokenize)
#save the csv
df.to_csv('Twitter_Training_Data.csv')