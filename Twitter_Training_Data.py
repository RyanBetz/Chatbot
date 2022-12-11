
import pandas as pd
#import twitter training data
see = pd.read_csv(r"C:\Users\ryanb\OneDrive\tweets_data.csv", encoding = 'latin-1')
#change when label column is 1 to negative
see.loc[see['label'] == 1, 'label'] = 'Negative'
#change when label column is 0 to other
see.loc[see['label'] == 0, 'label'] = 'Positive/Neutral'
#save the csv
see.to_csv('Twitter_info_4.csv')