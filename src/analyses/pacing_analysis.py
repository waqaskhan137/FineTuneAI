from .base_analysis import BaseAnalysis
import numpy as np
import nltk

class PacingAnalysis(BaseAnalysis):
    def run(self):
        nltk.download('punkt')
        sentence_lengths = []

        for text in self.df_dataset["Assistant"].dropna():
            sentences = nltk.sent_tokenize(text)
            lengths = [len(nltk.word_tokenize(sentence)) for sentence in sentences]
            sentence_lengths.extend(lengths)

        avg_length = np.mean(sentence_lengths)
        std_dev = np.std(sentence_lengths)

        # Detect pacing issues as sentences that deviate significantly from the average length
        pacing_issues = [length for length in sentence_lengths if abs(length - avg_length) > 2 * std_dev]

        return f"Number of Pacing Issues Detected: {len(pacing_issues)}" 