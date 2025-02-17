from .base_analysis import BaseAnalysis
from textstat import flesch_reading_ease
import numpy as np

class ReadabilityOutlierAnalysis(BaseAnalysis):
    def run(self):
        readability_scores = self.df_dataset["Assistant"].apply(lambda x: flesch_reading_ease(str(x)))
        mean_score = np.mean(readability_scores)
        std_dev = np.std(readability_scores)
        
        # Identify outliers as scores more than 2 standard deviations from the mean
        outliers = readability_scores[(readability_scores < mean_score - 2 * std_dev) | (readability_scores > mean_score + 2 * std_dev)]
        
        return f"Number of Readability Outliers: {len(outliers)}" 