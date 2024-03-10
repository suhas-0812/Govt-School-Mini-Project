import React, { useState, useEffect } from 'react';

const Quiz = () => {
    const [questions, setQuestions] = useState([]);
    const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
    const [selectedAnswer, setSelectedAnswer] = useState('');

    useEffect(() => {
        const fetchQuestions = async () => {
            try {
                const response = await fetch('http://127.0.0.1:5000/api/questions');
                const data = await response.json();
                setQuestions(data);
            } catch (error) {
                console.error('Error fetching questions:', error);
            }
        };

        fetchQuestions();
    }, []);

    const handleAnswerSelection = (answer) => {
        setSelectedAnswer(answer);
    };

    const validateAnswer = () => {
        // Add logic to send selected answer to backend for validation
    };

    if (questions.length === 0) {
        return <div className="text-center mt-8">Loading...</div>;
    }

    const currentQuestion = questions[currentQuestionIndex];

    return (
        <div className="max-w-md mx-auto p-4 bg-white shadow-lg rounded-lg">
            <h2 className="text-xl font-bold mb-4">{currentQuestion.question}</h2>
            <ul>
                {currentQuestion.answers.map((answer, index) => (
                    <li key={index} className="cursor-pointer py-2 hover:bg-gray-100" onClick={() => handleAnswerSelection(answer)}>
                        {answer}
                    </li>
                ))}
            </ul>
            <button className="mt-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onClick={validateAnswer}>Submit Answer</button>
        </div>
    );
};

export default Quiz;
