from villain import Villain


class Goblin(Villain):
    '''
    A goblin object that inherits the villain object. Goblin holds its type, lives,
    HP, and amount of special attacks

    Attributes
    ----------
    hp : float
        The health points of the Goblin
    specialCharges :  int
        The amount of special attacks the goblin has left to used

    Methods
    -------
    All methods in Goblin Class are private
    '''

    def __init__(self, hp=2, specialCharges=1):
        '''
        The constructor in the object. It is called when an object is created and initializes
        the attributes of the object

        Parameters
        ----------
        hp : int
            quantity of HP the goblin has
        specialCharges : int
            quantity of special charges the goblin has left

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
        super().__init__(villainType='Goblin', lives=1)

    def handSmack(self):
        '''
        Notifies player that the Goblin attempted to attacking

        Returns
        -------
        string
            Short messages informing the user their Hero was attacked
        '''
        return "Goblin smacked your hero!"

    def specialBite(self):
        '''
        Modifies the Goblins quantity of special charges and notifes the User that Goblin
        used a special attack

        Returns
        -------
        string
            short message notifying user
        '''
        if self._specialCharges > 0:
            self._specialCharges -= 1
            return "Goblin used special attack Bite"
