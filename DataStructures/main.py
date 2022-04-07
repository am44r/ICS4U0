'''
-----------------------------------------------------------------------------
Name:       Heros vs Villains (main.py)
Purpose:    A mini game that allows a user to play as a hero to fight the
            villains.

References: https://www.geeksforgeeks.org/read-json-file-using-python/
            https://www.youtube.com/watch?v=ZDa-Z5JzLYM
            https://www.youtube.com/watch?v=wfcWRAxRVBA
            https://www.youtube.com/watch?v=RSl87lqOXDE

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
    with open(filePath, "w") as file:
        json.dump(data, file)


def checkEnemyAlive(enemyLives):
    '''
    Checks if the enemy is still alives based on lives left

    Parameters
    ----------
    enemyLives : int
        The amount of lives the enemy has left

    Returns
    ---------
    None

    '''
    if enemyLives == 0:
        print("Game over! You slayed the enemy!")
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
    randomNumberToDodge = random.randint(1, 9)
    userRandomNumberChoice = int(input("Guess a number between 1-9: "))
    if userRandomNumberChoice == randomNumberToDodge:
        player.dodge()
    else:
        player._hp -= 1
        print(f"You lost a life!({player._hp} life)")


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
    try:
        userChoice = int(
            input("To play as an Elf (1). To play as a Dwarf (2): "))
        userHeroChoice = False
    except ValueError:
        print("Please choose a number (1) or (2).")

isLoadSavedData = input("Would you like to load saved data (y/n)?: ")

if userChoice == 1 and isLoadSavedData == "y":
    loadSavedHero = json.load(open('hero_data.json'))
    player = Elf(int(loadSavedHero['heroLives']),
                 int(loadSavedHero['heroSpecials']))
else:
    player = Elf(3, 2)
    heroData["heroType"] = "Elf"
    heroData["heroLives"] = 3
    heroData["heroSpecials"] = 2
    writeToJSON(path, heroSaved, heroData)


if userChoice == 2 and isLoadSavedData == 'y':
    loadSavedHero = json.load(open('hero_data.json'))
    print(loadSavedHero)
    player = Dwarf(int(loadSavedHero['heroLives']),
                   int(loadSavedHero['heroSpecials']))
else:
    player = Dwarf(3, 1)
    heroData["heroType"] = "Dwarf"
    heroData["heroLives"] = 3
    heroData["heroSpecials"] = 2
    writeToJSON(path, heroSaved, heroData)


enemyTypeRand = random.randint(1, 2)
if enemyTypeRand == 1 and isLoadSavedData == 'y':
    localSavedVillain = json.load(open('villain_data.json'))
    enempyOne = Goblin(int(localSavedVillain['enemyLives']), int(
        localSavedVillain['enemySpecials']))
else:
    enemyOne = Goblin(2, 1)
    enemyData["villainType"] = "Goblin"
    enemyData["enemyLives"] = 2
    enemyData["enemySpecials"] = 1
    writeToJSON(path, villainSaved, enemyData)

if enemyTypeRand == 2 and isLoadSavedData == 'y':
    localSavedVillain = json.load(open('villain_data.json'))
    enempyOne = Goblin(int(localSavedVillain['enemyLives']), int(
        localSavedVillain['enemySpecials']))
else:
    enemyOne = Orc(2, 2)
    enemyData["villainType"] = "Orc"
    enemyData["enemyLives"] = 3
    enemyData["enemySpecials"] = 2
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
if player._heroType == "Elf" and isAttack is not None:
    print(player.shootArrow()+"\n")
    enemyOne._hp -= 2
    print(enemyOne.getVillainLives())

if player._heroType == "Dwarf" and isAttack is not None:
    print(player.slash())
    enemyOne._hp -= 2
    print(enemyOne.getVillainLives())


print("The enemy will is using a speical attack!\n")
if enemyOne._villainType == "Orc" and enemyOne._specialCharges > 0:
    print(enemyOne.specialSlash())
    enemyOne._specialCharges -= 1
    player._hp -= 1
    print(
        f"Orc has used up a special. Costed your hero {player.getHeroLives()}")


isDeleteJSON = str(input("\nDelete saved data (y, n)?: "))
if isDeleteJSON == "y":
    heroData = {}
    enemyData = {}
    writeToJSON(path, heroSaved, heroData)
    writeToJSON(path, villainSaved, enemyData)
else:
    print("Game Data Saved.")
