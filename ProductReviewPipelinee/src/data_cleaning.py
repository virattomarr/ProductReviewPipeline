import pandas as pd
import re

def clean_text(text):
    if pd.isna(text):
        return ""
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def main():
    df = pd.read_csv("data/sample_reviews.csv")
    df.drop_duplicates(subset="review_text", inplace=True)
    df["cleaned_review"] = df["review_text"].apply(clean_text)
    df.to_csv("data/cleaned_reviews.csv", index=False)
    print("✅ Data cleaning complete. Saved to data/cleaned_reviews.csv")

if __name__ == "__main__":
    main()
