import React from "react";
class Tree extends React.Component{
    render(){
        return<div>
            <p> Trees are long-lived {this.props.value}, characterized by a single woody trunk, roots, 
        and branches, with over 60,000 to 80,000 species worldwide. They are essential for life, 
        producing oxygen, capturing carbon dioxide, providing habitats, and reducing noise. </p>
        </div>
    }
}
export default Tree;