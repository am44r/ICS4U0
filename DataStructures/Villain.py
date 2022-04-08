class Villain():
    '''
    A Villain object that holds the race and lives of a character

    Attributes
    ----------
    villainType : string
        The specific race of villain
    lives : int
        The amount of lives the villain has

    Methods
    -------
    getVillainType() -> None
        Prints the race of the villain to the console
    getVillainLives -> None
        Prints the amount of lives the villain has left
    '''

    def __init__(self, villainType, lives):
        self._villainType = villainType
        self._lives = lives

    def getVillainType(self):
        '''
        Tells the user the race of the villain

        Parameters
        ----------
        None

        Returns
        -------
        string
            small message telling the user the race of villain
        '''
        print(f"Your enemy is of type {self._villainType}. Be weary!")

    def getVillainLives(self):
        '''
        Tells the user the amount of lives the villain has

        Parameters
        ----------
        None

        Returns
        -------
        string
            small message telling the user the amount of lives
        '''
        print(f"Your enemy has {self._lives} live(s).")
