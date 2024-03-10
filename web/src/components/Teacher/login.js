import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const TeacherLogin = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [loggedIn, setLoggedIn] = useState(false);
    const navigate = useNavigate();

    const handleLogin = (event) => {
        event.preventDefault();

        if (username === 'admin' && password === 'admin') {
            setLoggedIn(true);
        } else {
            alert('Invalid username or password. Please try again.');
        }
    };

    return (
        <div className="max-w-md mx-auto p-4 bg-white shadow-lg rounded-lg">
            <h1 className="text-2xl font-bold mb-4">Teacher Login</h1>
            {!loggedIn ? (
                <form onSubmit={handleLogin}>
                    <label htmlFor="username" className="block mb-2">Username:</label>
                    <input type="text" id="username" value={username} onChange={(e) => setUsername(e.target.value)} required className="w-full p-2 mb-4 border rounded" />
                    
                    <label htmlFor="password" className="block mb-2">Password:</label>
                    <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} required className="w-full p-2 mb-4 border rounded" />
                    
                    <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Login</button>
                </form>
            ) : (
                <div>
                    <h2 className="text-xl font-bold mb-4">Select an option:</h2>
                    <button onClick={() => navigate('/add-new-questions')} className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mr-4">Add New Questions</button>
                    <button onClick={() => navigate('/add-new-students')} className="bg-indigo-500 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded">Add New Students</button>
                    <button onClick={() => navigate('/delete-question')} className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mr-4">Delete Question</button>
                    <button onClick={() => navigate('/delete-student')} className="bg-indigo-500 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded">Delete Student</button>
                </div>
            )}
        </div>
    );
};

export default TeacherLogin;
