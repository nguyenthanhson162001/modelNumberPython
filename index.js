var express = require('express');
var app = express();
const py = require('./python/runpython')
const router = require('./router/index')

router(app)
app.listen(3002, function () {
    console.log('server running on port http://localhost:3002');
})