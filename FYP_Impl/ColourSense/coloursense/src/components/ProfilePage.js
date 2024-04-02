import React, { useRef, useState } from 'react';
import './ProfilePage.css'; // You can create a CSS file for styling
import { useNavigate } from 'react-router-dom';

const ProfilePage = () => {
  const navigate = useNavigate(); // Get the navigate function
  const inputFileRef = useRef(null); // Reference to the file input element
  const [profilePicture, setProfilePicture] = useState("/images/upload-icon.png");

  const handleColourAnalysis = async () => {
    try {
      const formData = new FormData();
    formData.append('image', profilePicture);
      const response = await fetch('http://localhost:8000/image', {
        method: 'POST'
      });

      if (response.ok) {
        const data = await response.json();
        const result = data.result;
        // navigate('/resultpage', { state: { analysisResult: result } });
        navigate('/resultpage', { state: { profilePicture , analysisResult: result } });
      } else {
        console.error('Failed to trigger color analysis');
      }
    } catch (error) {
      console.error('Error occurred while triggering color analysis:', error);
    }
  };

  const handleUploadPhoto = async () => {
    inputFileRef.current.click();
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        setProfilePicture(reader.result); // Set profile picture to uploaded image
        saveProfilePicture(file);
      };
      reader.readAsDataURL(file);
    }
  };

  const saveProfilePicture = async (file) => {
    try {
      const formData = new FormData();
      formData.append('image', file);

      const response = await fetch('http://localhost:8000/save-profile-picture', {
        method: 'POST',
        body: formData
      });

      if (response.ok) {
        console.log('Profile picture saved successfully');
      } else {
        console.error('Failed to save profile picture');
      }
    } catch (error) {
      console.error('Error occurred while saving profile picture:', error);
    }
  };


  return (
    <div className="profile-container">
      {/* Top Bar */}
      <div className="sidebar-container">
        <div className="top-bar">
          <div className="icons">
            <span>
              <img src="/images/profile-icon.png" alt="Logo" className="profile-logo" />
            </span>
          </div>
          <button onClick={handleColourAnalysis} className="create-button">Start Analysis</button>
        </div>

        {/* Left Sidebar */}
        <div className="left-sidebar">
          <h2 className="profile-header">ColourSense</h2>
          <div className="home-tab">
            <div className="home-icon">
              <img src="/images/home.png" alt="Logo" className="logo" />
              <span>Home</span>
            </div>
          </div>
          <ul className='sidebarList'>
            <li className='sidebarListItem' >Overview</li>
            <li className='sidebarListItem'>List</li>
            <li className='sidebarListItem'>Schedule</li>
            <li className='sidebarListItem'>Comment</li>
          </ul>
        </div>
      </div>

      {/* Main Content */}
      <div className="main-content">
        
          <h2 className="info-title">WHAT IS PERSONAL COLOUR ANALYSIS ?</h2>
          <p className='info'>Discover the magic of personal color analysis on our website! <br /> 
          By understanding your unique skin tone, hair color, and eye color, you can unlock a world of flattering clothing <br />  and makeup choices. 
          Our expert analysis categorizes individuals into four seasonal types: Spring, Summer, <br /> Autumn, and Winter. 
          Each season comes with its own curated color palette designed to accentuate your <br /> natural beauty. Springs radiate in vibrant, sunny hues like peach and aqua,  
          while Summers shine in soft,<br /> muted shades like lavender and slate blue. Autumns embrace rich, earthy tones such as olive green and<br /> mustard yellow, while 
          Winters dazzle in jewel tones like emerald green and ruby red. Explore our personalized<br /> color recommendations to elevate your style and feel confident in 
          every outfit. Discover the power of color and<br /> unleash your inner beauty today!</p>
          <h4 className="info-title-h4">GET STARTED</h4>
          <div className="profile-picture">
            {/* Display user's profile picture */}
            <img src={profilePicture} alt="Profile" />
            <input type="file" style={{ display: 'none' }} ref={inputFileRef} onChange={handleFileChange} />
            <button onClick={handleUploadPhoto} className="upload-button">Upload Photo</button>
       
          </div>
          
      </div>

    
    </div>
  );
};

export default ProfilePage;


