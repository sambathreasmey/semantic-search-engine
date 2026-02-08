import sqlite3
from faker import Faker
from tqdm import tqdm
import random

# Initialize Faker with your country's locale (e.g., 'en_US', 'ja_JP', 'th_TH')
fake = Faker('en_US') 

def create_dummy_db(num_records=5000000):
    conn = sqlite3.connect('lab/tourism.db')
    cursor = conn.cursor()

    # Create the professional structure
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tourism_place (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            location TEXT,
            description TEXT,
            category TEXT,
            is_indexed INTEGER DEFAULT 0
        )
    ''')

    categories = ['Nature', 'Heritage', 'Beach', 'Adventure', 'Food', 'City', 'Spiritual']
    
    print(f"Generating {num_records} dummy records...")
    
    # Batch processing is much faster for SQLite
    batch_size = 10000
    for i in tqdm(range(0, num_records, batch_size)):
        data = []
        for _ in range(batch_size):
            # Generate realistic dummy content
            title = f"{fake.city()} {random.choice(['Park', 'Shrine', 'Beach', 'Museum', 'Street', 'Mountain'])}"
            location = fake.state()
            # A longer description helps the AI find better semantic matches
            description = fake.paragraph(nb_sentences=3)
            category = random.choice(categories)
            
            data.append((title, location, description, category))
        
        cursor.executemany(
            "INSERT INTO tourism_place (title, location, description, category) VALUES (?, ?, ?, ?)", 
            data
        )
        conn.commit()

    conn.close()
    print("Database generation complete!")

if __name__ == "__main__":
    create_dummy_db(5000000)