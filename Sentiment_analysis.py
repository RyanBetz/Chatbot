import csv
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

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
