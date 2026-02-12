import React from 'react';
class Lesson4A2 extends React.Component{
    
    constructor(props){
        super(props)
        this.state={
            name:"Rasya",
            grade:"9",
            age:"14",
            colour:"blue",
        }
    }

    favColour=()=>{
        this.setState({colour:"pink"})
    }
    
    render(){
        return(
            <div>
                <h1> Student Details </h1>
                <p> My name is {this.state.name}. </p>
                <p> I'm in grade {this.state.grade}. </p>
                <p> I am {this.state.name} years old. </p>
                <p> My favourite colour is {this.state.colour}. </p>
                <button type="button" onClick={this.favColour}> Click here. </button>
            </div>
        )
    }
}
export default Lesson4A2;