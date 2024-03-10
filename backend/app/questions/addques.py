

import psycopg2
# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="Quiz",
    user="postgres",
    password="Vidwan"
)

cur = conn.cursor()

# Insert the new question into the database
cur.execute("""
    INSERT INTO questions (question_id, level, question_text, option_1, option_2, option_3, option_4, correct_option)
    VALUES (100, 1, '1+2', '3', '4', '5', '6', 1)
""")
conn.commit()
conn.close()