function validate(e){
    e.preventDefault()
    const email = document.getElementById("email").value.trim();
    const pass = document.getElementById("password").value.trim();
    const age = document.getElementById("age").value.trim();
    const mesg = document.getElementById("message");
    let message = "";
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/;
    
    if(email === ""){
        message = "Enter an email.";
        mesg.style.color = 'red';
    }
    else if(! emailPattern.test(email)){
        message = "Enter a vaild email"
        mesg.style.color = 'red';
    }
    else if(pass === ""){
        message = "Enter a password";
        mesg.style.color = 'red';
    }
    else if(pass.length < 6){
        message = "Password must be atleast six characters"
        mesg.style.color = 'red';
    }
    else if(age === ""){
        message = "Enter an age.";
        mesg.style.color = 'red';
    }
    else{
        message = "Login successful.";
        mesg.style.color = 'green';
    }
    mesg.innerText = message
}