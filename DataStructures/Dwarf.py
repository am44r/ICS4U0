from hero import Hero


class Dwarf(Hero):
    '''
    A Dwarf object that inherits the hero object. Dwarf holds its type, lives,
    HP, and amount of special attacks

    Attributes
    ----------
    hp : float
        The health points of the Dwarf
    specialCharges :  int
        The amount of special attacks the Dwarf has left to used

    Methods
    -------
    All methods in Dwarf Class are private
    '''

    def __init__(self, hp=5, specialCharges=1):
        '''
        The constructor in the object. It is called when an object is created and initializes
        the attributes of the object

        Parameters
        ----------
        hp : int
            quantity of HP the dwarf has
        specialCharges : int
            quantity of special charges the dwarf has left

        Super
        -----
        villainType : string
            The name of the hero race
        lives : int
            amount of lives dwarf has left

        Returns
        -------
        None
        '''
        self._hp = hp
        self._specialCharges = specialCharges
        super().__init__(heroType="Dwarf", lives=3)

    def slash(self):
        '''
        Notfies the User that his hero used an attack

        Returns
        -------
        string
            Short messages informing the user their Hero used attack
        '''

        return "Your hero slashed the enemy!"

    def useOrcrist(self):
        '''
        Modifies the Dwarf's quantity of special charges and notifes the User that Dwarf
        used a special attack

        Returns
        -------
        string
            short message notifying user that special was used
        '''
        if self._specialCharges > 0:
            self._specialCharges -= 1
            return "Your hero used Orcrist to slash the enemy!"
