const runPython = require('..//python/runpython')

function router(app) {

    app.get('/', async (req, res) => {
        runPython(show)

        function show(data) {
            // console.log(data.tostrin)
            console.log(data)
            res.send("ahihi" + data)

        }
        // res.send('s')
    })
}
module.exports = router;