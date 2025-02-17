from .base_analysis import BaseAnalysis
import spacy
from collections import Counter

class POSTaggingAnalysis(BaseAnalysis):
    def __init__(self, df_dataset, df_evals):
        super().__init__(df_dataset, df_evals)
        self.nlp = spacy.load("en_core_web_sm")

    def run(self):
        pos_counts = Counter()
        for text in self.df_dataset["Assistant"].dropna():
            doc = self.nlp(text)
            pos_counts.update([token.pos_ for token in doc])
        return pos_counts.most_common(10) 