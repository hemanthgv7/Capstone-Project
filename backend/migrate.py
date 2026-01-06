import psycopg2
import os

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS deploy_log (
    id SERIAL PRIMARY KEY,
    deployed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
cursor.close()
conn.close()

print("Database migration completed")
