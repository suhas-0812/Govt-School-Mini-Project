import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Home = () => {
    const [rollNumber, setRollNumber] = useState('');
    const [selectedLevel, setSelectedLevel] = useState('1');
    const navigate = useNavigate();

    const startQuiz = () => {
        console.log("Roll Number:", rollNumber);
        console.log("Selected Level:", selectedLevel);
        // Redirect to another page with parameters if needed
        navigate('/quiz'); // Update 'your-other-page' with the actual path
    };

    const teacherlogin = () => {
        navigate('/teacherlogin'); // Update 'your-other-page' with the actual path
    };

    return (
        <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', backgroundColor: '#f3f4f6', padding: '1rem' }}>
            <h1 style={{ fontSize: '2rem', fontWeight: 'bold', textAlign: 'center', marginBottom: '1rem' }}>Welcome to the Quiz App!</h1>
            <div style={{ marginBottom: '1rem' }}>
                <label htmlFor="rollNumber" style={{ display: 'block' }}>Enter Roll Number:</label>
                <input type="text" id="rollNumber" placeholder="Enter your roll number" value={rollNumber} onChange={(e) => setRollNumber(e.target.value)} style={{ width: '100%', padding: '0.5rem', borderRadius: '0.25rem', border: '1px solid #ccc' }} />
            </div>
            <div style={{ marginBottom: '1rem' }}>
                <label htmlFor="levelSelect" style={{ display: 'block' }}>Select Level:</label>
                <select id="levelSelect" value={selectedLevel} onChange={(e) => setSelectedLevel(e.target.value)} style={{ width: '100%', padding: '0.5rem', borderRadius: '0.25rem', border: '1px solid #ccc' }}>
                    <option value="1">Level 1</option>
                    <option value="2">Level 2</option>
                    <option value="3">Level 3</option>
                    {/* Add more levels as needed */}
                </select>
            </div>
            <button onClick={startQuiz} style={{ backgroundColor: '#3498db', color: '#fff', fontWeight: 'bold', padding: '0.5rem 1rem', borderRadius: '0.25rem' }}>Start Quiz</button>
            <button onClick={teacherlogin} style={{ backgroundColor: '#3498db', color: '#fff', fontWeight: 'bold', padding: '0.5rem 1rem', borderRadius: '0.25rem' }}>Teacher Login</button>
        </div>
    );
};

export default Home;
