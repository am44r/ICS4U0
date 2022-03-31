module.export = class Villain {
    constructor(name='Villain', hp, lives) {
        this._name = name;
        this._hp = hp;
        this._lives = lives;
        this._dead = false;
    }

    takeDamage(damage) {
        let priorDamageTaken = this._hp - damage;

        if (priorDamageTaken >= 0) {
            this._hp = priorDamageTaken;
        }else{
            this._lives -= 1;
            if (this._lives > 0) {
                console.alert(`Lost a life`);
            }else{
                console.alert('Dude is dead!');
                this._dead = true;
            }
        }
        
    }
}