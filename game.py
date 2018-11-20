#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Character:
    def __init__(self, noun, health, power):
        self.noun = noun
        self.health = health
        self.power = power

    def attack(self, monster):
        monster.health -= self.power
        print(f"You did {self.power} damage to {monster.noun}.")
        print(f"{monster.noun} does {monster.power} damage to you.")
        if monster.health <= 0:
            print(f"{monster.noun} is dead.")
        if self.health <= 0:
            print("You are dead")
            
    def printStatus(self):
        if self.alive() == True:
            print(f"{self.noun} has {self.health} health left.") 

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Hero(Character):
    def __init__(self, noun, health, power):
        super().__init__ (noun, health, power)

class Goblin(Character):
    def __init__(self, noun, health, power):
        super().__init__(noun, health, power)

class Zombie(Character):
    def __init__(self, noun, health, power):
        super().__init__(noun, health, power)
    
    def regen(self):
        if self.health == 0:
            self.health += 5
            print("The zombie got it's health back and is alive!!!!")
            


def main():

    while goblinAnuj.health > 0 and heroErick.health > 0:
        print()
        print(f"You have {heroErick.health} health and {heroErick.power} power.")
        print(f"The goblin has {goblinAnuj.health} health and {goblinAnuj.power} power.")
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            heroErick.attack(goblinAnuj)

        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        # if goblinAnuj.health > 0:
        #     # Goblin attacks hero
        #     goblinAnuj.attack(heroErick)

def zombieInt():

    while zombiePhong.health > 0 and heroErick.health > 0:
        print()
        print(f"You have {heroErick.health} health and {heroErick.power} power.")
        print(f"The zombie has {zombiePhong.health} health and {zombiePhong.power} power.")
        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks zombie
            heroErick.attack(zombiePhong)
            zombiePhong.regen()

        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        # if zombiePhong.health > 0:
        #     # zombie attacks hero
        #     zombiePhong.attack(heroErick)



heroErick = Hero("The Hero", 10, 5)
goblinAnuj = Goblin("The Goblin", 6, 2)
zombiePhong = Zombie("The Zombie", 5,1)

main()
zombieInt()