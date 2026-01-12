const fs = require('fs');

// const arr = 'bob,tom,jerry,alice';

// let names = arr.split(',')

// for (const name of names) {
//    console.log(name);
// }

const dir = fs.readdirSync('./')

dir.forEach( item => {
    let names = item.split('-');

    let [number, name] = names;

    if (Number(number) < 10) {
        number = '0' + number;
    }

    let newName = number + name

    fs.renameSync(`./${item}`, `./${newName}`);

});
// // console.log(dir);