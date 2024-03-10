import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home/home';
import Quiz from './components/Quiz/quiz';
import TeacherLogin from './components/Teacher/login';
import AddQuestion from './components/Teacher/addquestion';
import AddStudent from './components/Teacher/addstudent';
import DeleteQuestion from './components/Teacher/deletequestion';
import DeleteStudent from './components/Teacher/deletestudent';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/quiz" element={<Quiz />} />
                <Route path="/teacherlogin" element={<TeacherLogin />} />
                <Route path="/add-new-questions" element={<AddQuestion />} />
                <Route path="/add-new-students" element={<AddStudent />} />
                <Route path="/delete-student" element={<DeleteStudent />} />
                <Route path="/delete-question" element={<DeleteQuestion />} />

            </Routes>
        </Router>
    );
}

export default App;
