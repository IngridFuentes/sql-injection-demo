import sqlite3

# Create or connect to the database file
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create a 'users' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# sample user
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', 'admin123'))

# Save changes and close
conn.commit()
conn.close()

print("users.db is ready!")
