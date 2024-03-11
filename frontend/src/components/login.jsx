
import React, { useEffect, useState } from 'react';


const Login = () =>{
    const [email, setEmail] = useState("")
    const [userName, setuserName] = useState("")
    const [password, setPassword] = useState("")
    
    const handleUserNameChange = (event) => {
        setuserName(event.target.value)

    };
    const handlePasswordChange = (event) => {
        setPassword(event.target.value)
    };

    const submitLogin = (event) => {
        event.preventDefault();

        console.log("login in with:",  userName)
    };

    return(
        <div className='wrapper'>

            <h1>Login Page</h1>
            <form id = "loginForm" onSubmit={submitLogin}>
                <div className='input-box'> 
                <input 
                value={userName}
                onChange={handleUserNameChange}
                placeholder = "Enter user name"></input>
                </div>
                <div className='input-box'> 
                <input
                value ={password}
                onChange={handlePasswordChange}
                type = "password"
                placeholder = "Password"></input>
                </div>
            <button type ="submit">Submit</button>
            
            </form>
            
        </div>

    );
};
export default Login;