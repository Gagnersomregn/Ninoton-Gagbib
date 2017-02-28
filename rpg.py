import sys
import os
import time
import random
# New test HIHI
####################Classes#####################################
weapons = {"Big Sword": 40}
#------------- Player class--------------
class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10
        self.gold = 40
        self.pots = 1
        self.activeweap = "Bad Sword"
        self.curweap = ["Bad Sword"]
    @property
    def attack(self):
        attack = self.base_attack
        if self.activeweap == "Bad Sword":
            attack += 10
        elif self.activeweap == "Big Sword":
            attack += 20
        return attack

#------------Goblin class-------------
class Goblin:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 105
        self.health = self.maxhealth
        self.attack = 16
        self.goldgain = 10
GoblinIG = Goblin("Goblin")
#------------Orc class------------------
class Orc:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 95
        self.health = self.maxhealth
        self.attack = 18
        self.goldgain = 10
OrcIG = Orc("Orc")

########################################################
##################main menu#############################
def main():
    #os.system("cls")
    print("Welcome to my game!\n")
    print("1: start")
    print("2: load")
    print("3: exit")
    option = input("->")
    #option = eval(input("->"))#-----string problemet, fixa...
    if option == "1":
        start()
    elif option == "2":
        pass
    elif option == "3":
        sys.exit()
    else:
        print("error! try again")
        time.sleep(2)
        main()
# # # # # # # #  #  # # # # # # # # #  # # # # # # # #

#players name?
def start():
    #os.system('cls')
    print("Hello, what is your name?")
    option = input("->")
    global PlayerIG
    PlayerIG = Player(option)
    start1()
##greeting and menu
def start1():
    #os.system("cls")
    print("Hello, " + PlayerIG.name + ". Wazzup?!\n")
    print("-----------------------------------------")
    print("/Your stats:                            /")
    print("/Attack: %i                             /" % PlayerIG.attack)
    print('/Health: %i / %i                      /' % (PlayerIG.health, PlayerIG.maxhealth))
    print("/Gold: %i                               /" % PlayerIG.gold)
    print("/Pots: %i                                /" % PlayerIG.pots)
    print("/Weapons: %s                 /" % PlayerIG.curweap)
    print("-----------------------------------------")
    time.sleep(2)
    print(".")
    time.sleep(0.6)
    print(".")
    time.sleep(0.4)
    print(".")
    print("Please choose an option:")
    print("1) fight")
    print("2) store")
    print("3) save")
    print("4) exit to main menu")
    option = input("-->")
    if option == '1':
        preFight()
    elif option == '2':
        store()
    elif option == '3':
        print("esave")
        #save()
    elif option == '4':
        print("main")
        main()
    else:
        print("error!, lets try again! ")
        time.sleep(2)
        start1()
#generate enemy
def preFight():
    os.system('cls')
    global enemy
    enemynum = random.randint(1, 2)
    if enemynum == 1:
        print("You're facing the Goblin Bitch ")
        enemy = GoblinIG
    else:
        print("You're facing the Orc Bitch ")
        enemy = OrcIG
    option = input("Enter to continue")
    fight()
#fight
firstTime = "true"
def fight():
    #os.system('cls')
    print("--------------------------------------------------------------")
    print("~~~~~%s                  VS                 %s~~~~~" %(PlayerIG.name, enemy.name ))
    print("%s's health: %d / %d         %s's health: %i / %i" %(PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth))
    print("Equipped weapon: %s" % PlayerIG.activeweap)
    print("potions: %i" % PlayerIG.pots)
    print("--------------------------------------------------------------")

    if firstTime == "true":
        for remaining in range(3, 0, -1):
            print("Fight starting in: {:2d}".format(remaining))
            time.sleep(1)
        print("GOO!!\n\n")
    global firstTime
    firstTime = "false"
    print("Attack:          1")
    print("Take pot:        2")
    print("Run:             3")
    print("Equip weapon:    4")
    option = input("-->")
    if option == "1":
        attack()
    elif option == "2":
        potion()
    elif option == "3":
        run()
    elif option == "4":
        newweap()
    else:
        print("oops! can't do that")
        time.sleep(1)
        fight()

