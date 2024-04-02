import React from 'react';
import './Login.css'; // Make sure to create a CSS file named "Login.css" for styling
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const navigate = useNavigate(); // Get the navigate function

  const handleLogin = () => {
    // try {
      // Make an API call to authenticate the user
    //   const response = await fetch('https://your-api-url/login', {
    //     method: 'POST',
    //     headers: {
    //       'Content-Type': 'application/json',
    //     },
    //     body: JSON.stringify({
    //       username: username,
    //       password: password,
    //     }),
    //   });
      
    //   // Check if the response is successful
    //   if (response.ok) {
    //     console.log('Login successful!');
    //     // Perform any additional actions after successful login, such as redirecting to another page
    //   } else {
    //     console.log('Incorrect username or password. Please try again.');
    //   }
    // } catch (error) {
    //   console.error('Error during login:', error);
    // }
    navigate('/profilepage');
  };
  

  return (
    <div className="login-container">
      <div className="left-section">
        <img
          src="/images/login.png"
          alt="ColourSense Logo"
          className="login-logo"
        />
        <h1 className="title">ColourSense - Personal <br />Colour Analysis</h1>
        <p className="tagline">Discover your perfect colours</p>
      </div>
      <div className="right-section">
        <div className="color-analysis">
          <h2 className="login-header">ColourSense</h2>
          <p className="login-subtext">Face Recognition
          <br />
          Technology</p>
        </div>
        <h1 className="title"> Unveiling Your Personal Color Symphony <br /> with ColourSense 
        </h1>
        <p className="tagline">Start your personal colour analysis process now!</p>
        <button onClick={handleLogin} className="login-button">
          Get Started
        </button>
        
      </div>
    </div>
  );
};

export default Login;
