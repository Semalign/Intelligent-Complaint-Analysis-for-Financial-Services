import pandas as pd
import os

TARGET_PRODUCTS = {
    "Credit card",
    "Personal loan",
    "Buy Now, Pay Later (BNPL)",
    "Savings account",
    "Money transfers"
}

CHUNK_SIZE = 10000
INPUT_PATH = "data/raw/complaints.csv"
OUTPUT_PATH = "data/processed/filtered_complaints.csv"

def clean_text(text):
    if pd.isnull(text):
        return None
    text = text.lower()
    text = pd.Series(text).replace(r'[^a-zA-Z0-9\s]', '', regex=True).values[0]
    text = text.replace('i am writing to file a complaint', '')
    return text.strip()

def process_and_filter_chunks():
    filtered_rows = []
    chunk_iter = pd.read_csv(INPUT_PATH, chunksize=CHUNK_SIZE, usecols=[
        'product', 'issue', 'consumer_complaint_narrative', 'company', 'date_received'
    ])

    for i, chunk in enumerate(chunk_iter):
        chunk = chunk[chunk['product'].isin(TARGET_PRODUCTS)]
        chunk = chunk.dropna(subset=['consumer_complaint_narrative'])
        chunk['cleaned_narrative'] = chunk['consumer_complaint_narrative'].apply(clean_text)
        filtered_rows.append(chunk[['product', 'issue', 'cleaned_narrative', 'company', 'date_received']])

        print(f"[Chunk {i+1}] Processed {len(chunk)} rows")

    df_final = pd.concat(filtered_rows, ignore_index=True)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df_final.to_csv(OUTPUT_PATH, index=False)
    print(f"[✔] Final cleaned file saved to: {OUTPUT_PATH} — {len(df_final)} rows total")

if __name__ == "__main__":
    process_and_filter_chunks()
