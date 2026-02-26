import React from "react";

// class Activity1Lesson5 extends React.Component {
//   render() {
//     return (
//       <div>
//         <h1 style={{ color: "blue" }}> Hi </h1>
//         <p style={{border: "2px solid red", color: "red"}}> My name is Rasya. </p>
//       </div>
//     );
//   }
// }

class Activity1Lesson5 extends React.Component {
  render() {
    
    const headerStyle= {color: "blue", padding: "8px", backgroundColor: "purple"}
    const pStyle={border: "10px solid green", color: "pink"}

    return (
      <div>
        <h1 style={headerStyle}> Hi </h1>
        <p style={pStyle}> My name is Rasya. </p>
      </div>
    );
  }
}
export default Activity1Lesson5;
