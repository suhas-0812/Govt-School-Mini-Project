import React, { useState } from 'react';
import axios from 'axios';

const AddQuestion = () => {
    const [question, setQuestion] = useState('');
    const [options, setOptions] = useState({ A: '', B: '', C: '', D: '' });
    const [correctAnswer, setCorrectAnswer] = useState('A');
    const [subject, setSubject] = useState('');
    const [classValue, setClassValue] = useState('');

    const handleAddQuestion = async (event) => {
        event.preventDefault();

        try {
            const response = await axios.post('http://localhost:5000/api/addquestions', {
                question,
                options,
                correctAnswer,
                subject,
                classValue
            });

            console.log('Response:', response.data);
            alert('Question added successfully');

            // Reset form fields after adding the question
            setQuestion('');
            setOptions({ A: '', B: '', C: '', D: '' });
            setCorrectAnswer('A');
            setSubject('');
            setClassValue('');
        } catch (error) {
            console.error('Error adding question:', error);
            alert('Failed to add question');
        }
    };

    return (
        <div className="max-w-md mx-auto p-4 bg-white shadow-lg rounded-lg">
            <h1 className="text-2xl font-bold mb-4">Add New Question</h1>
            <form onSubmit={handleAddQuestion}>
                <label htmlFor="question" className="block mb-2">Question:</label>
                <input type="text" id="question" value={question} onChange={(e) => setQuestion(e.target.value)} required className="w-full p-2 mb-4 border rounded" />
                
                <label htmlFor="optionA" className="block mb-2">Option A:</label>
                <input type="text" id="optionA" value={options.A} onChange={(e) => setOptions({ ...options, A: e.target.value })} required className="w-full p-2 mb-4 border rounded" />
                
                <label htmlFor="optionB" className="block mb-2">Option B:</label>
                <input type="text" id="optionB" value={options.B} onChange={(e) => setOptions({ ...options, B: e.target.value })} required className="w-full p-2 mb-4 border rounded" />
                
                <label htmlFor="optionC" className="block mb-2">Option C:</label>
                <input type="text" id="optionC" value={options.C} onChange={(e) => setOptions({ ...options, C: e.target.value })} required className="w-full p-2 mb-4 border rounded" />
                
                <label htmlFor="optionD" className="block mb-2">Option D:</label>
                <input type="text" id="optionD" value={options.D} onChange={(e) => setOptions({ ...options, D: e.target.value })} required className="w-full p-2 mb-4 border rounded" />

                {/* Repeat for options B, C, D */}

                <label htmlFor="correctAnswer" className="block mb-2">Correct Answer:</label>
                <select id="correctAnswer" value={correctAnswer} onChange={(e) => setCorrectAnswer(e.target.value)} className="w-full p-2 mb-4 border rounded">
                    <option value="A">A</option>
                    <option value="B">B</option>
                    <option value="C">C</option>
                    <option value="D">D</option>
                </select>

                <label htmlFor="subject" className="block mb-2">Subject:</label>
                <select id="subject" value={subject} onChange={(e) => setSubject(e.target.value)} className="w-full p-2 mb-4 border rounded">
                    <option value="Science">Science</option>
                    <option value="Maths">Maths</option>
                    <option value="Social">Social</option>
                </select>

                <label htmlFor="classValue" className="block mb-2">Class:</label>
                <input type="number" id="classValue" value={classValue} onChange={(e) => setClassValue(e.target.value)} required className="w-full p-2 mb-4 border rounded" />

                <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Add Question</button>
            </form>
        </div>
    );
};




export default AddQuestion;
