class BaseAnalysis:
    def __init__(self, df_dataset, df_evals):
        self.df_dataset = df_dataset
        self.df_evals = df_evals

    def run(self):
        raise NotImplementedError("Subclasses should implement this method.") 