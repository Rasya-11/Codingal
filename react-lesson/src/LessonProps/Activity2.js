import Tree from "./Component/Tree";
import React from "react";

// Passing data as variable
const Tree_name= "Test Value 1"
const data2="Test Value 2"
class Lesson3A2 extends React.Component{
    render(){
        return<div>
            <h1> About Tree! </h1>
            <Tree value={Tree_name} 
            // name={data2}
            />
        </div>
    }
}
export default Lesson3A2;