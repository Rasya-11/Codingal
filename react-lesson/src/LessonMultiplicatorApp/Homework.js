import React from "react";

class LoginForm extends React.Component {

    constructor(props){
        super(props)

        this.nameRef = React.createRef()
        this.ageRef = React.createRef()
        this.resultRef = React.createRef()
    }

    mySubmit = () => {

        const name = this.nameRef.current.value
        const age = this.ageRef.current.value

        if(age > 17){
            this.resultRef.current.innerText = "Welcome " + name + "! Login successful."
        }
        else{
            this.resultRef.current.innerText = "Access denied. You must be above 17 to use this form."
        }
    }

    render(){
        return(
            <form>
                <div className="container">

                    <h1>Login Form</h1>

                    <div className="form-group">
                        <label>Enter Name</label>
                        <input type="text" ref={this.nameRef}/>
                    </div>

                    <div className="form-group">
                        <label>Enter Age</label>
                        <input type="number" ref={this.ageRef}/>
                    </div>

                    <p ref={this.resultRef}></p>

                    <button type="button" onClick={this.mySubmit}>
                        Login
                    </button>

                </div>
            </form>
        )
    }
}

export default LoginForm;