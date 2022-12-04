import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import spacy as sp

#create csv with onl the column 3 in twitter_info.csv
df = pd.read_csv('Twitter_info.csv', usecols=[2])
#iterate through each row in the csv
for index, row in df.iterrows():
    #identify if each row contains a positive or negative word and add a column to the csv
    if 'good' in row['Tweet']:
        df.loc[index, 'Sentiment'] = 'Positive'
    elif 'bad' in row['Tweet']:
        df.loc[index, 'Sentiment'] = 'Negative'
    else:
        df.loc[index, 'Sentiment'] = 'Neutral'
#save the csv
df.to_csv('Twitter_info_3.csv')
#count the number of positive, negative, and neutral tweets
print(df['Sentiment'].value_counts())

#use n-grams to find the most common words
vect = CountVectorizer(ngram_range=(1,2), max_features=100)
vect.fit(df['Tweet'])
vect_transform = vect.transform(df['Tweet'])
vect_df = pd.DataFrame(vect_transform.toarray(), columns=vect.get_feature_names_out())
print(vect_df)
#use spacy to fin










