from .base_analysis import BaseAnalysis
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

class TopicModelingAnalysis(BaseAnalysis):
    def run(self):
        # Drop NaN values and convert to a list
        texts = self.df_dataset["Assistant"].dropna().tolist()
        
        # Initialize the CountVectorizer
        vectorizer = CountVectorizer(stop_words='english')
        text_matrix = vectorizer.fit_transform(texts)
        
        # Initialize the LDA model
        lda = LatentDirichletAllocation(n_components=5, random_state=42)
        lda.fit(text_matrix)
        
        # Get feature names (words)
        feature_names = vectorizer.get_feature_names_out()
        
        # Extract topics
        topics = []
        for topic_idx, topic in enumerate(lda.components_):
            top_features = [feature_names[i] for i in topic.argsort()[:-11:-1]]
            topics.append(f"Topic {topic_idx + 1}: " + ", ".join(top_features))
        
        return topics 