// 创建buffer
// let buf = Buffer.alloc(10);
// console.log(buf);

// let buf2 = Buffer.allocUnsafe(10); 不安全,保留历史数据
// console.log(buf2);

// let buf3 = Buffer.from("hellp world");  将字符串变成buffer
// console.log(buf3);

// let buf4 = Buffer.from([1, 2, 3, 4, 5]);
// console.log(buf4);

let buf = Buffer.from("i love you");
console.log(buf);
buf[0] = 71;
console.log(buf[0].toString(2));
console.log(buf.toString());
