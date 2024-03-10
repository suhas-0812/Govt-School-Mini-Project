import React, { useState } from 'react';
import axios from 'axios';

const AddStudent = () => {
    const [name, setName] = useState('');
    const [classValue, setClassValue] = useState('');
    const [message, setMessage] = useState('');

    const handleAddStudent = async (event) => {
        event.preventDefault();

        if (!Number.isInteger(Number(classValue))) {
            alert('Class should be an integer value.');
            return;
        }

        try {
            const response = await axios.post('http://127.0.0.1:5000/api/addstudents', {
                name: name,
                class: parseInt(classValue)
            });

            console.log(response.data); // Log the response from the Flask API

            setMessage('Student added successfully');
            // Reset input fields after adding the student
            setName('');
            setClassValue('');
        } catch (error) {
            console.error('Error adding student:', error);
            setMessage('Failed to add student');
        }
    };

    return (
        <div className="max-w-md mx-auto p-4 bg-white shadow-lg rounded-lg">
            <h1 className="text-2xl font-bold mb-4">Add New Student</h1>
            {message && <p className={message.includes('successfully') ? 'text-green-600' : 'text-red-600'}>{message}</p>}
            <form onSubmit={handleAddStudent}>
                <label htmlFor="name" className="block mb-2">Name:</label>
                <input type="text" id="name" value={name} onChange={(e) => setName(e.target.value)} required className="w-full p-2 mb-4 border rounded" />
                
                <label htmlFor="class" className="block mb-2">Class:</label>
                <input type="number" id="class" value={classValue} onChange={(e) => setClassValue(e.target.value)} required className="w-full p-2 mb-4 border rounded" />
                
                <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Add Student</button>
            </form>
        </div>
    );
};

export default AddStudent;
