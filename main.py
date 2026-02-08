import time
from search_engine import TourismSearch

search_engine = TourismSearch()

# 2. Perform a search
# The model converts your text into a vector and finds matches in the index
queries = [
    "Best beaches for surfing in Southeast Asia",
    "Top surfing beaches in Southeast Asia",
    "Best surf spots in Southeast Asia",
    "Beginner-friendly surfing beaches in Southeast Asia",
    "Best surfing destinations in Southeast Asia",
    "Southeast Asia surfing beaches for beginners",
    "Advanced surfing spots in Southeast Asia",
    "Cheap surfing beaches in Southeast Asia",
    "Best countries for surfing in Southeast Asia",
    "Surfing hotspots in Southeast Asia",
    "Best waves for surfing in Southeast Asia",
    "Hidden surfing beaches in Southeast Asia",
    "Best surfing beaches in Indonesia and Southeast Asia",
    "Best surfing beaches in Thailand and Southeast Asia",
    "Surf travel guide Southeast Asia beaches",
    "Best surfing beaches in Southeast Asia year-round",
    "Best surf beaches in Southeast Asia for solo travelers",
    "Best family-friendly surfing beaches in Southeast Asia",
    "Surfing beaches in Southeast Asia with resorts",
    "Surf camps near best beaches in Southeast Asia",
    "Best surfing beaches in Southeast Asia for beginners and pros",
    "Surfing beaches in Southeast Asia with consistent waves",
    "Best surfing beaches in Southeast Asia during monsoon season",
    "Southeast Asia beach destinations for surfing holidays",
    "Top-rated surfing beaches in Southeast Asia"
  ]
for query in queries:
    start_time = time.time()
    results = search_engine.search(query, top_k=10)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("________________________________________________")
    print("Query : ", query)
    print("Duration : ", round(elapsed_time, 3), "seconds")
    print("________________________________________________")

    # 3. Display the results
    if not results:
        print("No matches found.")
    else:
        print(f"Found {len(results)} results:")
        for i, item in enumerate(results, 1):
            print(f"\n[{i}] {item['title']} - {item['location']}")
            print(f"Description: {item['description'][:150]}...")
    time.sleep(1)