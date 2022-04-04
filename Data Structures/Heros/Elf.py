from Heros import Hero


class Elf(Hero):
    def __init__(self, hp, specialCharges):
        self._hp = hp
        self._specialCharges = specialCharges
        super().__init__(heroType="Elf", lives=3)

    def shootArrow(self):
        return 'Elf shot an arrow at the enemy!'

    def shootSpecial(self):
        if self._specialCharges > 0 and self._hp > 2:
            return 'Elf used a special attack!'
