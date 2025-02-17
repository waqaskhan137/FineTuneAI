from .base_analysis import BaseAnalysis
from sentence_transformers import SentenceTransformer, util
import numpy as np

class ContextConsistencyAnalysis(BaseAnalysis):
    def __init__(self, df_dataset, df_evals):
        super().__init__(df_dataset, df_evals)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def run(self):
        texts = self.df_dataset["Assistant"].dropna().tolist()
        embeddings = self.model.encode(texts, convert_to_tensor=True)
        consistency_scores = [util.pytorch_cos_sim(embeddings[i], embeddings[i+1]).item() for i in range(len(texts)-1)]
        avg_consistency = np.mean(consistency_scores)
        return avg_consistency 