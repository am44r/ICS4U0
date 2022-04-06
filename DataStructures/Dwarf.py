import Hero


class Dwarf(Hero):
    def __init__(self, hp, specialCharges):
        self._hp = hp
        self._specialCharges = specialCharges
        super().__init__(heroType="Dwarf", lives=3)

    def slash(self):
        return "Your hero slashed the enemy!"

    def specialSliceStatus(self):
        if self._specialCharges > 0:
            return "Your hero is able to use a special attack!"

    def useSpecial(self):
        if self._specialCharges > 0 and self._hp > 2:
            self._specialCharges -= 1
            return "Your hero used Orcrist to slash the enemy!"
