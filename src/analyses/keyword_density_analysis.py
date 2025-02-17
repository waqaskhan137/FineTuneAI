from .base_analysis import BaseAnalysis
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

class KeywordDensityAnalysis(BaseAnalysis):
    def run(self):
        # Define key concepts to analyze
        key_concepts = ['concept1', 'concept2', 'concept3']  # Replace with actual keywords

        vectorizer = CountVectorizer(vocabulary=key_concepts)
        term_matrix = vectorizer.fit_transform(self.df_dataset["Assistant"].dropna())

        # Calculate density for each keyword
        densities = np.sum(term_matrix, axis=0).A1 / term_matrix.shape[0]

        # Create a dictionary of keyword densities
        density_dict = {key_concepts[i]: densities[i] for i in range(len(key_concepts))}

        return density_dict 