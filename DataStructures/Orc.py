from villain import Villain


class Orc(Villain):
    '''
    An Orc object that inherits the villain object. Orc holds its type, lives,
    HP, and amount of special attacks

    Attributes
    ----------
    hp : float
        The health points of the Orc
    specialCharges :  int
        The amount of special attacks the Orc has left to used

    Methods
    -------
    All methods in Orc Class are private
    '''

    def __init__(self, hp=3, specialCharges=2):
        '''
        The constructor in the object. It is called when an object is created and initializes
        the attributes of the object

        Parameters
        ----------
        hp : int
            quantity of HP the orc has
        specialCharges : int
            quantity of special charges the orc has left

        Super
        -----
        villainType : string
            The name of the villains race
        lives : int
            amount of lives goblin has left

        Returns
        -------
        None
        '''
        self._hp = hp
        self._specialCharges = specialCharges
        super().__init__(villainType="Orc", lives=1)

    def hammerSlash(self):
        '''
        Notifies player that the Orc attempted to attacking

        Returns
        -------
        string
            Short messages informing the user the Orc attacked
        '''
        return "Orc attempted to slash you!"

    def specialSlash(self):
        '''
        Modifies the Goblins quantity of special charges and notifes the User that Goblin
        used a special attack

        Returns
        -------
        string
            short message notifying user
        '''
        if self._specialCharges > 0 and self._hp > 2:
            return "Orc used a special slash on your hero!"
