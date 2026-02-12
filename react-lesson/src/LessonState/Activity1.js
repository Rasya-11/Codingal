// class Lesson4A1 extends React.Component{
//     render(){
//         return(

//         )
//     }
// }
// export default Lesson4A1;

import React from 'react';
class Lesson4A1 extends React.Component{
// state object
    constructor(props){
        // props are values passed from a parent component.
        // The super(props) calls the constructor, passes props to the parent and make this.props available inside the constructor
        super(props)
        this.state={
            name:"Rasya",
            grade:"9",
            age:"14",
        }
    }

    render(){
        return(
            <div>
                <h1> Student Details </h1>
                <p> My name is {this.state.name}. </p>
                <p> I'm in grade {this.state.grade}. </p>
                <p> I am {this.state.age} years old. </p>
            </div>
        )
    }
}
export default Lesson4A1;