import faiss
import pickle
import os
from sentence_transformers import SentenceTransformer

class TourismSearch:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        # Load the AI model
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.metadata = []

    def load_engine(self, index_file="tourism.index", meta_file="tourism_data.pkl"):
        """Loads the saved index and the matching metadata."""
        if os.path.exists(index_file) and os.path.exists(meta_file):
            self.index = faiss.read_index(index_file)
            with open(meta_file, "rb") as f:
                self.metadata = pickle.load(f)
            print(f"Engine Loaded: {len(self.metadata)} places ready.")
        else:
            print("Error: Index files not found. Run the trainer script first!")

    def search(self, query, top_k=5):
        if self.index is None:
            return "Engine not loaded."

        # 1. Convert text query to vector
        query_vector = self.model.encode([query]).astype('float32')

        # 2. Search FAISS index
        # D = distances, I = indices
        distances, indices = self.index.search(query_vector, top_k)

        # 3. Map indices back to our data list (Preventing IndexError)
        results = []
        for i, idx in enumerate(indices[0]):
            if idx != -1 and idx < len(self.metadata):
                res = self.metadata[idx].copy()
                res['score'] = float(distances[0][i])
                results.append(res)
        
        return results