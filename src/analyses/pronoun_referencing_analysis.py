from .base_analysis import BaseAnalysis
import spacy
from collections import Counter

class PronounReferencingAnalysis(BaseAnalysis):
    def __init__(self, df_dataset, df_evals):
        super().__init__(df_dataset, df_evals)
        self.nlp = spacy.load("en_core_web_sm")

    def run(self):
        pronoun_counts = Counter()
        for text in self.df_dataset["Assistant"].dropna():
            doc = self.nlp(text)
            pronouns = [token.text for token in doc if token.pos_ == 'PRON']
            pronoun_counts.update(pronouns)

        # Identify potential coherence gaps by checking for high pronoun usage
        coherence_gaps = {pronoun: count for pronoun, count in pronoun_counts.items() if count > 5}

        return coherence_gaps 