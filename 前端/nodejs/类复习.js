class Person {
    name;
    age;
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    eat() {
        console.log(this.name + "在吃饭");
    }

    speak() {
        console.log(this.name + "在说话");
    }
}

class Studennt extends Person {
    sno;
    constructor(name, age, sno) {
        super(name, age);
        this.sno = sno;
    }

    study() {
        console.log(this.name + "在学习");
    }

    speak() {
        console.log(this.name + "在学生说话");
    }
}

const stu = new Studennt("张三", 20, "001");