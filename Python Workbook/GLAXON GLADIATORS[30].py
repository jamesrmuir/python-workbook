#Glaxon Gladiators 
#TODO:
#Change force field indecator to enum
#Deal with when there is no weapons left (a draw)
#High score tables
#Put game in loop
#Make it pretty 
#
#

#Importing modules 
import random 

#Player class
class player:
    def PurchaseItems():
        global items
        global playerCredits
        global playerItems
        
        print("Welcome to the Glaxon robot gladiator store. \nYou have %s credits remaining." %playerCredits)  
        print("Here are your options: ")
        print()
        print("ID, Name, Cost, Damage")
        ListItems(items)
        print("Remember each item is one use only")
        print("Note the force field will not protect againt a nuke only a hydrogen force field will.")
        
        while playerCredits > 0:
            print("Please enter the number of the item you want to buy.")
            try:
                playerInput = int(input("Enter number: "))
            except ValueError:
                print("Enter a numerical value") 
            player.BuyItem(playerInput)

        #playerItems = playerItems.sort()

    def BuyItem(itemId):
        global items
        global playerCredits
        global playerItems

        try:
            #Check Player has enough credit for item
            if playerCredits < items[itemId][2]:
                print("Sorry you do not have enough credits left")
            else:
                playerCredits = playerCredits - items[itemId][2]
                playerItems.append(items[itemId][0])
                print("You have just bought %s" %items[itemId][1])
                print("You have %s credits remaining" %playerCredits)
                print()
                
        except IndexError:
            print("Enter a number between 0 and 5.")

    def ListItems(itemList):
        for i in itemList:
            print(items[i])
        
    def Attack():
        global aiHealth
        global aiForcefield
        global playerHealth
        global playerItems
        
        print()
        print("Here are your items: ")
        player.ListItems(playerItems)
        print("Please select an item to use once you use it it will be removed.")
        print()
        while True:
            try:
                userChoice = int(input("Select the ID of the item you want to use: "))
            except ValueError:
                print("Enter a numerical value")
            try:
                playerItems.remove(userChoice)
                if aiForcefield == 0:
                    if userChoice == 0:
                        aiHealth -= 1
                        print("Power punch used.")
                    elif userChoice == 1:
                        aiHealth -= 3
                        print("Heatmissile used.")
                    elif userChoice == 2:
                        aiHealth -= 7
                        print("Plasma punch used.")
                    elif userChoice == 3:
                        playerForcefield = 1
                        print("Standard force field active.")
                    elif userChoice == 4:
                        playerForcefield = 3
                        print("Hydrogen force field active.")
                if userChoice == 5:
                    if aiForcefield == 0 or aiForcefield == 1: 
                        aiHealth -= 10
                        print("Tactical nuke inbound.")
                print()
                break
            except:
                print("You do not have that item.")
                print("")

        return 0

        
#AI class
class ai:
    def PurchaseItems():
        global aiCredits
        
        while aiCredits > 0:
            ai.BuyItem(random.randint(0,5))

    def BuyItem(itemId):
        global items
        global aiCredits
        global aiItems

        try:
            #Check Player has enough credit for item
            if aiCredits < items[itemId][2]:
                pass
            else:
                aiCredits = aiCredits - items[itemId][2]
                aiItems.append(items[itemId][0])
                
        except IndexError:
            print("Enter a number between 0 and 5.")
            pass

    def Attack():
        global playerHealth
        global playerForcefield
        global aiItems
        global aiForcefield
        while True:
            randomInt = random.randint(0,5)
            try:
                aiItems.remove(randomInt)
                if playerForcefield == 0:
                    if randomInt == 0:
                        playerHealth -= 1
                    elif randomInt == 1:
                        playerHealth -= 3
                    elif randomInt == 2:
                        playerHealth -= 7
                    elif randomInt == 3:
                        aiForcefield = 1
                    elif randomInt == 4:
                        aiForcefield = 3
                        
                if randomInt == 5:
                    if playerForcefield == 0 or playerForcefield == 1:
                        playerHealth -= 10
                break
            except:
                pass

            
#Start up script
def StartUp():
    global aiCredits
    global aiItems
    global playerHealth
    global aiHealth
    
    print("Welcome to Glaxon Gladiators")
    print("You must kit out a battle robot to fight the Glaxon robot")
    print()
    player.PurchaseItems()
    ai.PurchaseItems()
    print(aiCredits)
    print(aiItems)
    print(playerCredits)
    print(playerItems)
    print("Now you will fight...")

    #Game Loop
    while True:
        player.Attack()
        ai.Attack()
        if playerHealth < 0:
            print("The galxon wins.")
            break
        if aiHealth < 0:
            print("The player wins.")
            break
        if len(playerItems) <= 0:
            print("The galxon wins.")
            break
        if len(aiItems) <= 0:
            print("The player wins.")
            break



        AdvanceRound()
    #EndGame()
            
    

#Fucntion which will print out the items in the inventory and format them - WIP
def ListItems(itemList):
    global items
    for row in itemList:
    # Loop over columns.
        for column in row:
            print(column, end=" ")
        print(end="\n")

def AdvanceRound():
    global currentRound
    global playerHealth
    global aiHealth
    global playerForcefield
    global aiForcefield

    
    currentRound += 1
    print()
    print("The player has {} health remaining and the Glaxon has {}.".format(playerHealth, aiHealth))
    print()
    print("You have the following items remaining")
    player.ListItems(playerItems)
    print()

    if playerForcefield == 1:
        playerForcefield = 0
    elif playerForcefield == 2:
        playerForcefield = 3
    elif playerForcefield == 3:
        playerForcefield = 0

    if aiForcefield == 1:
        aiForcefield = 0
    elif aiForcefield == 2:
        aiForcefield = 3
    elif aiForcefield == 3:
        aiForcefield = 0
    
#Variable for repeating
repeating = True
#Items
#ID, Name, cost, damage,     
items = [
    [0, "Power Punch", 1, 1],
    [1, "Heat Missile", 2, 3],
    [2, "Plasma Punch", 4, 7],
    [3, "Force Field", 2, 10],
    [4, "Hydrogen Force Field", 3, 0],
    [5, "Nuke", 16, 30]
]

playerCredits = 20
playerItems = []
aiCredits = 20
aiItems = []
playerHealth = 10
aiHealth = 10
#0 for none, 1 for standard, 2 for hydrogen 2 turns left and 3 for hydrogen 1 turn left
playerForcefield = 0
aiForcefield = 0
currentRound = 0


#Start of program
StartUp()

