# Embedding Similarity Analysis

This analysis measures the semantic similarity between different responses, suggesting response consistency.

Average Embedding Similarity: 0.1922


---

# TF-IDF Analysis

This analysis identifies important words that contribute to differentiation in scripts using TF-IDF scores.

| word     |   tfidf_score |
|:---------|--------------:|
| h1       |      2.85366  |
| going    |      1.53693  |
| day      |      1.36295  |
| say      |      1.35671  |
| don      |      1.33713  |
| just     |      1.22112  |
| need     |      1.20009  |
| want     |      1.1893   |
| protein  |      1.18363  |
| make     |      1.1724   |
| help     |      1.12659  |
| ll       |      1.00504  |
| like     |      0.987547 |
| dividend |      0.983426 |
| cashback |      0.97076  |
| walking  |      0.940861 |
| really   |      0.886617 |
| vaccine  |      0.874708 |
| lot      |      0.719534 |
| people   |      0.567022 |


---

# Readability Analysis

This analysis uses the Flesch Reading Ease score to evaluate how easy or difficult the text is to read.

|   readability_score |
|--------------------:|
|            10       |
|            66.132   |
|             9.49794 |
|            44.75    |
|            62.5375  |
|            66.655   |
|            71.0625  |
|            78.28    |


---

# PronounReferencingAnalysis



- that: 74
- their: 25
- it: 99
- you: 301
- That: 13
- they: 33
- them: 18
- all: 11
- her: 6
- You: 30
- this: 23
- your: 111
- who: 12
- It: 28
- I: 73
- This: 13
- what: 32
- yourself: 13
- we: 25
- its: 13
- What: 10
- They: 6
- there: 14
- something: 11
- which: 19
- my: 14
- our: 17
- us: 8
- me: 13
- the: 6
- 's: 6
- Your: 7
- anything: 7


---

# ContrastiveSimilarityAnalysis



Contrastive Similarity Analysis could not be performed: 'QueryGroup' column is missing.


---

# Context Consistency Analysis

This analysis evaluates how consistent the context is between consecutive responses, crucial for coherent conversations.

- Average Consistency Score: 0.1281


---

# TemporalDriftAnalysis



Temporal Drift Analysis could not be performed: 'Date' column is missing.


---

# GrammarSyntaxAnalysis



Average grammar/syntax errors per text: 2.90


---

# Part-of-Speech (POS) Tagging Analysis

This analysis shows the most common parts of speech in the assistant's responses, providing grammatical insights.

[('NOUN', 1514), ('VERB', 1251), ('PRON', 1154), ('PUNCT', 1021), ('ADP', 802), ('DET', 686), ('ADJ', 623), ('AUX', 604), ('ADV', 511), ('PART', 335)]


---

# TopicModelingAnalysis



- Topic 1: going, h1, want, say, like, cashback, just, don, money, help
- Topic 2: walking, dividend, h1, etf, investment, shipping, companies, yield, company, oil
- Topic 3: vaccine, covid, 19, vaccines, protein, really, trial, body, h1, messenger
- Topic 4: knee, h1, leg, toe, comfortable, tap, strength, good, work, time
- Topic 5: metabolism, day, h1, sacrifice, true, person, north, going, calories, training


---

# Lexical Diversity Analysis

This analysis measures the variety of words used in the text, indicating vocabulary richness.

- Unique Word Ratio: 0.2908
- Most Common Words: [('to', 319), ('the', 300), ('you', 223), ('and', 209), ('a', 174), ('of', 160), ('is', 123), ('that', 115), ('your', 111), ('in', 80), ('it', 66), ('for', 64), ('have', 59), ('with', 57), ('I', 53), ('on', 51), ('are', 45), ('if', 45), ('The', 44), ('as', 41)]


---

# DialogueStructureAnalysis



Average Transition Score: 0.1281


---

# N-gram Analysis

This analysis identifies common bigrams and trigrams to detect repetitive phrases in the text.

| ngram                   |   count |
|:------------------------|--------:|
| covid 19                |      11 |
| dream scenario          |       7 |
| little bit              |       7 |
| north star              |       6 |
| messenger rna           |       5 |
| dividend yield          |       5 |
| green tea               |       5 |
| product service         |       5 |
| person self             |       5 |
| person self talk        |       4 |
| self talk               |       4 |
| say hey                 |       4 |
| points cashback         |       4 |
| armour residential      |       4 |
| lose weight             |       4 |
| going say               |       4 |
| feel like               |       4 |
| true sacrifice          |       4 |
| let know                |       3 |
| small regular increases |       3 |


---

# Token Distribution Analysis

This analysis examines the distribution of tokens in the assistant's responses, offering insights into text complexity.

|   token_count |
|--------------:|
|         10    |
|        993.7  |
|        313.91 |
|        470    |
|        794.25 |
|       1001.5  |
|       1174.5  |
|       1526    |


---

# Text Length Analysis

This analysis provides statistics on the length of text responses from the assistant, helping to understand verbosity.

|   assistant_text_length |
|------------------------:|
|                   10    |
|                 4637.1  |
|                 1477.52 |
|                 2153    |
|                 3602    |
|                 4847    |
|                 5498    |
|                 6800    |


---

# PacingAnalysis



Number of Pacing Issues Detected: 19


---

# SpeechActAnalysis



Counter({'opinion': 9, 'persuasion': 9, 'information': 7})


---

# SentimentAnalysis



- negative: 2
- positive: 8


---

# NERAnalysis



[('CARDINAL', 58), ('DATE', 50), ('ORG', 43), ('PERSON', 25), ('ORDINAL', 24), ('MONEY', 22), ('PERCENT', 21), ('GPE', 11), ('LOC', 8), ('TIME', 7)]


---

# KeywordDensityAnalysis



- concept1: 0.0000
- concept2: 0.0000
- concept3: 0.0000


---

# ResponseRedundancyAnalysis



Average Redundancy Score: 0.3164


---

# ReadabilityOutlierAnalysis



Number of Readability Outliers: 1


---
