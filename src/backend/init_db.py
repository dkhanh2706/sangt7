import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')
print(f"Database path: {DB_PATH}")

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Create users table
c.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT DEFAULT 'user',
    createdAt TEXT NOT NULL
)''')

# Create history table
c.execute('''CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userId INTEGER NOT NULL,
    subject TEXT NOT NULL,
    score INTEGER NOT NULL,
    total INTEGER NOT NULL,
    answers TEXT,
    createdAt TEXT NOT NULL
)''')

conn.commit()

# Check tables
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = c.fetchall()
print(f"Tables created: {tables}")

# Insert a test user
c.execute("INSERT INTO users (fullname, email, password, role, createdAt) VALUES (?, ?, ?, ?, ?)",
          ('Admin Test', 'admin@test.com', '123456', 'admin', '2024-01-01'))
conn.commit()

# Show data
c.execute("SELECT * FROM users")
print("Users:", c.fetchall())

conn.close()
print("Database initialized successfully!")