'use strict';
const fs = require('fs');
const User = require('./User');



class Student extends User {
    constructor(name, email, isLearning=0, isStudying=0, strikes = 0) {
        super(name, email);

        this.isLearning;
        this.isStudying;
        this.strikes;
    }
}

fs.readFile('./studentList.json', 'utf8', (err, dataString) => {
    if(err) {
        console.log("Error has occured", err);
        return;
    }
    try {
        const student = JSON.parse(dataString);
        var studentOne = new Student(student.name, student.email, student.isLearning, student.isStudying);
        console.log(studentOne);
    } catch(err) {
        console.log('Error', err)
    }
});


