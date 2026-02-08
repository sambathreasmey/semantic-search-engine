from search_engine import TourismSearch

# Initialize
engine = TourismSearch()
engine.load_engine()

# Search
query = "Islamic"
results = engine.search(query, top_k=3)

for i, res in enumerate(results, 1):
    print(f"{i}. {res['title']} ({res['location']})")
    print(f"   Description: {res['description'][:100]}...")
    print(f"   Similarity Score: {res['score']:.4f}\n")