from .base_analysis import BaseAnalysis
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

class TFIDFAnalysis(BaseAnalysis):
    def run(self):
        # Drop NaN values and convert to a list
        texts = self.df_dataset["Assistant"].dropna().tolist()
        
        # Initialize the TF-IDF Vectorizer
        vectorizer = TfidfVectorizer(stop_words='english', max_features=20)
        
        # Fit and transform the text data
        tfidf_matrix = vectorizer.fit_transform(texts)
        
        # Get feature names (words)
        feature_names = vectorizer.get_feature_names_out()
        
        # Sum the TF-IDF scores for each word across all documents
        tfidf_scores = tfidf_matrix.sum(axis=0).A1
        
        # Create a DataFrame with words and their corresponding TF-IDF scores
        tfidf_df = pd.DataFrame({'word': feature_names, 'tfidf_score': tfidf_scores})
        
        # Sort the DataFrame by TF-IDF score in descending order
        tfidf_df = tfidf_df.sort_values(by='tfidf_score', ascending=False)
        
        # Return the top 20 words with the highest TF-IDF scores
        return tfidf_df.head(20) 