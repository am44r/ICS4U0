from villain import Villain


class Orc(Villain):
    def __init__(self, hp, specialCharges):
        self._hp = hp
        self._specialCharges = specialCharges
        super().__init__(villainType="Orc", lives=2)

    def hammerSlash(self):
        return "Orc attempted to slash you!"

    def specialSlash(self):
        if self._specialCharges > 0 and self._hp > 2:
            return "Orc used a special slash on your hero!"
