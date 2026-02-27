import React from 'react';
import '../LessonMultiplicatorApp/Style.css'

class Multiplicator extends React.Component {
    
    constructor(props){
        super(props);
        this.op1Ref=React.createRef() //CreateRef() creates a reference to the element.
        this.op2Ref=React.createRef()
        this.resultRef=React.createRef()
    }

    mySubmit=()=>{
        const num1 = this.op1Ref.current.value; //for input element, user input is stored in value.
        const num2 = this.op2Ref.current.value;
        const result = Number(num1) * Number(num2);
        this.resultRef.current.innerText = "result: " + result //innertext property of <p> is to display text.
    }

    render(){
        return(
            <form>
                <div className="container">
                    <h1> Multiply </h1>
                    <div className="form-group">
                        <label> Enter operand 1 </label>
                        <input type="number" ref={this.op1Ref}/>
                    </div>
                    <div className="form-group">
                        <label> Enter operand 2 </label>
                        <input type="number" ref={this.op2Ref}/>
                    </div>
                    <p ref={this.resultRef} className="result">  </p>
                    <button type="button" onClick={this.mySubmit}> Multiply </button>
                </div>
            </form>
        )
    }
}
export default Multiplicator;