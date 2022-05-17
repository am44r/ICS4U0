class Hero():
    '''
    A Villain object that holds the race and lives of a character

    Attributes
    ----------
    heroType : string
        The specific race of hero
    lives : int
        The amount of lives the hero has

    Methods
    -------
    getHeroType() -> None
        Prints the race of the hero to the console
    getHeroLives -> None
        Prints the amount of lives the hero has left
    '''

    def __init__(self, heroType, lives):
        self._heroType = heroType
        self._lives = lives

    def getHeroType(self):
        '''
        Tells the user the race of their hero

        Parameters
        ----------
        None

        Returns
        -------
        string
            small message telling the user the race of hero
        '''
        return f"Your hero is of type {self._heroType}."

    def getHeroLives(self):
        '''
        Tells the user the amount of lives their hero has

        Parameters
        ----------
        None

        Returns
        -------
        string
            small message telling the user the amount of lives
        '''
        return f"Your hero has {self._lives} lives."

    def dodge(self):
        '''
        Returns that the user dodged an enemies attack

        Returns
        -------
        string
            short message notifying user that dodge was used
        '''
        return "You dodged the enemies attack!!"
