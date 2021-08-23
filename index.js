var express = require('express');
var app = express();


app.get('/name', callName);
async function callName(req, res) {
    var spawn = require('child_process').spawn;
    var process = spawn('python', [
        './usingModel.py',
        './download.jfif'
    ]);
    await process.stdout.on('data', function(data) {
        console.log(data.toString());
        // console.log()
        res.send(data.toString());
    });
}

app.listen(3002, function() {
    console.log('server running on port http://localhost:3002');
})