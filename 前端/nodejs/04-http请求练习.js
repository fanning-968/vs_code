const http = require('http');
const { app } = require('./01_npm/01_express');

const sever = http.createServer((req, res) => {

    let method = req.method;
    let { pathname } = new URL(req.url, 'http://127.0.0.1');
    res.setHeader('Content-Type', 'text/html; charset=utf-8');
    if (method === 'GET' && pathname === '/login') {
        res.end('这是登录页面');
    } else if (method === 'GET' && pathname === '/reg') {
        res.end('这是注册页面');
    } else {
        res.end('Not Found');
    }
})

sever.listen(9000, () => {
    console.log('服务已启动!');
});
app.get('/request', (req, res) => {
    console.log(req.method);
    console.log(req.url);
    console.log(req.headers);
    console.log(req.httpVersion);
    console.log(req.params);
    res.send('这是登录页面');
});
