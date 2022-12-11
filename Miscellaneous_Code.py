from wordcloud import STOPWORDS
import pandas as pd
stop_words = set(STOPWORDS)
stop_words.add("https")
stop_words.add("co")
stop_words.add("rt")
stop_words.add("RT")
stop_words.add("14")
#create csv with onl the column 3 in twitter_info.csv
df = pd.read_csv('Twitter_info.csv', usecols=[2])
#iterate through each row in the csv
#def classify_sentiment(row):
#    if 'good' in row['Tweet']:
#        return 'Positive'
#    elif 'bad' in row['Tweet']:
#        return 'Negative'
#    else:
#        return 'Neutral'
#df['Sentiment'] = df.apply(classify_sentiment, axis=1)
#use n-grams to find the most common words and remove stop words
#vect = CountVectorizer(ngram_range=(1,2), max_features=10, stop_words=stop_words)
#vect.fit(df['Tweet'])
#vect_transform = vect.transform(df['Tweet'])
#vect_df = pd.DataFrame(vect_transform.toarray(), columns=vect.get_feature_names_out())
#print(vect_df)
#count the number o f positive, negative, and neutral tweets
#print(df['Sentiment'].value_counts())