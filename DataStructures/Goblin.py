import Villain


class Goblin(Villain):
    def __init__(self, hp, specialCharges, stickCount):
        self._hp = hp
        self._specialCharges = specialCharges
        self._stickCount = stickCount
        super().__init__(villainType='Goblin', lives=1)

    def handSmack(self):
        return "Goblin smacked your hero!"

    def specialBite(self):
        if self._specialCharges > 0:
            self._specialCharges -= 1
            return "Goblin used special attack Bite"

    def stickShove(self):
        if self._stickCount > 0:
            self._stickCount -= 1
            return "Goblin used a stick to rebuild his bones!"
