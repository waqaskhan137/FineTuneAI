from .base_analysis import BaseAnalysis
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

class ResponseRedundancyAnalysis(BaseAnalysis):
    def run(self):
        redundancy_scores = []
        vectorizer = CountVectorizer(stop_words='english')
        
        for text in self.df_dataset["Assistant"].dropna():
            term_matrix = vectorizer.fit_transform([text])
            term_counts = np.sum(term_matrix.toarray(), axis=0)
            redundancy_score = np.sum(term_counts > 1) / len(term_counts)
            redundancy_scores.append(redundancy_score)
        
        avg_redundancy_score = np.mean(redundancy_scores)
        return f"Average Redundancy Score: {avg_redundancy_score:.4f}" 