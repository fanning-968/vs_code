const fs = require('fs');

// 创建一个可写流
const writeStream = fs.createWriteStream('./座右铭.txt', {
    flags: 'a' // 追加写入
});

// 写入内容
writeStream.write('hello 1\n');
writeStream.write('hello 2\n');
writeStream.write('hello 3\n');

// 标记写入完成
writeStream.end();