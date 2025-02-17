from .base_analysis import BaseAnalysis
from sentence_transformers import SentenceTransformer, util
import numpy as np

class ContrastiveSimilarityAnalysis(BaseAnalysis):
    def __init__(self, df_dataset, df_evals):
        super().__init__(df_dataset, df_evals)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def run(self):
        # Check if the 'QueryGroup' column exists
        if 'QueryGroup' not in self.df_dataset.columns:
            return "Contrastive Similarity Analysis could not be performed: 'QueryGroup' column is missing."

        grouped_texts = self.df_dataset.groupby('QueryGroup')["Assistant"].apply(list)
        contrastive_scores = []
        
        for texts in grouped_texts:
            if len(texts) > 1:
                embeddings = self.model.encode(texts, convert_to_tensor=True)
                similarity_matrix = util.pytorch_cos_sim(embeddings, embeddings).cpu().numpy()
                contrastive_score = 1 - np.mean(similarity_matrix)
                contrastive_scores.append(contrastive_score)
        
        avg_contrastive_score = np.mean(contrastive_scores)
        return f"Average Contrastive Similarity Score: {avg_contrastive_score:.4f}" 