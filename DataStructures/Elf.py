from hero import Hero


class Elf(Hero):
    '''
    A elf object that inherits the hero object. Elf holds its type, lives,
    HP, and amount of special attacks

    Attributes
    ----------
    hp : float
        The health points of the Elf
    specialCharges :  int
        The amount of special attacks the Elf has left to used

    Methods
    -------
    All methods in Elf Class are private
    '''

    def __init__(self, hp=4, specialCharges=1):
        '''
        The constructor in the object. It is called when an object is created and initializes
        the attributes of the object

        Parameters
        ----------
        hp : float
            quantity of HP the elf has
        specialCharges : int
            quantity of special charges the elf has left

        Super
        -----
        villainType : string
            The name of the hero race
        lives : int
            amount of lives elf has left

        Returns
        -------
        None
        '''
        self._hp = hp
        self._specialCharges = specialCharges
        super().__init__(heroType="Elf", lives=3)

    def shootArrow(self):
        '''
        Notfies the User that Elf used an attack

        Returns
        -------
        string
            Short messages informing the user Elf used attack
        '''
        return 'Elf shot an arrow at the enemy!'

    def shootDailir(self):
        '''
        Modifies the Dwarf's quantity of special charges and notifes the User that Dwarf
        used a special attack. Also decreases Elf's HP.

        Returns
        -------
        string
            short message notifying user that special was used and how much HP they lost
        '''
        if self._specialCharges > 0:
            self._specialCharges -= 1
            self._hp -= 0.5
            return 'Elf used Belthronding and shot Dailir at the enemy! (-1 HP)'
