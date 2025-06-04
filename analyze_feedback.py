import pandas as pd
from textblob import TextBlob
from keybert import KeyBERT

import textblob.download_corpora

def get_sentence_sentiments(text):
    """Return sentiment scores and classifications for each sentence."""
    blob = TextBlob(text)
    scores = [sentence.sentiment.polarity for sentence in blob.sentences]
    labels = [
        "Positive" if s > 0 else "Negative" if s < 0 else "Neutral"
        for s in scores
    ]
    return scores, labels

def extract_keywords(text, model):
    """Extract keywords using KeyBERT and return a list of terms."""
    keywords = model.extract_keywords(
        text, keyphrase_ngram_range=(1, 2), stop_words="english"
    )
    return [kw[0] for kw in keywords]

def main():
    # Download TextBlob corpora
    textblob.download_corpora.download_all()

    # Load feedback data
    df = pd.read_csv("Customer_Feedback_Dataset.csv")

    # Analyze sentiment sentence by sentence
    df[["sentence_sentiments", "sentiment_classifications"]] = df["feedback"].apply(
        lambda text: pd.Series(get_sentence_sentiments(text))
    )

    # Keyword extraction
    kw_model = KeyBERT()
    df["keywords"] = df["feedback"].apply(lambda text: extract_keywords(text, kw_model))

    # Group keywords by sentiment classification
    grouped = df.groupby("sentiment_classifications")["keywords"].sum()

    # Save results
    df.to_csv("customer_feedback_with_keywords.csv", index=False)

    # Display grouped keywords
    print(grouped)

if __name__ == "__main__":
    main()
