class Hero(object):
    def __init__(self, heroType, lives):
        self._heroType = heroType
        self._lives = lives

    def getHeroType(self):
        return f"Your hero is of type {self._heroType}."

    def getHeroLives(self):
        return f"Your hero has {self._lives} lives to start with."

    def sharpenWeapon(self):
        return f"{self._heroType} sharpened weapon and increased DP by 1!"
