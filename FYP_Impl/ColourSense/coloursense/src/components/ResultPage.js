import React from 'react';
import './ResultPage.css'; // Your custom CSS file
import { Link, useLocation } from 'react-router-dom';

const ResultPage = () => {
  // Use the useLocation hook to access the location object
  const location = useLocation();
  // Retrieve analysis result passed as state
  const { profilePicture, analysisResult } = location.state || {};;

  // Mapping of analysis results to their corresponding seasons
  const seasons = {
    1: "Spring",
    2: "Summer",
    3: "Autumn",
    4: "Winter"
  };

  // Retrieve the corresponding season name based on the analysis result
  const seasonName = seasons[analysisResult];

  // Mapping of analysis results to their corresponding color palettes
  const analysisResultPalettes = {
    "Autumn": ["#ffcd00", "#b4a91f", "#b89d18", "#a09958", "#8f993e", "#5e7e29", "#7a7256", "#a07400", "#a6631b",
               "#946037", "#9d4815", "#7c4d3a", "#9a3324", "#5c462b", "#c4622d", "#ec5037", "#ef7200",
               "#f68d2e", "#d69a2d", "#6bcaba", "#00bfb3", "#009f4d", "#00778b", "#046a38", "#205c40"],
    "Spring": ["#fce300", "#fdd26e", "#ffcd00", "#ffb81c", "#f0b323", "#d4c304", "#c4d600", "#a9c23f", "#a8ad00",
                "#74aa50", "#6cc24a", "#009f4d", "#00a499", "#2dccd3", "#6dcdb8", "#9595d2", "#963cbd",
                "#da291c", "#b46a55", "#ec5037", "#a6631b", "#ff8200", "#ff8f1c", "#fdaa63", "#ffa38b"],
    "Summer": ["#f395c7", "#bcbdbe", "#c4a4a7", "#f57eb6", "#e277cd", "#c964cf", "#a277a6", "#808286", "#00a376",
                "#00b0b9", "#00a9e0", "#71c5e8", "#57728b", "#0077c8", "#7965b2", "#963cbd", "#93328e", 
                "#ac145a", "#bf0d3e", "#e31c79", "#ef60a3", "#007681", "#006f62", "#484a51", "#003057"],
    "Winter": ["#fefefe", "#99d6ea", "#f8e59a", "#f395c7", "#59cbe8", "#9bb8d3", "#00a3e1", "#808286", "#009775",
                "#00b0b9", "#0082ba", "#0086d6", "#0072ce", "#0057b8", "#004b87", "#484a51", "#84329b",
                "#963cbd", "#c724b1", "#da1884", "#e3006d", "#ce0037", "#aa0061", "#890c58", "#131413"],
    // Add more analysis results and their corresponding color palettes as needed
  };

  // Retrieve the relevant color palette based on the analysis result
  const colorPalette = analysisResultPalettes[seasonName];

  return (
    <div className="result-page">
      <div className="result-top-bar">
        <div className="home-logo-container">
          <Link to="/profilepage">
            <img src="/images/result-home.png" alt="Logo" className="home-logo" />
          </Link>
        </div>
        <div className="heading-container">
          <h1>Personal Color Analysis Result</h1>
        </div>
      </div>
      <div className="user-image">
        <img src={profilePicture} alt="User" />
      </div>
      <div className="analysis-result">
        <div className="analysis-result-container">
          <h2>Your Perfect Season</h2>
          <p>{seasonName}</p>
        </div>
      </div>
      <h3 className='palette-header'>Color Palette</h3>
      <div className="color-palette">
        <div className="colors">
          {colorPalette.map((color, index) => (
            <div
              key={index}
              className="color"
              style={{ backgroundColor: color }}
            ></div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default ResultPage;
