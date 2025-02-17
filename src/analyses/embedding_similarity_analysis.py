from .base_analysis import BaseAnalysis
from sentence_transformers import SentenceTransformer, util
import numpy as np

class EmbeddingSimilarityAnalysis(BaseAnalysis):
    def __init__(self, df_dataset, df_evals):
        super().__init__(df_dataset, df_evals)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def run(self):
        # Example implementation: calculate average similarity between responses
        embeddings = self.model.encode(self.df_dataset["Assistant"].dropna().tolist(), convert_to_tensor=True)
        similarity_matrix = util.pytorch_cos_sim(embeddings, embeddings).cpu().numpy()
        avg_similarity = np.mean(similarity_matrix)
        return f"Average Embedding Similarity: {avg_similarity:.4f}" 