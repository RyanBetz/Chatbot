import pandas as pd
import spacy
#create csv with onl the column 3 in twitter_info.csv
df = pd.read_csv('Twitter_info.csv', usecols=[2])
#remove column 1 in twitter_info.csv

df.to_csv('Twitter_info_3.csv')
#iterate through each row in the csv
#add a new column to the csv titled sentiment
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



