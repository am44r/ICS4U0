// This is the generic player class

module.export = class Hero {
    constructor(type) {
        this.type = type;
        this._level = 1;
        this._lives = 1;
        this._score = 0;
    }

    getLives() {
        return this._lives;
    }

    setLives(_lives) {
        if (_lives >= 0) {
            this._lives = 0;
        }else{
            console.alert('Sorry, no negative life!');
            this._lives = 0;
        }
    }

    getLevel() {
        return this._level;
    }


}