'''
-----------------------------------------------------------------------------
Name:       Heros vs Villains (main.py)
Purpose:    A mini game that allows a user to play as a hero to fight the
            villains.

References: Multiple YouTube vidoes were used to learn topics such as JSON and Classes
                https://www.geeksforgeeks.org/read-json-file-using-python/
                https://www.youtube.com/watch?v=ZDa-Z5JzLYM
                https://www.youtube.com/watch?v=wfcWRAxRVBA
                https://www.youtube.com/watch?v=RSl87lqOXDE
                https://www.youtube.com/watch?v=Ogym0QZLDgw&ab_channel=Keith%2CtheCoder

            Official Python Docs was also used to learn Random and Time
                https://docs.python.org/3/library/random.html
                https://docs.python.org/3/library/time.html

Author:      Amaar S
Created:     28-Mar-2022
Updated:     07-Apr-2022
-----------------------------------------------------------------------------
'''
# Importing the classes and children of the classes
from orc import Orc
from goblin import Goblin
from elf import Elf
from dwarf import Dwarf

# Importing miscelaneous
import time
import random
import json


def writeToJSON(path, fileName, data):
    '''
    Writes data to a JSON file

    Parameters
    ----------
    path : string
        The path/directory I want the function to look/userChoice

    fileName: string
        Name of the JSON file created to write Data

    data : dict
        storage in dictionary to be loaded into main.py

    Returns
    ---------
    None

    '''
    filePath = "./" + path + "./" + fileName + ".json"
    # Opens the file in write mode (w)
    with open(filePath, "w") as file:
        # Writes the data to the file
        json.dump(data, file)


def looseEnemyLife():
    '''
    Takes away a life from enemy if they have no HP

    Returns
    ---------
    None

    '''
    if enemyOne._hp < 0:
        enemyOne._lives -= 1


def checkEnemyAlive(enemyLives):
    '''
    Checks if the enemy is still alive based on lives left

    Parameters
    ----------
    enemyLives : int
        The amount of lives the enemy has left

    Returns
    ---------
    None

    '''
    if enemyLives == 0:
        print("\nGame over! You slayed the enemy!")
        exit()


def playerDodge():
    '''
    Allows the user to dodge and attack by guessing a random number
    and either decreases or increase the hero's HP

    Parameters
    ----------
    None

    Returns
    -------
    None

    '''
    # Generates a random integer from 1-9 and stores in variable
    randomNumberToDodge = random.randint(1, 9)
    userRandomNumberChoice = int(input("Guess a number between 1-9: "))
    if userRandomNumberChoice == randomNumberToDodge:
        player.dodge()
    else:
        player._hp -= 1
        print(f"Wrong! You lost a life!({player._hp} life)")


path = "./"
heroSaved = "hero_data"
villainSaved = "villain_data"
heroData = {}
enemyData = {}

print("Welcome to Heros vs Villains. Spawn as a Hero and fight\n")
print("How to play:\n1. Choose a hero to play as\n2. Follow the prompts\n")

print("Loading......\n")
time.sleep(1)

print("Please choose a character class to play as")

userHeroChoice = None
while userHeroChoice is None:
    # Trys to collect correct value of user input
    try:
        userChoice = int(
            input("To play as an Elf (1). To play as a Dwarf (2): "))
        userHeroChoice = False
    # Throws error when the user inputs wrong type
    except ValueError:
        print("Please choose a number (1) or (2).")

isLoadSavedData = input(
    "Would you like to load saved data (y/n) ('n' if first time play)?: ")

if userChoice == 1 and isLoadSavedData == "y":
    # Assigning a variable to hold all loaded JSON info
    loadSavedHero = json.load(open('hero_data.json'))
    # Creating a new instance of a hero using the data from the JSON file
    player = Elf(int(loadSavedHero['heroLives']),
                 int(loadSavedHero['heroSpecials']))
else:
    player = Elf(4, 2)
    # Manually writing data to the JSON file
    heroData["heroType"] = "Elf"
    heroData["heroLives"] = str(3)
    heroData["heroSpecials"] = str(2)
    # Using the write to JSON function to write the info to JSON
    writeToJSON(path, heroSaved, heroData)


if userChoice == 2 and isLoadSavedData == 'y':
    # Assigning a variable to hold all loaded JSON info
    loadSavedHero = json.load(open('hero_data.json'))
    # Creating a new instance of a hero using the data from the JSON file
    player = Dwarf(int(loadSavedHero['heroLives']),
                   int(loadSavedHero['heroSpecials']))
