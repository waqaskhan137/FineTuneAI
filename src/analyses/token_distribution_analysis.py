from .base_analysis import BaseAnalysis
import tiktoken

class TokenDistributionAnalysis(BaseAnalysis):
    def __init__(self, df_dataset, df_evals):
        super().__init__(df_dataset, df_evals)
        self.enc = tiktoken.get_encoding("cl100k_base")

    def run(self):
        self.df_dataset["token_count"] = self.df_dataset["Assistant"].apply(lambda x: len(self.enc.encode(str(x))))
        return self.df_dataset["token_count"].describe() 