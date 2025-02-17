from .base_analysis import BaseAnalysis
from collections import Counter

class LexicalDiversityAnalysis(BaseAnalysis):
    def run(self):
        all_words = " ".join(self.df_dataset["Assistant"].dropna()).split()
        word_counts = Counter(all_words)
        unique_word_ratio = len(set(all_words)) / len(all_words)
        return unique_word_ratio, word_counts.most_common(20) 