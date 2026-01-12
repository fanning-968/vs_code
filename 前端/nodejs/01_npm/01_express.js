
const express = require('express');
const app = express();

app.get('/request', (req, res) => {
    console.log(req.method);
    console.log(req.url);
    console.log(req.headers);
    console.log(req.httpVersion);

    console.log(req.path);
    console.log(req.query);
    
    
    res.send('这是请求页面');
});
app.get('/login', (req, res) => {
    res.send('这是登录页面');
});
app.listen(9000, () => {
    console.log('服务已启动!');
});

// const express = require('express');
// //创建应用对象
// const app = express();
// //获取请求的路由规则
// app.get('/request', (req, res) => {
//     //1. 获取报文的方式与原生 HTTP 获取方式是兼容的
//     console.log(req.method);
//     console.log(req.url);
//     console.log(req.httpVersion);
//     console.log(req.headers);
//     //2. express 独有的获取报文的方式
//     //获取查询字符串
//     console.log(req.query); // 『相对重要』
//     // 获取指定的请求头
//     console.log(req.get('host'));
//     res.send('请求报文的获取');
// });
// //启动服务
// app.listen(3000, () => {
//     console.log('启动成功....')
// })