
const http = require('http');

const sever = http.createServer((req, res) => {
    res.setHeader('content-type', 'text/html; charset=utf-8'); // 设置响应头，防止中文乱码
    res.end('hello nodejs http module');
})

sever.listen(9000, () => {
    console.log('服务已启动!');
})