'use strict';

const User = require('./User');

class Teacher extends User {
    constructor(name, email, isTeaching) {
        super(name, email);

        this.isTeaching;
    }
}

let teacherOne = new Teacher('Bob', 'bob@gmail.com', true);
console.log(teacherOne.name);