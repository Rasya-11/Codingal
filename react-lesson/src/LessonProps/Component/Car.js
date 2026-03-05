import React from "react";

class Car extends React.Component{
    render(){
        return(
            <div>
                <p>
                    My favourite car is the {this.props.brand}. It is {this.props.color} in colour
                    and has a top speed of {this.props.speed}.
                </p>
            </div>
        );
    }
}

export default Car;