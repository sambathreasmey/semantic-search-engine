import sqlite3
import json

# Sample data list (expanded to 100 items)
data = [
  {
    "id": 1,
    "title": "Grand Canyon National Park",
    "category": "Nature",
    "location": "Arizona, USA",
    "description": "Massive canyon known for its layered bands of red rock, revealing millions of years of geological history. Perfect for hiking and photography."
  },
  {
    "id": 2,
    "title": "Santorini Caldera",
    "category": "Beach",
    "location": "Greece",
    "description": "Iconic volcanic islands with white-washed buildings, blue domes, and stunning sunset views over the Aegean Sea. Famous for luxury stays and beaches."
  },
  {
    "id": 3,
    "title": "Kyoto Fushimi Inari Shrine",
    "category": "Heritage",
    "location": "Kyoto, Japan",
    "description": "Famous for its thousands of vermilion torii gates, which straddle a network of trails behind its main buildings. A spiritual and historic landmark."
  },
  {
    "id": 4,
    "title": "Machu Picchu",
    "category": "Adventure",
    "location": "Cusco Region, Peru",
    "description": "An Incan citadel set high in the Andes Mountains. Known for its sophisticated dry-stone walls and panoramic views. Requires trekking via the Inca Trail."
  },
  {
    "id": 5,
    "title": "The Great Barrier Reef",
    "category": "Nature",
    "location": "Queensland, Australia",
    "description": "The world's largest coral reef system. Home to thousands of species of tropical fish, turtles, and sharks. Popular for snorkeling and scuba diving."
  },
  {
    "id": 6,
    "title": "Petra Ancient City",
    "category": "Heritage",
    "location": "Jordan",
    "description": "Archaeological site containing tombs and temples carved into pink sandstone cliffs. Often called the 'Rose City' because of the color of the stone."
  },
  {
    "id": 7,
    "title": "Geirangerfjord",
    "category": "Nature",
    "location": "Norway",
    "description": "A deep blue UNESCO-protected fjord surrounded by majestic, snow-covered mountain peaks and wild waterfalls."
  },
  {
    "id": 8,
    "title": "Serengeti National Park",
    "category": "Nature",
    "location": "Tanzania",
    "description": "Famous for its annual migration of over 1.5 million wildebeest; the ultimate destination for wildlife safaris."
  },
  {
    "id": 9,
    "title": "Mont Saint-Michel",
    "category": "Heritage",
    "location": "Normandy, France",
    "description": "A stunning medieval abbey perched atop a rocky tidal island that becomes isolated from the mainland at high tide."
  },
  {
    "id": 10,
    "title": "Banff National Park",
    "category": "Adventure",
    "location": "Alberta, Canada",
    "description": "Located in the heart of the Rockies, known for its turquoise glacial lakes and endless alpine hiking trails."
  },
  {
    "id": 11,
    "title": "Gardens by the Bay",
    "category": "Cityscape",
    "location": "Singapore",
    "description": "A futuristic park featuring the iconic Supertrees and high-tech glass greenhouses, blending nature with urban design."
  },
  {
    "id": 12,
    "title": "Bora Bora",
    "category": "Beach",
    "location": "French Polynesia",
    "description": "Known for its turquoise lagoons and overwater bungalows, making it a premier destination for luxury and relaxation."
  },
  {
    "id": 13,
    "title": "Alhambra Palace",
    "category": "Heritage",
    "location": "Granada, Spain",
    "description": "A sprawling fortress complex showcasing stunning Islamic architecture and meticulously manicured gardens."
  },
  {
    "id": 14,
    "title": "Salar de Uyuni",
    "category": "Nature",
    "location": "Bolivia",
    "description": "The world's largest salt flat, which transforms into a giant mirror during the rainy season, reflecting the sky."
  },
  {
    "id": 15,
    "title": "Angkor Wat",
    "category": "Heritage",
    "location": "Siem Reap, Cambodia",
    "description": "The largest religious monument in the world, originally built as a Hindu temple and later transformed into a Buddhist site."
  },
  {
    "id": 16,
    "title": "The Dolomites",
    "category": "Adventure",
    "location": "Northern Italy",
    "description": "A mountain range famous for its dramatic vertical walls and jagged peaks; a haven for skiing and climbing."
  }
]

def setup_db():
    conn = sqlite3.connect('tourism.db')
    curr = conn.cursor()
    
    # Create Table
    curr.execute('''
        CREATE TABLE IF NOT EXISTS tourism_place (
            id INTEGER PRIMARY KEY,
            title TEXT,
            category TEXT,
            location TEXT,
            description TEXT
        )
    ''')
    
    # Batch Insert
    curr.executemany('''
        INSERT INTO tourism_place (title, category, location, description) 
        VALUES (?, ?, ?, ?)
    ''', [(item['title'], item['category'], item['location'], item['description']) for item in data])
    
    conn.commit()
    conn.close()

setup_db()