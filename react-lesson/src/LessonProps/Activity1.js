import Tree from "./Component/Tree";
import React from "react";

class Tree1 extends React.Component{
    render(){
        return<div>
            <p> Trees are long-lived {this.props.value}, characterized by a single woody trunk, roots, 
        and branches, with over 60,000 to 80,000 species worldwide. They are essential for life, 
        producing oxygen, capturing carbon dioxide, providing habitats, and reducing noise. </p>
        </div>
    }
}

// In this activity, learn how to pass data for your props and how to use them while rendering HTML in components.
class Lesson3A1 extends React.Component{
    render(){
        return<div>
            <h1> About Tree! </h1>
            <Tree1 value={"perennial plants"}/>
        </div>
    }
}
export default Lesson3A1;