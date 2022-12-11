import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import spacy as sp
from nltk import word_tokenize
from wordcloud import STOPWORDS
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
#create csv with onl the column 3 in twitter_info.csv
df = pd.read_csv('Twitter_info.csv', usecols=[2])
#read twitter_info_4.csv
df_2 = pd.read_csv('Twitter_info_4.csv')
#tokenize the twitter_info_3.csv tweets
df['tweet'] = df['tweet'].apply(word_tokenize)
#tokenize the twitter_info_4.csv tweets
df_2['tweet'] = df_2['tweet'].apply(word_tokenize)
#lemmatize the tweets
nlp = sp.load('en_core_web_sm')
lemmatized_tweets_1 = []
for tweet in df['Tweet']:
    lemmatized_tweets_1.append([token.lemma_ for token in nlp(tweet)])
#remove all stop words and numbers from lemmatized tweets
for index, tweet in enumerate(lemmatized_tweets_1):
    lemmatized_tweets_1[index] = [word for word in tweet]
#save the csv
df.to_csv('Twitter_info_3.csv')














