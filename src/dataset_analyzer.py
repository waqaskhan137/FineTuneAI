import pandas as pd
from analyses.text_length_analysis import TextLengthAnalysis
from analyses.token_distribution_analysis import TokenDistributionAnalysis
# Import other analyses as needed

class DatasetAnalyzer:
    def __init__(self, dataset_path):
        self.file_path = dataset_path
        self.xls = pd.ExcelFile(self.file_path)
        self.df_dataset = pd.read_excel(self.xls, sheet_name="Sample Dataset")
        self.df_evals = pd.read_excel(self.xls, sheet_name="Sample Evals")
        self.analyses = []

    def register_analysis(self, analysis_class):
        analysis = analysis_class(self.df_dataset, self.df_evals)
        self.analyses.append(analysis)

    def execute_analyses(self):
        results = {}
        for analysis in self.analyses:
            result = analysis.run()
            results[analysis.__class__.__name__] = result
        return results 