import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import spacy as sp
from nltk import word_tokenize
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from transformers import AutoTokenizer, AutoModelForSequenceClassification

import nltk

#nltk.download('punkt')

# read twitter_info.csv
df = pd.read_csv('Twitter_info_2.csv')
# tokenize the twitter_info.csv tweets
#use a model to run sentiment analysis
tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
# save the csv with the predictions
df.to_csv('Twitter_info_2.csv')
