const Herp = require('./Hero');

class Elf extends Hero {
    constructor() { super(type, lives, hp); }

    shootArrow() {
        if (lives > 0) {
            console.log('Elf shot an arrow!');
        }
    }
}


