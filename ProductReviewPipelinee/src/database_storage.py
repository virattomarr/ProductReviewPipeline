import pandas as pd
import sqlite3

def main():
    df = pd.read_csv("data/reviews_with_sentiment.csv")

    conn = sqlite3.connect("data/reviews.db")
    df.to_sql("product_reviews", conn, if_exists="replace", index=False)

    cursor = conn.cursor()
    result = cursor.execute("SELECT sentiment, COUNT(*) FROM product_reviews GROUP BY sentiment").fetchall()
    print("📊 Sentiment counts:")
    for row in result:
        print(f"{row[0]}: {row[1]}")

    conn.close()
    print("✅ Data stored in SQLite at data/reviews.db")

if __name__ == "__main__":
    main()
