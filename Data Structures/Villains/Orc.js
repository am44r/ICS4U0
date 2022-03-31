const Villain = require('./Villain');

class Orc extends Villain {
    constructor() {
        super(type = type, lives, hp);
    }

    meatEat(hp, lives) {
        if (hp > 0 && lives > 0) {
            alert('Eating Meat');
            this.hp += 2;
        }
    }

    clubSwing() {
        if (lives >= 1) {
            alert('Orc swinged his club at your head!');
        }
    }

} 