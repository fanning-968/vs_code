const express = require('express');
const app = express();

app.get('/123', (req, res) => {

    res.send('123');
})

app.get('/234', (req, res) => {

    res.send('234');
});

app.get('/:id', (req, res) => {

    let id = req.params.id;
    res.send(`您请求的ID是${id}`);
}   );

app.all('*splat', (req, res) => {

    res.send('404 Not Found');
});

app.listen(9000, () => {
    console.log('服务已启动!');
});