const Herp = require('./Hero');

class Elf extends Hero {
    constructor() { super(type, lives, hp); }

    shootArrow() {
        if (lives > 0) {
            alert('Elf shot an arrow!');
        }
    }

    usePotion(hp) {
        if (hp > 0) {
            this.hp++;
        }else{
            alert('You are dead!');
        }
    }
}


