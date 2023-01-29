import csv
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Open the input file in read mode
with open('Twitter_info_2.csv', 'r') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames + ['Sentiment']
    # Open the output file in write mode
    with open('Twitter_info_2.csv', 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            tweet = row['Tweet']
            sentiment = sia.polarity_scores(tweet)
            if sentiment['compound'] >= 0.05:
                row['Sentiment'] = 'positive'
            elif sentiment['compound'] <= -0.05:
                row['Sentiment'] = 'negative'
            else:
                row['Sentiment'] = 'neutral'
            writer.writerow(row)
#generate summary statistics of the sentiment
#delete the last column
df = pd.read_csv('Twitter_info_2.csv')
df = df.drop(columns=['Sentiment'])
#save the file
df.to_csv('Twitter_info_2.csv')