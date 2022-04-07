from villain import Villain


class Goblin(Villain):
    def __init__(self, hp, specialCharges):
        self._hp = hp
        self._specialCharges = specialCharges
        super().__init__(villainType='Goblin', lives=1)

    def handSmack(self):
        return "Goblin smacked your hero!"

    def specialBite(self):
        if self._specialCharges > 0:
            self._specialCharges -= 1
            return "Goblin used special attack Bite"