else:
    player = Dwarf(5, 1)
    # Manually writing data to the JSON file
    heroData["heroType"] = "Dwarf"
    heroData["heroLives"] = str(2)
    heroData["heroSpecials"] = str(2)
    # Using the write to JSON function to write the info to JSON
    writeToJSON(path, heroSaved, heroData)


enemyTypeRand = random.randint(1, 2)
if enemyTypeRand == 1 and isLoadSavedData == 'y':
    # Assigning a variable to hold all loaded JSON info
    localSavedVillain = json.load(open('villain_data.json'))
    # Creating a new instance of a hero using the data from the JSON file
    enempyOne = Goblin(int(localSavedVillain['enemyLives']), int(
        localSavedVillain['enemySpecials']))
else:
    enemyOne = Goblin(2, 1)
    # Manually writing data to the JSON file
    enemyData["villainType"] = "Goblin"
    enemyData["enemyLives"] = str(2)
    enemyData["enemySpecials"] = str(1)
    # Using the write to JSON function to write the info to JSON
    writeToJSON(path, villainSaved, enemyData)

if enemyTypeRand == 2 and isLoadSavedData == 'y':
    # Assigning a variable to hold all loaded JSON info
    localSavedVillain = json.load(open('villain_data.json'))
    # Creating a new instance of a hero using the data from the JSON file
    enempyOne = Goblin(int(localSavedVillain['enemyLives']), int(
        localSavedVillain['enemySpecials']))
else:
    enemyOne = Orc(3, 2)
    # Manually writing data to the JSON file
    enemyData["villainType"] = "Orc"
    enemyData["enemyLives"] = str(3)
    enemyData["enemySpecials"] = str(2)
    # Using the write to JSON function to write the info to JSON
    writeToJSON(path, villainSaved, enemyData)


print(
    f"\nYou're a(n) {player._heroType} agaisnt the {enemyOne._villainType}!\n")


print("The enemy is attacking!!!\n")
if enemyOne._villainType == "Goblin":
    print(enemyOne.handSmack())

if enemyOne._villainType == "Orc":
    print(enemyOne.hammerSlash()+"\n")

    print("\nYou have to dodge the attack!")

playerDodge()

print("\nTime to Attack!")
isAttack = input("Press enter!")

# Converts the value to bool and checks if false becuase empty str -> bool == False
if player._heroType == "Elf" and bool(isAttack) is False:
    print(player.shootArrow()+"\n")
    enemyOne._hp -= 2
    print(enemyOne.getVillainLives())

# Converts the value to bool and checks if false becuase empty str -> bool == False
if player._heroType == "Dwarf" and bool(isAttack) is False:
    print(player.slash())
    enemyOne._hp -= 2
    print(enemyOne.getVillainLives())

looseEnemyLife()
# Checks if the enemy is alive or not and ends game if they aren't
checkEnemyAlive(enemyOne._lives)


print("\nThe enemy will is using a speical attack!\n")
if enemyOne._villainType == "Orc" and enemyOne._specialCharges > 0:
    print(enemyOne.specialSlash())
    enemyOne._specialCharges -= 1
    player._hp -= 1
    print(
        f"Orc has used up a special. Hero has {player._hp}HP now")

if enemyOne._villainType == "Goblin" and enemyOne._specialCharges > 0:
    print(enemyOne.specialBite())
    enemyOne._specialCharges -= 1
    player._hp -= 2
    print(
        f"Goblin has used up a special. Hero has {player._hp}HP now")

print("\nLets use a special attack against the enemy!")
isUseSpecial = input("Press Enter!")
# Converts the value to bool and checks if false becuase empty str -> bool == False
if player._heroType == "Elf" and bool(isUseSpecial) is False:
    player.shootDailirg()
    enemyOne._hp -= 2

# Converts the value to bool and checks if false becuase empty str -> bool == False
if player._heroType == "Dwarf" and bool(isUseSpecial) is False:
    player.useOrcrist()
    enemyOne._hp -= 2

looseEnemyLife()
# Checks if the enemy is alive or not and ends game if they aren't
checkEnemyAlive(enemyOne._lives)

# This set of code allows a user to save their current gamestate and re-load it
# later if they want

# Asks user if they would like to store or delete the gamedata
isDeleteJSON = str(input("\nDelete saved data (0 - no, 1 - yes)?: "))
# Converts the user input from string to int for usage
if int(isDeleteJSON) == 1:
    # Creates empty dictionaries for both the hero and villain
    heroData = {}
    enemyData = {}
    # Writes they emtpy dictionaries to the files
    writeToJSON(path, heroSaved, heroData)
    writeToJSON(path, villainSaved, enemyData)
else:
    # Nothing in the JSON files change
    print("Game Data Saved.")
