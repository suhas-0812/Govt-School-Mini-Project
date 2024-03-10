import React, { useState } from 'react';
import axios from 'axios';

const DeleteStudent = () => {
    const [student, setQuestion] = useState('');

    const handleDeleteStudent = async (event) => {
        event.preventDefault();

        try {
            const response = await axios.post('http://localhost:5000/api/deletestudent', {
                student
            });

            console.log('Response:', response.data);
            alert('Student deleted successfully');

            // Reset form fields after adding the question
            setQuestion('');

        } catch (error) {
            console.error('Error deleting student:', error);
            alert('Failed to delete student');
        }
    };

    return (
        <div className="max-w-md mx-auto p-4 bg-white shadow-lg rounded-lg">
            <h1 className="text-2xl font-bold mb-4">Delete Student</h1>
            <form onSubmit={handleDeleteStudent}>
                <label htmlFor="student" className="block mb-2">Student ID:</label>
                <input type="text" id="student" value={student} onChange={(e) => setQuestion(e.target.value)} required className="w-full p-2 mb-4 border rounded" />
                <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Delete Student</button>
            </form>
        </div>
    );
};


export default DeleteStudent;