def newweap():
    #os.system('cls')
    print("Choose one of these weapons")
    print("Bad Sword:         1")
    print("Big Sword:         2")
    option = input("-->")
    if option == "1":
        PlayerIG.activeweap = PlayerIG.curweap[0]
    elif option == "2":
        PlayerIG.activeweap = PlayerIG.curweap[1]
    else:
        print("Try again")
    print("you have chosen %s" % PlayerIG.activeweap)
    option = input('press enter to continue')
    fight()

def attack():
    #os.system('cls')
    PAttack = random.randint(PlayerIG.attack / 2, PlayerIG.attack)
    EAttack = random.randint(enemy.attack / 2, enemy.attack)
    if PAttack == PlayerIG.attack / 2:
        print("Boom you miss!")
    else:
        enemy.health -= PAttack
        print("Daaamn son! you dealt %i DMG" % PAttack)
    option = input('press enter to continue the fight')
    if enemy.health <= 0:
        win()
    os.system('cls')
    if EAttack == enemy.attack / 2:
        print("Enemy missed you!")
    else:
        PlayerIG.health -= EAttack
        print("Shiet! enemy dealt %i DMG" % EAttack)
    option = input('press enter to continue the fight')
    if PlayerIG.health <= 0:
        dead()
    else:
        fight()

def potion():
    #os.system('cls')
    if PlayerIG.pots == 0:
        print("No pots")
    else:
        PlayerIG.health += 15
        if PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
        if PlayerIG.pots > 1:
            PlayerIG.pots -= 1
        else:
            PlayerIG.pots = 0
        print("You drank a pot")
    option = input('press enter to continue')
    fight()

def run():
    #os.system('cls')
    runnum = random.randint(1, 3)
    if runnum == 1:
        print("you ran away!")
        time.sleep(1)
        option = ('Press enter')
        start1()
    else:
        print("you couldn't run")
        option = ('Press enter')
        os.system('cls')
        ## back to enemy attacks you
        EAttack = random.randint(enemy.attack / 2, enemy.attack)
        if EAttack == enemy.attack / 2:
            print("Enemy missed you!")
        else:
            PlayerIG.health -= EAttack
            print("Shiet! enemy dealt %i DMG" % EAttack)
        option = input('press enter to continue the fight')
        if PlayerIG.health <= 0:
            dead()
        else:
            fight()
def win():
    #os.system('cls')
    #reset health for next match
    enemy.health = enemy.maxhealth
    PlayerIG.health = PlayerIG.maxhealth
    #loot gold after winning
    PlayerIG.gold += enemy.goldgain
    print("¨*¨*¨*¨*¨* you have won against %s ¨*¨*¨*¨*¨*¨" % enemy.name)
    print("Loot: %i gold. Good Job!!" % enemy.goldgain)
    option = input('Enter to continue')
    start1()
def dead():
    ##when you die, the program shuts down
    os.system('cls')
    print("You are dead")
    option = input("Press enter")
    sys.exit()
#store - still need to add buying option for pots
def store():
    #os.system('cls')
    print("Welcome to the store!")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("Gold left: %i" % PlayerIG.gold)
    print("Choose what u wanna buy below:")
    print("1: For Big Sword(40 g),    type 'Big Sword'")
    print("2: Health Pot(10 g),       press 2")
    print("More weapons:        coming soon..")
    print("Back to main menu,   press 3")
    option = input(' ')
    if option == '3':
        start1()
    if option in weapons:
        if PlayerIG.gold >= weapons[option]:
            #os.system('cls')
            PlayerIG.gold -= weapons[option]
            PlayerIG.curweap.append(option)
            print('you have purchased: %s' % option)
            option = input("Press enter")
            store()
        else:
            #os.system('cls')
            print("Not enough gold!!")
            option = input("Press enter")
            store()
    if option == '2':
        if PlayerIG.gold >= 10:
            PlayerIG.pots += 1
            PlayerIG.gold -= 10
            print("you have purchased one health potion")
            option = input("Press enter")
            store()
        else:
            #os.system('cls')
            print("Not enough gold!!")
            option = input("Press enter")
            store()
    else:
        print('No such item!\n')
        option = input("Press enter to go back to store")
        store()
def save():
    #os.system('cls')
    Player

    pass
#call main
main()