const Villain = require('./Villain');

class Goblin extends Villain {
    constructor() {
        super(type = type, lives = 1, hp = 20);
    }

    screamAttack() {
        alert('Screamed!');
    }
}