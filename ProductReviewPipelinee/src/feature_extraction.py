import pandas as pd
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer

def extract_keywords(texts, top_n=10):
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)
    word_counts = X.toarray().sum(axis=0)
    vocab = vectorizer.get_feature_names_out()
    word_freq = dict(zip(vocab, word_counts))
    common = Counter(word_freq).most_common(top_n)
    return common

def main():
    df = pd.read_csv("data/cleaned_reviews.csv")
    common_features = extract_keywords(df["cleaned_review"])
    print("🧠 Top keywords:")
    for word, freq in common_features:
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()
