# Customer Service Sentiment Analysis

This repository contains a simple script for analyzing customer feedback. The script performs the following steps:

1. Downloads required TextBlob corpora.
2. Computes sentence-level sentiment scores and classifications.
3. Extracts keywords from each feedback entry using KeyBERT.
4. Saves the resulting dataset with sentiments and keywords to `customer_feedback_with_keywords.csv`.

## Usage

Ensure `Customer_Feedback_Dataset.csv` is present in the repository directory, then run:

```bash
python analyze_feedback.py
```

The grouped keywords by sentiment will be printed to the console and the CSV file will be created.
