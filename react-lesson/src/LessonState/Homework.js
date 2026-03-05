import React from "react";
class ChocolateShop extends React.Component {

    constructor(){
        super();

        // State object
        this.state = {
            chocolate:{
                name: "Dark Chocolate",
                price: "£3",
                cocoa: "70%"
            }
        }
    }

    changeChocolate = () => {

        // condition check
        if(this.state.chocolate.name === "Dark Chocolate"){
            this.setState({
                chocolate:{
                    name: "White Chocolate",
                    price: "£2.50",
                    cocoa: "30%"
                }
            })
        }
    }

    render(){
        return(
            <div>

                <h1>Chocolate Shop</h1>

                <h2>{this.state.chocolate.name}</h2>
                <p>Price: {this.state.chocolate.price}</p>
                <p>Cocoa Content: {this.state.chocolate.cocoa}</p>

                <button onClick={this.changeChocolate}>
                    Show White Chocolate
                </button>

            </div>
        )
    }
}

export default ChocolateShop;