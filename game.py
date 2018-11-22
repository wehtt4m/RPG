import random
# !/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Character:
    def __init__(self, noun, health, power, originalHealth):
        self.noun = noun
        self.health = health
        self.power = power
        self.originalHealth = originalHealth

    def attack(self, monster):
        damage = self.power
        damageAfter = monster.power - self.armor
        if self.noun == "The Hero":
            critRoll = random.randint(1,5)
            if critRoll == 5:
                damage = 2 * self.power
                print("Critical Hit!")
        elif self.noun == "The Medic":
            if self.health < self.originalHealth:
                print(f"After the attack you have {self.health} health")
                if random.randint(1,5) == 5:
                    self.health += 2
                    print("You regenerated 2 health!")
        elif self.noun == "The Shadow":
            self.count(monster)

        if self.noun != "The Shadow":
            if self.armor == 0:
                self.health -= monster.power
            elif self.armor > 0:
                self.health -= damageAfter
            
        monster.health -= damage

        if self.evasion == 2:
            if random.randint(1,10) == 1:
                monster.power = 0
                damageAfter = 0
        elif self.evasion == 4:
            if random.randint(1,100) <= 15:
                monster.power = 0
                damageAfter = 0
        elif self.evasion == 6:
            if random.randint(1,10) <= 2:
                monster.power = 0
                damageAfter = 0

        print(f"You did {damage} damage to {monster.noun}.")
        if self.armor == 0:
            print(f"{monster.noun} does {monster.power} damage to you.")
        elif self.armor > 0:
            print(f"{monster.noun} does {damageAfter} damage to you because of your armor.")

        if monster.health <= 0:
            monster.coinDrop(self)

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

