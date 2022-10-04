const express = require("express")
const app = express()

const { exec, spawn } = require('child_process');


app.use(express.json())




app.post('/signup', async(req, res) => {
    
    const {username, password} = req.body
    res.end("logging into :" + username)
    
    const execCommand = "python3 facebooklogin.py "+username+ " "+password
    exec(execCommand, (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
    });

    
  })
  


app.listen(3000)

