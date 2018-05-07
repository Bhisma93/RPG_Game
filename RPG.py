from RPG1 import Hero
from RPG1_1 import Goblin
from RPG1_3 import Zombie

def main():
    mainHero = Hero(10, 5)
    mainGoblin = Goblin(6, 2)
    mainZombie = Zombie(1000000000, 100000000)
    KeepGoing = True

    while mainGoblin.alive() and mainHero.alive() and mainZombie.alive() and KeepGoing:
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("4. fight zombie")
        print("5. let zombie eat you(if you choose this your weird and need help)")
        print("> ",)
        user_input = input()
        if user_input == "1":
            mainHero.attack(mainGoblin)
            mainGoblin.print_status(mainGoblin)
            if not mainGoblin.alive():
                print("The goblin is dead.")
        elif user_input == "2":
            mainGoblin.attack(mainHero)
            mainHero.print_status(mainHero)
            if not mainHero.alive():
                print("The hero is dead.")
        elif user_input == "3":
            print("Goodbye.")
            KeepGoing = False
        elif user_input == "4":
            mainHero.attack(mainZombie)
            mainZombie.print_status(mainZombie)
            if not mainZombie.alive():
                print("The zombie is dead.")
        elif user_input == "5":
            mainZombie.attack(mainHero)
            mainHero.print_status(mainHero)
            if not mainHero.alive():
                print("The hero is a moron because he chose this option, and died.")
        else:
            print("Invalid input %r" % user_input)
        if mainGoblin.health > 0:
            if mainHero.health <= 0:
                print("You are dead.")


main()

