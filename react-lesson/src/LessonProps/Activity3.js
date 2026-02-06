import Tree from "./Component/Tree";
import React from "react";

class Tree1 extends React.Component{
    render(){
        return<div>
            <p> Trees are long-lived {this.props.detail.data1}, characterized by a single woody trunk, roots, 
        and branches, with over 60,000 to 80,000 species worldwide. They are essential for life, 
        producing oxygen, capturing carbon dioxide, providing habitats, and reducing noise. 
        My favourite tree is an {this.props.detail.Tree_name}. </p>
        </div>
    }
}

// Passing data as an object.
class Lesson3A3 extends React.Component{
    render(){
        const info = {data1:"perinneal trees", Tree_name:"Oak tree"}
        return<div>
            <h1> About Tree! </h1>
            <Tree1 detail={info}/>
        </div>
    }
}
export default Lesson3A3;