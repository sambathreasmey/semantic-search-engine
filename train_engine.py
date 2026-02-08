import sqlite3
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

def train():
    print("Starting 1 AM Training Job...")
    
    # 1. Connect to your database
    conn = sqlite3.connect('tourism.db') # Change to your DB connection
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, location, description FROM tourism_place")
    rows = cursor.fetchall()
    conn.close()

    # 2. Format data for AI and for Metadata
    metadata = []
    texts_to_encode = []
    
    for r in rows:
        place = {"id": r[0], "title": r[1], "location": r[2], "description": r[3]}
        metadata.append(place)
        # We combine title and description so the AI understands both
        texts_to_encode.append(f"{r[1]} in {r[2]}: {r[3]}")

    # 3. Create Vectors
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(texts_to_encode).astype('float32')

    # 4. Build FAISS Index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # 5. Save EVERYTHING (This ensures they stay in sync!)
    faiss.write_index(index, "tourism.index")
    with open("tourism_data.pkl", "wb") as f:
        pickle.dump(metadata, f)

    print(f"Training Complete. {len(metadata)} records indexed.")

if __name__ == "__main__":
    train()