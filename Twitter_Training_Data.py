import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk import word_tokenize
#import twitter training data
see = pd.read_csv(r"C:\Users\ryanb\OneDrive\tweets_data.csv", encoding = 'latin-1')
#change when label column is 1 to negative
see.loc[see['label'] == 1, 'label'] = 'Negative'
#change when label column is 0 to other
see.loc[see['label'] == 0, 'label'] = 'Positive/Neutral'
#vectorize the tweets
vect = CountVectorizer(ngram_range=(1,2), max_features=10)
vect.fit(see['tweet'])
vect_transform = vect.transform(see['tweet'])
vect_df = pd.DataFrame(vect_transform.toarray(), columns=vect.get_feature_names_out())
#tokenize the tweets
tokens_tweets = [word_tokenize(tweet) for tweet in see['tweet']]
#save the csv
see.to_csv('Twitter_info_4.csv')