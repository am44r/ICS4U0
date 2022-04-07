from orc import Orc
from goblin import Goblin
from elf import Elf
from dwarf import Dwarf
import time
import random


def checkEnemyLife(enemyLives):
    if enemyLives == 0:
        print("Game over! You slayed the enemy!")
        exit()


def playerDodge():
    randomNumberToDodge = random.randint(1, 9)
    userRandomNumberChoice = int(input("Guess a number between 1-9: "))
    if userRandomNumberChoice == randomNumberToDodge:
        player.dodge()
    else:
        player._hp -= 1
        print(f"You lost a life!({player._hp} life)")


print("Welcome to Heros vs Villains (super unique name I know). You soon shall spawn as a Hero and fight the Orcs or Goblins\n")
print("How to play:\n1. You will choose a hero to play as\n2. Follow the prompts on the screen\n")

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

if userChoice == 1:
    player = Elf(3, 2)


if userChoice == 2:
    player = Dwarf(4, 1)


enemyTypeRand = random.randint(1, 2)
if enemyTypeRand == 1:
    enemyOne = Goblin(2, 1, 2)


if enemyTypeRand == 2:
    enemyOne = Orc(3, 2)

print(
    f"\nWelcome soldier. You are fighting as a(n) {player._heroType} agaisnt the mighty {enemyOne._villainType}!!\n")


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

if player._heroType == "Dwarf" and isAttack:
    print(player.slash()+"\n")
    enemyOne._hp -= 2

    print(enemyOne.getVillainType()+"\n")

    print("The enemy will is using a speical attack!\n")
