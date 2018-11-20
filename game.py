#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def attack(self, monster):
            # Hero attacks goblin
        monster.health-= self.power
        print(f"You did {self.power} damage to the goblin.")
        if monster.health <= 0:
            print("The goblin is dead.")
        print(f"The goblin has {monster.health} health left.")
    def alive(self):
        if self.health > 0:
            print(f"You have {self.health} health left.")

class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def attack(self, human):
        # Goblin attacks hero
        human.health -= self.power
        print(f"The goblin does {self.power} damage to you.")
        if human.health <= 0:
            print("You are dead.")
    def alive(self):
        if self.health > 0:
            print(f"The goblin has {self.health} health left.")


            


heroErick = Hero(10, 5)
goblinAnuj = Goblin(6, 2)

heroErick.attack(goblinAnuj)
goblinAnuj.attack(heroErick)

heroErick.alive()
goblinAnuj.alive()


# def main():
#     hero_health = 10
#     hero_power = 5
#     goblin_health = 6
#     goblin_power = 2

#     while goblin_health > 0 and hero_health > 0:
#         print("You have {} health and {} power.".format(hero_health, hero_power))
#         print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
#         print()
#         print("What do you want to do?")
#         print("1. fight goblin")
#         print("2. do nothing")
#         print("3. flee")
#         print("> ", end=' ')
#         raw_input = input()
#         if raw_input == "1":
#             # Hero attacks goblin
#             goblin_health -= hero_power
#             print("You do {} damage to the goblin.".format(hero_power))
#             if goblin_health <= 0:
#                 print("The goblin is dead.")
#         elif raw_input == "2":
#             pass
#         elif raw_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print("Invalid input {}".format(raw_input))

        # if goblin_health > 0:
        #     # Goblin attacks hero
        #     hero_health -= goblin_power
        #     print("The goblin does {} damage to you.".format(goblin_power))
        #     if hero_health <= 0:
        #         print("You are dead.")

# main()