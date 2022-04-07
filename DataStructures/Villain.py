class Villain():
    def __init__(self, villainType, lives):
        self._villainType = villainType
        self._lives = lives

    def getVillainType(self):
        print(f"Your enemy is of type {self._villainType}. Be weary!")

    def getVillainLives(self):
        print(f"Your enemy has {self._lives} live(s).")
