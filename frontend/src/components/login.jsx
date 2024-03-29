
import React, { useEffect, useState } from 'react';
import axios from 'axios';

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

        const url = ' http://localhost:8000/token';
        const userData = {
            username: userName,
            password : password
        }
        axios.post(url,userData ).then((response)=>{
            console.log(response.data.token);
        })
    
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