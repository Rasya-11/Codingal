import React from "react";
import Car from "./Component/Car";

class Lesson3Hw extends React.Component{
    render(){
        return(
            <div>
                <h1>Car Information</h1>

                <Car brand="BMW" color="black" speed="250 km/h"/>

            </div>
        );
    }
}

export default Lesson3Hw;