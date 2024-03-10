from flask import Flask, jsonify, request
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Mock data representing quiz questions fetched from a PostgreSQL database
questions = [
    {
        "id": 1,
        "question": "What is the capital of France?",
        "answers": ["Paris", "London", "Berlin", "Madrid"],
        "correctAnswer": "Paris"
    },
    {
        "id": 2,
        "question": "Which planet is known as the Red Planet?",
        "answers": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correctAnswer": "Mars"
    }
]

students = []  # Initialize an empty list to store student data

@app.route('/api/questions', methods=['GET'])
def get_questions():
    return jsonify(questions)

@app.route('/api/addstudents', methods=['POST'])
def add_student():
    conn = psycopg2.connect(
        host="localhost",
        database="Quiz",
        user="postgres",
        password="Vidwan"
    )
    cur = conn.cursor()
    
    data = request.json
    name = data.get('name')
    class_value = data.get('class')

    if not isinstance(class_value, int):
        return jsonify({'error': 'Class should be an integer value.'}), 400

    try:
        cur.execute('''
            INSERT INTO Students (name, class) VALUES (%s, %s)
        ''', (name, class_value))
        
        conn.commit()
        conn.close()

        return jsonify({'message': 'Student added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/addquestions', methods=['POST'])
def add_question():
    data1 = request.json
    question = data1.get('question')
    answers = data1.get('options')
    options = [answers['A'],answers['B'],answers['C'],answers['D']]
    correct_answer = data1.get('correctAnswer')
    subject = data1.get('subject')
    classaddq = data1.get('classValue')
    if correct_answer=='A':
        correct_answer1 = answers["A"]
    elif correct_answer=='B':
        correct_answer1 = answers["B"]
    elif correct_answer=='C':
        correct_answer1 = answers["C"]
    else:
        correct_answer1 = answers["D"]

    conn = psycopg2.connect(
        host="localhost",
        database="Quiz",
        user="postgres",
        password="Vidwan"
    )
    cur = conn.cursor()
    try:
        cur.execute('''
            INSERT INTO questions (question,options,correctanswer,subject,class) VALUES (%s, %s,%s,%s,%s)
        ''', (question,options,correct_answer1,subject,classaddq ))
        
        conn.commit()
        conn.close()
        return jsonify({'message': 'Student added successfully'}), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/deletequestion', methods=['POST'])
def delete_question():
    data2 = request.json
    questionid = data2.get("question")
    conn = psycopg2.connect(
        host="localhost",
        database="Quiz",
        user="postgres",
        password="Vidwan"
    )
    cur = conn.cursor()
    try:
        cur.execute('''
            delete from questions where id = %s
        ''', (questionid ))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Question deleted successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/deletestudent', methods=['POST'])
def delete_student():
    data3 = request.json
    studentid = data3.get("student")
    conn = psycopg2.connect(
        host="localhost",
        database="Quiz",
        user="postgres",
        password="Vidwan"
    )
    cur = conn.cursor()
    try:
        cur.execute('''
            delete from students where id = %s
        ''', (studentid ))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Question deleted successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
