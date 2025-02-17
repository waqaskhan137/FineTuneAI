from .base_analysis import BaseAnalysis

class TextLengthAnalysis(BaseAnalysis):
    def run(self):
        self.df_dataset["assistant_text_length"] = self.df_dataset["Assistant"].apply(lambda x: len(str(x)))
        return self.df_dataset["assistant_text_length"].describe() 