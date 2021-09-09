var spawn = require('child_process').spawn;

module.exports = async function(callback) {
    var process = spawn('python', [
        './usingModel.py',
        './python/img2.jpg'
    ]);
    await process.stdout.on('data', function(data) {
        return callback(data)
    });
}