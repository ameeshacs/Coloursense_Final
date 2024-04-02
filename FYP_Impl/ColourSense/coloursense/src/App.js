
import React from 'react';
import {  Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import ProfilePage from './components/ProfilePage';
// import ExampleNew from './components/ExampleNew';
import ResultPage from './components/ResultPage';

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/profilepage" element={<ProfilePage />} />
      {/* <Route path="/examplenew" element={<ExampleNew />} /> */}
      <Route path="/resultpage" element={<ResultPage />} />
    </Routes>
  );
};

export default App;

