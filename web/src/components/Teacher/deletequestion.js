import React, { useState } from 'react';
import axios from 'axios';

const DeleteQuestion = () => {
    const [question, setQuestion] = useState('');

    const handleDeleteQuestion = async (event) => {
        event.preventDefault();

        try {
            const response = await axios.post('http://localhost:5000/api/deletequestion', {
                question
            });

            console.log('Response:', response.data);
            alert('Question deleted successfully');

            // Reset form fields after adding the question
            setQuestion('');

        } catch (error) {
            console.error('Error adding question:', error);
            alert('Failed to delete question');
        }
    };

    return (
        <div className="max-w-md mx-auto p-4 bg-white shadow-lg rounded-lg">
            <h1 className="text-2xl font-bold mb-4">Delete Question</h1>
            <form onSubmit={handleDeleteQuestion}>
                <label htmlFor="question" className="block mb-2">Question ID:</label>
                <input type="text" id="question" value={question} onChange={(e) => setQuestion(e.target.value)} required className="w-full p-2 mb-4 border rounded" />
                
                <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Delete Question</button>
            </form>
        </div>
    );
};


export default DeleteQuestion;