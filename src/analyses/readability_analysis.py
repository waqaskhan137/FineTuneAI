from .base_analysis import BaseAnalysis
from textstat import flesch_reading_ease

class ReadabilityAnalysis(BaseAnalysis):
    def run(self):
        self.df_dataset["readability_score"] = self.df_dataset["Assistant"].apply(lambda x: flesch_reading_ease(str(x)))
        return self.df_dataset["readability_score"].describe() 