import psycopg2
# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="Quiz",
    user="postgres",
    password="Vidwan"
)

cur = conn.cursor()

level = 1  # You can change this to the desired level

# Select a random question from the 'questions' table based on the specified level
cur.execute("SELECT * FROM questions WHERE level = %s ORDER BY RANDOM() LIMIT 1", (level,))
random_question = cur.fetchone()

# Display the fetched questions
print(random_question)

conn.commit()
conn.close()