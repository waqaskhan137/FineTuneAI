import pandas as pd
import matplotlib.pyplot as plt
import json
import nltk
import spacy
import tiktoken
import numpy as np
from collections import Counter
from sentence_transformers import SentenceTransformer, util

# Load the Excel file
file_path = "Sample Dataset.xlsx"
xls = pd.ExcelFile(file_path)

# Load datasets
df_dataset = pd.read_excel(xls, sheet_name="Sample Dataset")
df_evals = pd.read_excel(xls, sheet_name="Sample Evals")

# Function: Text Length Analysis
def text_length_analysis(df):
    df["assistant_text_length"] = df["Assistant"].apply(lambda x: len(str(x)))
    return df["assistant_text_length"].describe()

# Function: Extract numerical values from JSON evaluation scores
def extract_scores_fixed(row):
    try:
        data = json.loads(row)
        flow_score = next((int(item["flow"]) for item in data["criteria_scores"] if "flow" in item), None)
        repetition_score = next((int(item["repetition"]) for item in data["criteria_scores"] if "repetition" in item), None)
        return flow_score, repetition_score
    except Exception:
        return None, None

# Function: Token Distribution Analysis
def token_distribution_analysis(df):
    enc = tiktoken.get_encoding("cl100k_base")
    df["token_count"] = df["Assistant"].apply(lambda x: len(enc.encode(str(x))))
    return df["token_count"].describe()

# Function: Lexical Diversity & Word Frequency
def lexical_diversity_analysis(df):
    all_words = " ".join(df["Assistant"].dropna()).split()
    word_counts = Counter(all_words)
    unique_word_ratio = len(set(all_words)) / len(all_words)
    return unique_word_ratio, word_counts.most_common(20)

# Function: POS Tagging Analysis
def pos_tagging_analysis(df):
    nlp = spacy.load("en_core_web_sm")
    pos_counts = Counter()
    for text in df["Assistant"].dropna():
        doc = nlp(text)
        pos_counts.update([token.pos_ for token in doc])
    return pos_counts.most_common(10)

# Function: Sentiment & Readability Analysis
def readability_analysis(df):
    from textstat import flesch_reading_ease
    df["readability_score"] = df["Assistant"].apply(lambda x: flesch_reading_ease(str(x)))
    return df["readability_score"].describe()

# Function: Embedding Similarity Analysis
def embedding_similarity_analysis(df):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(df["Assistant"].dropna().tolist(), convert_to_tensor=True)
    similarity_matrix = util.pytorch_cos_sim(embeddings, embeddings).cpu().numpy()
    avg_similarity = np.mean(similarity_matrix)
    return avg_similarity

# Function: Context Consistency Check
def context_consistency_analysis(df):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    texts = df["Assistant"].dropna().tolist()
    embeddings = model.encode(texts, convert_to_tensor=True)
    consistency_scores = [util.pytorch_cos_sim(embeddings[i], embeddings[i+1]).item() for i in range(len(texts)-1)]
    avg_consistency = np.mean(consistency_scores)
    return avg_consistency

# Execute analyses
text_length_stats = text_length_analysis(df_dataset)
df_evals["flow_scores"], df_evals["repetition_scores"] = zip(*df_evals.iloc[:, 2].apply(extract_scores_fixed))
repetition_stats_fixed = df_evals["repetition_scores"].describe()
flow_stats_fixed = df_evals["flow_scores"].describe()
token_stats = token_distribution_analysis(df_dataset)
lexical_diversity, common_words = lexical_diversity_analysis(df_dataset)
pos_tags = pos_tagging_analysis(df_dataset)
readability_stats = readability_analysis(df_dataset)
avg_embedding_similarity = embedding_similarity_analysis(df_dataset)
avg_context_consistency = context_consistency_analysis(df_dataset)

# Generate Markdown Report with Explanations
report = f"""
# Dataset Analysis Report

## Text Length Analysis
This section provides statistics on the length of text responses from the assistant. It helps in understanding the verbosity of the responses.
{text_length_stats.to_markdown()}

## Token Distribution Analysis
This section analyzes the distribution of tokens in the assistant's responses, which is useful for understanding the complexity and structure of the text.
{token_stats.to_markdown()}

## Lexical Diversity
Lexical diversity measures the variety of words used in the text. A higher unique word ratio indicates a richer vocabulary.
- Unique Word Ratio: {lexical_diversity:.4f}
- Most Common Words: {common_words}

## Part-of-Speech (POS) Tagging Analysis
This section shows the most common parts of speech in the assistant's responses, providing insights into the grammatical structure of the text.
{pos_tags}

## Readability Analysis
Readability scores indicate how easy or difficult the text is to read. This section uses the Flesch Reading Ease score.
{readability_stats.to_markdown()}

## Embedding Similarity Analysis
This analysis measures the semantic similarity between different responses. A higher average similarity score suggests more consistent responses.
- Average Similarity Score: {avg_embedding_similarity:.4f}

## Context Consistency Analysis
This section evaluates how consistent the context is between consecutive responses, which is crucial for maintaining coherent conversations.
- Average Consistency Score: {avg_context_consistency:.4f}

## Repetition Score Distribution
This section provides statistics on the repetition scores extracted from the evaluation data, indicating how often the assistant repeats itself.
{repetition_stats_fixed.to_markdown()}

## Flow Score Distribution
Flow scores measure the logical flow of the assistant's responses. This section provides a distribution of these scores.
{flow_stats_fixed.to_markdown()}
"""

# Save report to a markdown file
with open("dataset_analysis_report.md", "w") as f:
    f.write(report)

# Display report content
print(report)
