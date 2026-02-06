import Tree from "./Component/Tree";
import React from "react";

class User extends React.Component{
    constructor(props){
        super(props);
        this.info={location:"London"}
    }
    render(){
        return<div>
            <p> I am from {this.props.city}, {this.info.location} </p>
        </div>
    }
}

// In this activity, learn how to pass data for your props and how to use them while rendering HTML in components.
class Lesson3A4 extends React.Component{
    render(){
        return<div>
            <h1> Hello </h1>
            <User city={"Newham"}/>
        </div>
    }
}
export default Lesson3A4;