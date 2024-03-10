import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Quiz",
    user="postgres",
    password="Vidwan"
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE questions (
        question_id SERIAL PRIMARY KEY,
        level INTEGER,
        question_text VARCHAR(255) NOT NULL,
        option_1 VARCHAR(100),
        option_2 VARCHAR(100),
        option_3 VARCHAR(100),
        option_4 VARCHAR(100),
        correct_option INTEGER
    )
""")
conn.commit()
conn.commit()
conn.close()

