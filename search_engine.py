import faiss
import sqlite3
from sentence_transformers import SentenceTransformer

class TourismSearch:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.read_index("tourism.index")
        # Increase nprobe for better accuracy at 5M scale
        faiss.ParameterSpace().set_index_parameter(self.index, "nprobe", 10)

    def search(self, query, top_k=5):
        query_vector = self.model.encode([query]).astype('float32')
        distances, ids = self.index.search(query_vector, top_k)
        
        clean_ids = [int(i) for i in ids[0] if i != -1]
        if not clean_ids: return []

        conn = sqlite3.connect('tourism.db')
        cursor = conn.cursor()
        placeholders = ','.join(['?'] * len(clean_ids))
        # Order results to match FAISS ranking
        query_sql = f"SELECT id, title, location, description FROM tourism_place WHERE id IN ({placeholders})"
        cursor.execute(query_sql, clean_ids)
        db_results = {row[0]: row for row in cursor.fetchall()}
        conn.close()

        # Re-order based on clean_ids to maintain similarity ranking
        results = []
        for doc_id in clean_ids:
            if doc_id in db_results:
                row = db_results[doc_id]
                results.append({"id": row[0], "title": row[1], "location": row[2], "description": row[3]})
        return results