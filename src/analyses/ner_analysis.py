from .base_analysis import BaseAnalysis
import spacy
from collections import Counter

class NERAnalysis(BaseAnalysis):
    def __init__(self, df_dataset, df_evals):
        super().__init__(df_dataset, df_evals)
        self.nlp = spacy.load("en_core_web_sm")

    def run(self):
        entity_counts = Counter()
        for text in self.df_dataset["Assistant"].dropna():
            doc = self.nlp(text)
            entity_counts.update([ent.label_ for ent in doc.ents])
        return entity_counts.most_common(10) 