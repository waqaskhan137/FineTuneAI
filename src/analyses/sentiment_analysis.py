from .base_analysis import BaseAnalysis
from textblob import TextBlob
from collections import Counter

class SentimentAnalysis(BaseAnalysis):
    def run(self):
        sentiment_counts = Counter()
        for text in self.df_dataset["Assistant"].dropna():
            polarity = TextBlob(text).sentiment.polarity
            if polarity > 0:
                sentiment_counts['positive'] += 1
            elif polarity < 0:
                sentiment_counts['negative'] += 1
            else:
                sentiment_counts['neutral'] += 1
        return sentiment_counts 