import pandas as pd
from textblob import TextBlob

def get_sentiment(text):
    if not text:
        return "neutral"
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

def main():
    df = pd.read_csv("data/cleaned_reviews.csv")
    df["sentiment"] = df["cleaned_review"].apply(get_sentiment)
    df.to_csv("data/reviews_with_sentiment.csv", index=False)
    print("✅ Sentiment analysis complete. Saved to data/reviews_with_sentiment.csv")

if __name__ == "__main__":
    main()
