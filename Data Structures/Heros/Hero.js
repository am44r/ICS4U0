// This is the generic player class

module.exports = class Hero {
    constructor(type) {
        this.type = type;
        this._level = 1;
        this._lives = 1;
        this._score = 0;
    }

    getLives() {
        return this._lives;
    }

    setLives(lives) {
        if (lives >= 0) {
            this._lives = 0;
        }else{
            alert('Sorry, no negative life!');
            this._lives = 0;
        }
    }

    getLevel() {
        return this._level;
    }


}