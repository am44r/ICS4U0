'use strict';

const User = require('./User');


class Student extends User {
    constructor(name, email, isLearning, isStudying, strikes = 0) {
        super(name, email);

        this.isLearning;
        this.isStudying;
        this.strikes;
    }
}