class GameInteraction():
    def shopInt(hero, store):
        print()
        print ("Welcome to the store!")
        print(f"You have {hero.coinbag} coins!")
        print()
        print("What would you like to do?")
        print("1.Purchase an item")
        # print("2.Sell an item")
        print("2.Leave")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            print("What would you like to buy?")
            print(f"1. {store.item1.name}")
            print(f"2 {store.item2.name}")
            print(f"3. {store.item3.name}")
            print(f"4. {store.item4.name}")
            raw_input = input()
            if raw_input == "1":
                print(f"That will be {store.item1.cost} coins.")
                print("Are you sure you want to buy this? (Y/N)")
                raw_input = str.upper(input())
                if raw_input == "Y":
                    if hero.coinbag < store.item1.cost:
                        print("Sorry you do not have enough money")
                    if hero.coinbag >= store.item1.cost:
                        hero.coinbag -= store.item1.cost
                        print("Thank you for your purchase!")
                        print(f"You have {hero.coinbag} coins left")
                        hero.backpack.append(store.item1)
                        for i in range(len(hero.backpack)):
                            print(f"Your backpack: {hero.backpack[i].name}")
                        GameInteraction.shopInt(hero,store)
                elif raw_input == "N":
                    GameInteraction.shopInt(hero,store)

            elif raw_input == "2":
                print(f"That will be {store.item2.cost} coins.")
                print("Are you sure you want to buy this? (Y/N)")
                raw_input = str.upper(input())
                if raw_input == "Y":
                    if hero.coinbag < store.item2.cost:
                        print("Sorry you do not have enough money")
                    if hero.coinbag >= store.item2.cost:
                        hero.coinbag -= store.item2.cost
                        print("Thank you for your purchase!")
                        print(f"You have {hero.coinbag} coins left")
                        hero.backpack.append(store.item2)
                        for i in range(len(hero.backpack)):
                            print(f"Your backpack: {hero.backpack[i].name}")                        
                        GameInteraction.shopInt(hero,store)
                elif raw_input == "N":
                    GameInteraction.shopInt(hero,store)

            elif raw_input == "3":
                print(f"That will be {store.item3.cost} coins.")
                print("Are you sure you want to buy this? (Y/N)")
                raw_input = str.upper(input())
                if raw_input == "Y":
                    if hero.coinbag < store.item3.cost:
                        print("Sorry you do not have enough money")
                    if hero.coinbag >= store.item3.cost:
                        hero.coinbag -= store.item3.cost
                        print("Thank you for your purchase!")
                        print(f"You have {hero.coinbag} coins left")
                        hero.backpack.append(store.item3)
                        for i in range(len(hero.backpack)):
                            print(f"Your backpack: {hero.backpack[i].name}")
                        GameInteraction.shopInt(hero,store)
                elif raw_input == "N":
                    GameInteraction.shopInt(hero,store)

            elif raw_input == "4":
                print(f"That will be {store.item4.cost} coins.")
                print("Are you sure you want to buy this? (Y/N)")
                raw_input = str.upper(input())
                if raw_input == "Y":
                    if hero.coinbag < store.item4.cost:
                        print("Sorry you do not have enough money")
                    if hero.coinbag >= store.item4.cost:
                        hero.coinbag -= store.item4.cost
                        print("Thank you for your purchase!")
                        print(f"You have {hero.coinbag} coins left")
                        hero.backpack.append(store.item4)
                        for i in range(len(hero.backpack)):
                            print(f"Your backpack: {hero.backpack[i].name}")
                        GameInteraction.shopInt(hero,store)
                elif raw_input == "N":
                    GameInteraction.shopInt(hero,store)

        # elif raw_input == "2":
        #     print("What would you like to sell?")
        elif raw_input == "2":
            print("Have a nice day!")

    def monsterInt(myClass, monster):
        order = 0  #used for inventory list
        while monster.health > 0 and myClass.health > 0:
            print()
            print(f"You have {myClass.health} health and {myClass.power} power.")
            print(f"{monster.noun} has {monster.health} health and {monster.power} power.")
            print()
            print("What do you want to do?")
            print(f"1. fight {monster.noun}")
            print("2. Use item")
            print("3. flee")
            print("> ", end=' ')
            raw_input = input()
            if raw_input == "1":
                # Hero attacks goblin and goblin attacks back
                if monster.noun == "The Zombie":
                    myClass.attack(monster)
                    monster.belowZ()
                    monster.regen()
                elif monster.noun == "The Dwarf":
                    myClass.attack(monster)
                    monster.itemDrop()
                else:
                    myClass.attack(monster)

            elif raw_input == "2":
                if len(myClass.backpack) > 0:

                    print("What item would you like to use?")
                    
                    for i in range(len(myClass.backpack)):
                        order = int(order)
                        order += 1
                        order = str(order)
                        print(order,".", f"{myClass.backpack[i].name}.")
                        
                    order = 0
                    raw_input = input()

                    if myClass.backpack[i].name == "Armor":
                        myClass.backpack[i].buff(myClass)
                        print(f"You have used {myClass.backpack[i].name}")
                        myClass.backpack.remove(myClass.backpack[i])
                    elif myClass.backpack[i].name == "Smoke Bomb":
                        myClass.backpack[i].buff(myClass)
                        print(f"You have used {myClass.backpack[i].name}")
                        print(f"Your evasion is now {myClass.evasion}")
                        myClass.backpack.remove(myClass.backpack[i])
                    elif myClass.backpack[i].name == "Super Tonic":
                        if myClass.noun == "The Shadow":
                            print("You cannot increase you health past 1.")
                        else:
                            myClass.backpack[i].buff(myClass)
                            print(f"You have used {myClass.backpack[i].name}")
                            print(f"You currently have {myClass.health} health")
                            myClass.backpack.remove(myClass.backpack[i])

                elif len(myClass.backpack) == 0:
                    print("Sorry you don't have any items")



            elif raw_input == "3":
                print("Goodbye.")
                break
            else:
                print("Invalid input {}".format(raw_input))

# #===================Playable Characters===================

class Hero(Character):
    def __init__(self, noun, health, power, originalHealth, backpack, coinbag, armor, evasion):
        super().__init__ (noun, health, power, originalHealth)
        self.backpack = []
        self.coinbag = 0
        self.armor = 0
        self.evasion = 0

class Medic(Character):
    def __init__(self, noun, health, power, originalHealth, backpack, coinbag, armor, evasion):
        super().__init__(noun, health, power, originalHealth)
        self.backpack = []
        self.coinbag = 0
        self.armor = 0
        self.evasion = 0

class Shadow(Character):
    def __init__(self, noun, health, power, originalHealth, attackCount, backpack, coinbag, armor,evasion):
        super().__init__(noun, health, power, originalHealth)
        self.health = 1
        self.originalHealth = 1
        self.attackCount = attackCount
        self.backpack = []
        self.coinbag = 0
        self.armor = 0
        self.evasion = 0

    def count(self, monster):
        if random.randint(1,10) < 10:
            monster.power = 0
    
    def notOne(self):
        if self.health > 1:
            print("Unable to increase health!")
            self.health = 1


