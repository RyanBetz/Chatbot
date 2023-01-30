import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Read the input file
df = pd.read_csv('Twitter_info_2.csv')

# Check if the "Sentiment" column already exists
if "Sentiment" in df.columns:
    # If it does, drop the column
    df = df.drop(columns=["Sentiment"])

# Add a new column "Sentiment"
df["Sentiment"] = None

# Analyze the sentiment of each tweet
for i in range(len(df)):
    tweet = df.loc[i, "Tweet"]
    sentiment = sia.polarity_scores(tweet)
    if sentiment['compound'] >= 0.05:
        sentiment_score = 'positive'
    elif sentiment['compound'] <= -0.05:
        sentiment_score = 'negative'
    else:
        sentiment_score = 'neutral'
    df.loc[i, "Sentiment"] = sentiment_score

# Save the output file
df.to_csv('Twitter_info_2.csv', index=False)
