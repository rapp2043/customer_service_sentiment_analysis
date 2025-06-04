# Customer Sentiment Analysis from Synthetic Feedback

This repository showcases a passion project exploring how natural language processing (NLP) can be used to extract, classify, and evaluate customer sentiment from open-text feedback. It was inspired by real-world applications observed in a workplace setting, reimagined here in a consumer-facing context to explore how such tools can be developed and applied independently.

---

## 🔍 Project Overview

The project performs end-to-end sentiment analysis on a synthetic customer feedback dataset of **300 entries**, which was **entirely generated using the Python Faker library**. Each entry mimics realistic consumer feedback and includes:

- An order number  
- Open-text feedback  
- A Likert-style satisfaction score (1–10)  

The pipeline performs sentence-level and overall sentiment scoring, assigns sentiment labels, extracts keywords, categorizes the feedback, and flags mismatches between textual sentiment and numerical score.

---

## ✨ Why This Matters

Understanding customer sentiment at scale is essential for businesses looking to improve customer experience, identify pain points, and enhance brand reputation. This project demonstrates how NLP tools like **TextBlob** and **KeyBERT** can:

- Automate sentiment scoring and classification  
- Extract actionable keywords from unstructured text  
- Group feedback into meaningful categories (e.g., Billing, Support, Delivery)  
- Detect inconsistencies between perceived experience (text) and reported satisfaction (score)  

This approach could be adapted for call center analytics, survey response triage, app store reviews, product feedback monitoring, and more.

---

## 📁 Dataset Columns

| Column Name                | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `order_number`             | Unique ID for each order                                                    |
| `feedback`                 | Synthetic customer review (1–4 sentences)                                   |
| `score`                    | Likert rating (1–10) representing customer satisfaction                     |
| `sentence_sentiments`      | List of sentiment polarity scores per sentence                              |
| `sentiment_classifications`| List of sentiment labels (Positive, Neutral, Negative) per sentence         |
| `keywords`                 | Extracted keywords using KeyBERT                                            |
| `categorized_feedback`     | Assigned feedback category based on keywords                                |
| `overall_sentiment`        | Combined sentiment polarity for entire feedback text                        |
| `sentiment_classification` | Overall sentiment label from combined polarity                              |
| `mismatch`                 | Boolean flag if overall sentiment contradicts Likert score                  |

---

## 🛠 Tools & Libraries Used

- 🐍 Python 3.9+  
- 📝 [TextBlob](https://textblob.readthedocs.io/en/dev/) — for sentiment analysis  
- 🧠 [KeyBERT](https://github.com/MaartenGr/KeyBERT) — for keyword extraction  
- 🧪 [Faker](https://faker.readthedocs.io/en/master/) — to generate synthetic customer feedback  
- 📊 pandas — for data manipulation and CSV handling  

---

## 🧪 How to Run It

1. **Install required libraries**  
   ```bash
   pip install textblob keybert pandas
   python -m textblob.download_corpora

2. **Run the pipeline scripts in sequence**
   Or consolidate them into one for end-to-end processing.

3. **Inspect the output file**
   ```bash
   5_customer_feedback_with_sentiment_and_mismatch.csv

## 🔮 Potential Use Cases

- Customer support triage: Route issues by category and urgency
- Quality assurance: Detect sentiment-score mismatches to flag underreported dissatisfaction
- Product development: Identify keyword clusters tied to low or high satisfaction
- Reputation monitoring: Track feedback trends over time

## ⚠️ Disclaimer
This dataset is synthetic and was developed solely for experimentation and demonstration purposes. No real customer data was used.

## 💡 Future Work
- Integrate Named Entity Recognition (NER) to tag brands, products, or locations
- Develop a dashboard in Tableau or Streamlit for visual insights
- Connect to live feedback sources (e.g., reviews API or form responses)

## 📬 Author Note
This project stemmed from a desire to independently replicate a sentiment analysis pipeline seen in a professional setting, but tailored for a consumer-focused use case. It’s both a learning exercise and a potential foundation for more advanced NLP-driven analytics.

## 📝 License
This project is licensed under the MIT License.
