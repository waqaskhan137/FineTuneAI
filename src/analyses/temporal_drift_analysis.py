from .base_analysis import BaseAnalysis
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd

class TemporalDriftAnalysis(BaseAnalysis):
    def run(self):
        # Check if the 'Date' column exists
        if 'Date' not in self.df_dataset.columns:
            return "Temporal Drift Analysis could not be performed: 'Date' column is missing."

        self.df_dataset['Date'] = pd.to_datetime(self.df_dataset['Date'])
        self.df_dataset.sort_values('Date', inplace=True)
        
        vectorizer = CountVectorizer(stop_words='english')
        term_matrix = vectorizer.fit_transform(self.df_dataset["Assistant"].dropna())
        
        # Calculate term usage over time
        term_usage = np.sum(term_matrix, axis=0)
        term_usage_over_time = np.diff(term_usage, axis=0)
        
        # Measure drift as variance in term usage
        drift_score = np.var(term_usage_over_time)
        return f"Temporal Drift Score: {drift_score:.4f}" 