class Knight(Character):
    def __init__(self, noun, health, power, originalHealth, armor, backpack, coinbag, evasion):
        super().__init__(noun, health, power, originalHealth)
        self.armor = 1
        self.backpack = []
        self.coinbag = 0
        self.evasion = 0


#===================Monsters===================

class Goblin(Character):
    def __init__(self, noun, health, power, originalHealth, bounty):
        super().__init__(noun, health, power, originalHealth)
        self.bounty = 1
    
    def coinDrop(self, hero):
        if self.health <= 0:
            print(f"{self.noun} is dead and dropped {self.bounty} coins.")
            hero.coinbag += self.bounty


class Zombie(Character):
    def __init__(self, noun, health, power, originalHealth, bounty):
        super().__init__(noun, health, power, originalHealth)
        self.bounty = 5
    
    def belowZ(self):
        if self.health < 0:
            self.health = 0
            return self.health
    
    def regen(self):
        if self.health == 0:
            self.health += 5
            print("The zombie got it's health back and is alive!!!!")

    def coinDrop(self, hero):
        if self.health <= 0:
            print(f"{self.noun} is dead and dropped {self.bounty} coins.")
            hero.coinbag += self.bounty


class Dwarf(Character):
    def __init__(self, noun, health, power, originalHealth, bounty):
        super().__init__(noun, health, power, originalHealth)
        self.bounty = 7

    def itemDrop(self):
        if self.health <= 0:
            # if random.randint(1,2) == 1 or random.randint(1,2) ==2:
            print("The dwarf dropped an item!")

    def coinDrop(self, hero):
        if self.health <= 0:
            print(f"{self.noun} is dead and dropped {self.bounty} coins.")
            hero.coinbag += self.bounty

#===================Store===================


class Tonic():
    def __init__(self, name, cost, value):
        self.name = "Super Tonic"
        self.cost = 2
        self.value = 1 

    def buff(self, hero):
        hero.health += 10
        

class Armor():
    def __init__(self, name, cost, value):
        self.name = "Leather Armor"
        self.cost = 5
        self.value = 3
    
    def buff(self,myClass):
        myClass.armor += 1
        
class Weapon():
    def __init__(self, name, cost, value):
        self.name = "Copper Sword"
        self.cost = 5
        self.value = 3

    def buff(self, hero):
        hero.power + 2

class Bomb():
    def __init__(self, name, cost, value):
        self.name = "Smoke Bomb"
        self.cost = 4
        self.value = 2
    
    def buff(self,myClass):
        myClass.evasion += 1
        

class Store():
    def __init__(self,item1, item2, item3, item4):
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.item4 = item4

    def inventory(self):
        items = [self.item1, self.item2, self.item3, self.item4]



knightMatt = Knight("The Knight", 25, 4, 25, None, None, None, None)
heroErick = Hero("The Hero", 10, 3, 10, None, None, None, None)
medicRay = Medic("The Medic", 15, 2, 15, None, None, None, None)
shadowBen = Shadow("The Shadow", None , 3, None, 10, None, None, None, None)

dwarfEric = Dwarf("The Dwarf", 20, 3, 20, None)
goblinAnuj = Goblin("The Goblin", 13, 2, 6, None)
zombiePhong = Zombie("The Zombie", 5,1, 5, None)

healTonic = Tonic(None, None, None)
beginArmor = Armor(None, None, None)
beginWeap = Weapon(None, None, None)
beginBomb = Bomb(None, None, None)

beginStore = Store(healTonic, beginArmor, beginWeap, beginBomb)


# print(knightMatt.coinbag)
# GameInteraction.shopInt(medicRay,beginStore)

GameInteraction.monsterInt(shadowBen, dwarfEric)
GameInteraction.shopInt(shadowBen, beginStore)
GameInteraction.monsterInt(shadowBen, goblinAnuj)



#regeneration test
# health = 15
# originalHealth = 15

# while health > 0:
#     health -= 3
#     if health < originalHealth:
#         if random.randint(1,5) == 5:
#             health += 2
#     print(health)
#     break

#iterate through inventory list
# raw_input = input()
# for i in range(len(heroErick.backpack)):
#     if raw_input == str(len(heroErick.backpack)) :
#         print(heroErick.health)

