import React from "react";

class Lesson5Hw extends React.Component {
  render() {

    const headerStyle = {
      color: "white",
      padding: "10px",
      backgroundColor: "navy",
      textAlign: "center"
    };

    const sectionStyle = {
      border: "2px solid grey",
      padding: "10px",
      margin: "10px"
    };

    const textStyle = {
      color: "black"
    };

    return (
      <div>

        <h1 style={headerStyle}>My Resume</h1>

        <div style={sectionStyle}>
          <h2>Personal Details</h2>
          <p style={textStyle}>Name: Rasya Rao</p>
          <p style={textStyle}>Location: London</p>
          <p style={textStyle}>Email: Rasyarao@gmail.com</p>
        </div>

        <div style={sectionStyle}>
          <h2>Education</h2>
          <p style={textStyle}>BSc Computer Science</p>
          <p style={textStyle}>University of London</p>
        </div>

        <div style={sectionStyle}>
          <h2>Skills</h2>
          <p style={textStyle}>JavaScript</p>
          <p style={textStyle}>React</p>
          <p style={textStyle}>HTML & CSS</p>
        </div>

        <div style={sectionStyle}>
          <h2>Experience</h2>
          <p style={textStyle}>Web Developer Intern</p>
          <p style={textStyle}>ABC Tech Company</p>
        </div>

      </div>
    );
  }
}

export default Lesson5Hw;