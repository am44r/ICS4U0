from orc import *
from goblin import *
from elf import *
from dwarf import *
import time
import random


def checkEnemyLife(enemyLives):
    if enemyLives == 0:
        print("Game over! You slayed the enemy!")
        exit()


print("Welcome to Heros vs Villains (super unique name I know). You soon shall spawn as a Hero and fight the Orcs or Goblins\n")
print("How to play:\n1. You will choose a hero to play as\n2. Follow the prompts on the screen\n")

print("Loading......\n")
time.sleep(1)

print("Please choose a character class to play as")

userHeroChoice = None
while userHeroChoice == None:
    try:
        userChoice = int(
            input("To play as an Elf (1). To play as a Dwarf (2): "))
        userHeroChoice = False
    except ValueError:
        print("Please choose a number (1) or (2).")

if userChoice == 1:
    player = Elf(3, 2)
    userHero = "Elf"


if userChoice == 2:
    player = Dwarf(4, 1)
    userHero = "Dwarf"


enemyTypeRand = random.randint(1, 2)
if enemyTypeRand == 1:
    enemyOne = Goblin(2, 1, 2)
    enemy = "Goblin"


if enemyTypeRand == 2:
    enemyOne = Orc(3, 2)
    enemy = "Orc"

print(
    f"\nWelcome soldier. You are fighting as a(n) {userHero} agaisnt the mighty {enemy}!!\n")

print("The enemy is attacking!!!\n")
if enemy == "Goblin":
    print(enemyOne.handSmack())
    print("\nYou have to dodge the attack!")

randomNumberToDodge = randint(1, 9)
if randint(1, 9) + randint(1, 9) == randomNumberToDodge:
    player.dodge()
else:
    player._hp -= 1

print("Time to Attack!\n")
isAttack = input("Press enter!")
if userHero == "Elf" and isAttack:
    player.shootArrow()
    enemyOne._hp -= 1
    checkEnemyLife(enemyOne._lives)
