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

#create bag of words model
cv = CountVectorizer()
#transform the vectorizer using pandas dataframe
X = cv.fit_transform(df['Tweet'])
#convert the vectorizer to a dataframe
df = pd.DataFrame(X.toarray(), columns=cv.get_feature_names())
#save the dataframe
df.to_csv('Twitter_info_3.csv')








