import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import spacy as sp
from nltk import word_tokenize
from wordcloud import STOPWORDS
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
#include other stopwords and numbers to remove
stop_words = set(STOPWORDS)
stop_words.add("https")
stop_words.add("co")
stop_words.add("rt")
stop_words.add("RT")
stop_words.add("14")
#create csv with onl the column 3 in twitter_info.csv
df = pd.read_csv('Twitter_info.csv', usecols=[2])
#iterate through each row in the csv
def classify_sentiment(row):
    if 'good' in row['Tweet']:
        return 'Positive'
    elif 'bad' in row['Tweet']:
        return 'Negative'
    else:
        return 'Neutral'

df['Sentiment'] = df.apply(classify_sentiment, axis=1)
#use n-grams to find the most common words and remove stop words
#vect = CountVectorizer(ngram_range=(1,2), max_features=10, stop_words=stop_words)
#vect.fit(df['Tweet'])
#vect_transform = vect.transform(df['Tweet'])
#vect_df = pd.DataFrame(vect_transform.toarray(), columns=vect.get_feature_names_out())
#print(vect_df)
#count the number o f positive, negative, and neutral tweets
print(df['Sentiment'].value_counts())
#tokenize the tweets using word tokenize
tokens_tweets = [word_tokenize(tweet) for tweet in df['Tweet']]
#iterate through each tokenized tweet and create new feature for the length of each tweets
#lemmatize the tweets
nlp = sp.load('en_core_web_sm')
lemmatized_tweets = []
for tweet in df['Tweet']:
    lemmatized_tweets.append([token.lemma_ for token in nlp(tweet)])
#remove all stop words and numbers from lemmatized tweets
for index, tweet in enumerate(lemmatized_tweets):
    lemmatized_tweets[index] = [word for word in tweet if word not in stop_words and not word.isnumeric()]
#perform sentiment analysis on the lemmatized tweets
#vectorize the training and testing data


#save the csv
df.to_csv('Twitter_info_3.csv')














