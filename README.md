# Finetune Analysis

This project performs various analyses on a dataset using Python. It includes text length analysis, token distribution, lexical diversity, part-of-speech tagging, readability, embedding similarity, and context consistency checks. The results are compiled into a markdown report.

## Features

- **Text Length Analysis**: Provides statistics on the length of text responses.
- **Token Distribution Analysis**: Analyzes the distribution of tokens in the text.
- **Lexical Diversity**: Measures the variety of words used in the text.
- **POS Tagging Analysis**: Shows the most common parts of speech.
- **Readability Analysis**: Uses the Flesch Reading Ease score to evaluate text readability.
- **Embedding Similarity Analysis**: Measures semantic similarity between responses.
- **Context Consistency Analysis**: Evaluates consistency between consecutive responses.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/waqaskhan137/finetune.git
   cd finetune
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Required Models**:
   Ensure you have the necessary NLP models downloaded for `spacy` and `sentence-transformers`.

5. **Run the Analysis**:
   Execute the script to perform the analysis and generate the report:
   ```bash
   python app.py
   ```

## Requirements

- Python 3.x
- See `requirements.txt` for a list of Python packages.

## Output

The analysis results are saved in `dataset_analysis_report.md`, providing a detailed markdown report of the dataset analysis.

## Contact

For any questions or issues, please contact [Waqas](mailto:waqaskhan137@gmail.com). 