const fs = require('fs');

// 追加写入
fs.appendFile('./message.txt', '三人行,必有我师焉\n', (err) => {
    if (err) {
        console.log('写入失败');
        return;
    }
    console.log('写入成功');
})
// 追加写入第二中写入方式,flag可以去掉,变为覆盖写入
fs.writeFile('./message.txt', '三人行,必有我师焉', { flag: 'a' }, (err) => {
    if (err) {
        console.log('写入失败');
        return;
    }
    console.log('写入成功');
})

console.log(1 + 1);

// 同步写入
fs.writeFileSync('./message.txt', 'test sync 写入内容');
