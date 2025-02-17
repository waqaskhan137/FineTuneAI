from .base_analysis import BaseAnalysis
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

class NgramAnalysis(BaseAnalysis):
    def run(self):
        # Drop NaN values and convert to a list
        texts = self.df_dataset["Assistant"].dropna().tolist()
        
        # Initialize the CountVectorizer for bigrams and trigrams
        vectorizer = CountVectorizer(ngram_range=(2, 3), stop_words='english', max_features=20)
        
        # Fit and transform the text data
        ngram_matrix = vectorizer.fit_transform(texts)
        
        # Get feature names (n-grams)
        feature_names = vectorizer.get_feature_names_out()
        
        # Sum the counts for each n-gram across all documents
        ngram_counts = ngram_matrix.sum(axis=0).A1
        
        # Create a DataFrame with n-grams and their corresponding counts
        ngram_df = pd.DataFrame({'ngram': feature_names, 'count': ngram_counts})
        
        # Sort the DataFrame by count in descending order
        ngram_df = ngram_df.sort_values(by='count', ascending=False)
        
        # Return the top 20 n-grams with the highest counts
        return ngram_df.head(20) 