import streamlit as st
import mysql.connector
import random
import time
import cv2
import mediapipe as mp
from datetime import datetime


class Question:
    def __init__(self,id,ques,options,ans):
        self.id=id
        self.ques=ques
        self.options=options
        self.ans=ans


# Connect to the database
connection = mysql.connector.connect(host='localhost', user='root', password="", database='quiz_app')
cursor = connection.cursor()

page = st.sidebar.radio("Navigation",['Take Test','Check Results', 'Add Questions'],index=0)

if page=='Take Test':

    st.title("Take quiz")

    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

    # Initialize MediaPipe Drawing Utility
    mp_drawing = mp.solutions.drawing_utils


    def fetch_questions():

        Level1_Questions=[]
        Level2_Questions=[]
        Level3_Questions=[]
        Level4_Questions=[]
        Level5_Questions=[]

        # Execute the query to select random 10 rows
        cursor.execute("SELECT * FROM level1 ORDER BY RAND() LIMIT 10")
        # Fetch the rows
        rows = cursor.fetchall()
        for row in rows:
            Level1_Questions.append(Question(row[0], row[1], {"A":row[2], "B":row[3], "C":row[4], "D":row[5]}, row[6]))
            
        cursor.execute("SELECT * FROM level2 ORDER BY RAND() LIMIT 8")
        rows = cursor.fetchall()
        for row in rows:
            Level2_Questions.append(Question(row[0], row[1], {"A":row[2], "B":row[3], "C":row[4], "D":row[5]}, row[6]))

        cursor.execute("SELECT * FROM level3 ORDER BY RAND() LIMIT 6")
        rows = cursor.fetchall()
        for row in rows:
            Level3_Questions.append(Question(row[0], row[1], {"A":row[2], "B":row[3], "C":row[4], "D":row[5]}, row[6]))

        cursor.execute("SELECT * FROM level4 ORDER BY RAND() LIMIT 4")
        rows = cursor.fetchall()
        for row in rows:
            Level4_Questions.append(Question(row[0], row[1], {"A":row[2], "B":row[3], "C":row[4], "D":row[5]}, row[6]))

        cursor.execute("SELECT * FROM level5 ORDER BY RAND() LIMIT 2")
        rows = cursor.fetchall()
        for row in rows:
            Level5_Questions.append(Question(row[0], row[1], {"A":row[2], "B":row[3], "C":row[4], "D":row[5]}, row[6]))

        return Level1_Questions, Level2_Questions, Level3_Questions, Level4_Questions, Level5_Questions


    def get():

        # Open the camera
        cap = cv2.VideoCapture(0)

        # Create a window in opencv
        cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)

        # Make the window stay on top
        cv2.setWindowProperty("Frame", cv2.WND_PROP_TOPMOST, 1)

        # Variables to track the quadrant and time
        last_quadrant = None
        start_time = None

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                continue

            # Flip the image horizontally for a later selfie-view display
            frame = cv2.flip(frame, 1)
            height, width, _ = frame.shape

            # Draw lines to divide the frame into 4 quadrants
            cv2.line(frame, (width//2, 0), (width//2, height), (255, 0, 0), 2)
            cv2.line(frame, (0, height//2), (width, height//2), (255, 0, 0), 2)

            # Add options to each quadrant
            cv2.putText(frame, "A", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(frame, "B", (width//2 + 50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(frame, "C", (50, height//2 + 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(frame, "D", (width//2 + 50, height//2 + 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

            # Convert the BGR image to RGB before processing
            results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            # Draw the hand annotations on the image
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    # Get the coordinates of the center of the hand
                    cx, cy = int(hand_landmarks.landmark[0].x * width), int(hand_landmarks.landmark[0].y * height)

                    # Determine the quadrant
                    quadrant = 'A' if cx < width//2 and cy < height//2 else \
                            'B' if cx > width//2 and cy < height//2 else \
                            'C' if cx < width//2 and cy > height//2 else 'D'

                    # Check if the hand is in the same quadrant
                    if quadrant == last_quadrant:
                        # If the hand has been in the quadrant for more than 3 seconds
                        if time.time() - start_time > 3:
                            selected_ans=quadrant
                            start_time = time.time()

                            # Close the camera and windows
                            cap.release()
                            cv2.destroyAllWindows()

                        
                    else:
                        # Update the last quadrant and start time
                        last_quadrant = quadrant
                        start_time = time.time()

                    # Display the quadrant on the frame
                    cv2.putText(frame, quadrant, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

            # Display the frame
            cv2.imshow('Frame', frame)

            # Break the loop on 'q' key press
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        # Close the camera and windows
        cap.release()
        cv2.destroyAllWindows()

        return quadrant



    def play():
        # Initialize counters for correct and incorrect answers
        correct_answers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        incorrect_answers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

        # Start with level 1
        level = 1

        # List of question sets for each level
        L1,L2,L3,L4,L5=fetch_questions()
        questions = [L1, L2, L3, L4, L5]

        # Counter for total questions asked
        total_questions = 0

        # Placeholder for the question and response
        placeholder = st.empty()
        response_placeholder = st.empty()

        # List to store question details
        question_details = []

        # While there are still questions left and total questions is less than 10
        while total_questions < 10:
            # If there are no questions left at the current level, move to the next level
            if not questions[level - 1]:
                level += 1
                continue

            # Get a random question at the current level
            question_index = random.randint(0, len(questions[level - 1]) - 1)
            current_question = questions[level - 1].pop(question_index)

            # Concatenate question and options into a single string
            content = str(total_questions + 1) + ". " + current_question.ques
            for key, value in current_question.options.items():
                content += "\n{}: {}\n".format(key, value)

            # Write the content to the placeholder
            placeholder.subheader(content)
            time.sleep(3)

            # Get the student's answer (this part depends on your implementation)
            sel = get()

            response = "Option {} selected. ".format(sel)

            # Check if the student's answer is correct
            if sel == current_question.ans:
                # If the answer is correct, increment the counter for correct answers
                correct_answers[level] += 1
                response += "Correct Answer"
            else:
                # If the answer is incorrect, increment the counter for incorrect answers
                incorrect_answers[level] += 1
                response += "Wrong Answer"

            # Store the question details
            question_details.append((current_question.id, level, sel == current_question.ans))

            # If the student has answered two questions correctly at this level, move up to the next level
            if correct_answers[level] == 2 and level < 5:
                level += 1
            # If the student has answered two questions incorrectly at this level, move down to the previous level
            elif incorrect_answers[level] == 2 and level > 1:
                level -= 1

            # Show the response
            response_placeholder.write(response)
            time.sleep(1.5)

            # Clear the placeholders
            placeholder.empty()
            response_placeholder.empty()
            time.sleep(1)

            # Increment the total questions counter
            total_questions += 1


        # Show the final score (this part depends on your implementation)
        st.subheader("Your score is {}/10".format(sum(correct_answers.values())))

        # Prepare the data for insertion
        data = [roll_no] + [str(detail) for detail in question_details] + [sum(1 for detail in question_details if detail[2])]

        # Prepare the SQL command
        sql = """
        INSERT INTO student_answers (roll_no, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, total_marks, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Execute the SQL command
        cursor.execute(sql, data + [time.strftime('%Y-%m-%d %H:%M:%S')])

        # Commit the changes
        connection.commit()

        # Add a restart button
        if st.button("Play again"):
            # Clear everything
            st.experimental_rerun()
    
    # Create a placeholder for the name input field
    roll_no_placeholder = st.empty()

    # Create a placeholder for the play button
    button_placeholder = st.empty()

    # Get the user's name
    roll_no = roll_no_placeholder.text_input("Enter your Roll no:")

    # Display the play button
    play_button = button_placeholder.button("Play")

    # If the play button is clicked and a name is entered, start the game
    if play_button and roll_no:
        # Clear the name input field and the play button
        roll_no_placeholder.empty()
        button_placeholder.empty()

        # Call the play function
        play()


if page=='Add Questions':
    # Start the streamlit app
    st.title('Add New Questions')

    # Create a form
    with st.form(key='add_question_form'):
        # Select box for level
        levels = ['Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5']
        level = st.selectbox('Select Level', levels)

        # Text input for question
        question = st.text_input('Enter the question')

        # Text inputs for options
        options = {
            'A': st.text_input('Enter option A'),
            'B': st.text_input('Enter option B'),
            'C': st.text_input('Enter option C'),
            'D': st.text_input('Enter option D'),
        }

        # Select box for correct answer
        correct_answer = st.selectbox('Select the correct answer', list(options.keys()))

        # Submit button
        submit_button = st.form_submit_button(label='Add Question')

        # If the form is submitted, insert the new question into the database
        if submit_button:
            try:
                cursor.execute("""
                    INSERT INTO {} (question, optionA, optionB, optionC, optionD, answer)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """.format(level.lower().replace(' ', '')), (question, options['A'], options['B'], options['C'], options['D'], correct_answer))

                # Commit the changes
                connection.commit()

                st.success("Question inserted successfully!")

            except mysql.connector.Error as err:
                st.error(f"Error: {err}")


if page=='Check Results':
    # Create a form
    with st.form(key='check_results_form'):
        # Text input for roll number
        roll_no = st.text_input('Enter the roll number')

        # Date input for date
        date = st.date_input('Enter the date')

        # Submit button
        submit_button = st.form_submit_button(label='Check Results')

        # If the form is submitted, fetch the student's results
        if submit_button:
            # Prepare the SQL command
            sql = """
            SELECT * FROM student_answers
            WHERE roll_no = %s AND DATE(timestamp) = %s
            """

            # Execute the SQL command
            cursor.execute(sql, (roll_no, date))

            # Fetch the result
            result = cursor.fetchone()

            # If a result was found, display it
            if result:
                st.write(f"Roll Number: {result[0]}")
                st.write(f"Total Score: {result[11]}/10")
                for i in range(1, 11):
                    question_id, level, correct = eval(result[i])
                    st.write(f"Question {i}: {'Correct' if correct else 'Incorrect'} (Level {level})")
            else:
                st.write("No results found for this roll number and date.")


if cursor is not None:
    cursor.close()
if connection.is_connected():
    connection.close()
