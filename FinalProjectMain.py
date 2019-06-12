# Name: Ranvir Singh
# Date: March 20th, 2019
# File Name: Main.py AKA Monopoly
# Description: This program allows for the user to play monopoly with as many different AI players as they want or with
# other human players taking turns on the terminal, the user can set their own difficulty settings, choose their own
# names, if playing against AI depending on the level of difficulty the AI will choose card sets and play different
# tactics to win against the human player, the user has access to all the typical parts of monopoly community chests,
# chance cards, buy properties and can even modify game rules from a set of different changes they can  choose what to
# for example they can choose to add a upper limit to the amount of money earned and whoever reaches there first wins.

# todo
# add try and except to everything
# Create a hotel and apartments function 
import time
import random

# A list of all the properties the user can land on
property = ["Go", "Mediterranean Ave", "Community Chest", "Baltic Ave", "Income Tax", "Reading Railroad",
            "Oriental Ave", "Chance", "Vermont Ave", "Connecticut Ave", "jail/Just Visiting", "St. Charles Place",
            "Electric Company", "States Ave", "Virginia Ave", "Pennsylvania Railroad", "St. James Place",
            "Community Chest", "Tennessee Ave", "New York Ave", "Free Parking", "Kentucky Ave", "Chance",
            "Indiana Ave", "Illinois Ave", "B. & O. Railroad", "Atlantic Ave", "Ventnor Ave", "Water Works",
            "Marvin Gardens", "Go to Jail", "Pacific Ave", "North Carolina Ave", "Community Chest",
            "Pennsylvania Ave", "Short Line Railroad", "Chance", "Park Place", "Luxury Tax", "Boardwalk"]

# a corresponding index list of all the property prices
propertyPrice= [
    200, 60, 0, 60,100, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160,200, 180, 0,180, 200, 0, 220, 0, 220, 240,
    200, 260, 260, 150, 280, 0, 300, 300, 0, 320, 200, 0, 350, 300, 400
]
# another corresponding index list of all property colors 
propertyColor = [
    "None", "Brown", "None", "Brown", "None", "None", "Navy", "None", "Navy", "Navy", "None", "Pink", "None", "Pink", "Pink", "None", "Orange", 
    "None", "Orange", "Orange", "None", "Red", "None", "Red", "Red", "None", "Yellow", "Yellow", "None", "Yellow", "None", "Green", "Green", "None",
    "Green", "None", "None", "Blue", "None", "Blue"    
]
# all the chance cards and Community chest cards
chanceCards = ["Advance to Go (Collect $200)", "Advance to Illinois Ave",
               "Advance to St. Charles Place – If you pass Go, collect $200", "Bank pays you dividend of $50", "Get Out of Jail Free", "Go Back 3 Spaces",
               "Go to Jail","Pay poor tax of $15", "Take a trip to Reading Railroad",
               "Take a walk on the Boardwalk", "You have been elected Chairman of the "
                                                                          "Board–Pay each player $50",
               "Your building and loan matures—Collect $150", "You have won a crossword competition—Collect $100"]

CommunityChest = ["Advance to Go (Collect $200)", "Bank error in your favor—Collect $200", "Doctor's fee—Pay $50",
                  "From sale of stock you get $50", "Get Out of Jail Free", "Go to Jail–Go directly to jail–Do "
                                                                            "not pass Go–Do not collect $200",
                  "Grand Opera Night—Collect $50 from every player for opening night seats", "Holiday Fund matures—"
                                                                                             "Receive $100",
                  "Income tax refund–Collect $20", "It is your birthday—Collect $10", "Life insurance matures–Collect "
                                                                                      "$100",
                  "Pay hospital fees of $100", "Pay school fees of $150", "Receive $25 consultancy fee",
                "You have won second prize in "
                "a beauty contest–Collect $10",
                "You inherit $100"]


# Back end function that dont directly affect gameplay 
# Allows for access to the settings file and drops values into a list
settings = []
with open("settings.txt") as file:
    for line in file:
        line = line.split(":")
        line = line[1]
        line = line.rstrip("\n")
        line = line[1:]
        line = line.split(" ")
        try:
            for x in range(len(line)):
                line[x] = int(line[x])
            line = (line[0], line[1])
        except:
            line = line[0]
            settings.append(line)
file.close()

# Error checking for inputs file stored as a function


def inputs(line, typeinp=None, start=None, end=None):
    while True:
        string = input(line)
        if typeinp != None:
            try:
                if typeinp == "string":
                    string = str(string)
                elif typeinp == "integer":
                    string = int(string)
                if start != None and end != None:
                    while not (string >= start and string <= end):
                        print("Please input a number between", str(start) + "-" + str(end))
                        string = int(input(line))
                break
            except:
                print("Please input a", typeinp)
        else:
            break
    return string

# A list of commands for the player and AI if they land on a chance/community chest card
def chance_community():
    if property[player_update] == "Chance":
        if chanceCards.index(ChanceCardPick) == 0:
            players[PlayerTurn]["PlayerLocation"] = 0
            money = int(players[PlayerTurn]["money"])
            money += 200
            players[PlayerTurn]["money"] = money
            print("You were moved back to go and gained $200")
        elif chanceCards.index(ChanceCardPick) == 1:
            ill = property.index("Illinois Ave") 
            
            players[PlayerTurn]["PlayerLocation"] = ill
            print("You are now on Illinois Ave")
        elif chanceCards.index(ChanceCardPick) == 2:
            cill = property.index("St. Charles Place")
            players[PlayerTurn]["PlayerLocation"] = ill
            print("You are now on St. Charles Place")
        elif chanceCards.index(ChanceCardPick) == 3:
            money = int(players[PlayerTurn]["money"])
            money += 50
            players[PlayerTurn]["money"] = money
            print("You earned $50")
        elif chanceCards.index(ChanceCardPick) == 4:
            if players[PlayerTurn]["Getoutajail"] == True:
                print("You already have a get outa jail free card so no more for you..")
            elif players[PlayerTurn]["Getoutajail"] == False:
                players[PlayerTurn]["Getoutajail"] = True
                print("You now own a get out of jail free card")
        elif chanceCards.index(ChanceCardPick) == 5:
            players[PlayerTurn]["PLayerLocation"] -= 3
            print("You Got moved back 3 spaces")
        elif chanceCards.index(ChanceCardPick) == 6:
            players[PlayerTurn]["inJail"]= True
            players[PlayerTurn]["PlayerLocation"] = 10
            print("Oh no you are now in jail")
        elif chanceCards.index(ChanceCardPick) == 7:
            money = int(players[PlayerTurn]["money"])   
            money -= 15
            players[PlayerTurn]["money"] = money
        elif chanceCards.index(ChanceCardPick) == 8:
            players[PlayerTurn]["PlayerLocation"] = 5
            print("You went to reading railroad")
        elif chanceCards.index(ChanceCardPick) == 9:
            bord = property.index("Boardwalk")
            players[PlayerTurn]["PlayerLocation"] = bord
            print("You went to Boardwalk")
        elif chanceCards.index(ChanceCardPick) == 10:
            count = 0
            for pp in range(len(players)):
                money = players[pp]["money"]
                money +=50
                count +=1
            moneylost = (50 * count) -50
            players[PlayerTurn]["money"] -= moneylost
            print("You paid everyone $50") 
        elif chanceCards.index(ChanceCardPick) == 11:
            money = players[PlayerTurn]["money"]
            money +=150
            players[PlayerTurn]["money"] = money
            print("You made $150")
        elif chanceCards.index(ChanceCardPick) == 12:
            money = players[PlayerTurn]["money"]
            money +=100
            players[PlayerTurn]["money"] = money
            print("You made $100")

    elif property[player_update] == "Community Chest":
        if CommunityChest.index(ChanceCardPick) == 0:
            players[PlayerTurn]["PlayerLocation"] = 0
            money = int(players[PlayerTurn]["money"])
            money += 200
            players[PlayerTurn]["money"] = money
            print("You were moved back to go and gained $200")
        elif CommunityChest.index(ChanceCardPick) == 1:
            money = int(players[PlayerTurn]["money"])
            money += 200
            print("You made $200")
            players[PlayerTurn]["money"] = money
        elif CommunityChest.index(ChanceCardPick) == 2:
            money = int(players[PlayerTurn]["money"])
            money += 50
            players[PlayerTurn]["money"] = money
            print("You paid $50")
        elif CommunityChest.index(ChanceCardPick) == 3:
            money = int(players[PlayerTurn]["money"])
            money += 50
            players[PlayerTurn]["money"] = money
            print("You earned $50")
        elif CommunityChest.index(ChanceCardPick) == 4:
            if players[PlayerTurn]["Getoutajail"] == True:
                print("You already have a get outa jail free card so no more for you..")
            elif players[PlayerTurn]["Getoutajail"] == False:
                players[PlayerTurn]["Getoutajail"] = True
                print("You now own a get out of jail free card")
        elif CommunityChest.index(ChanceCardPick) == 5:
            players[PlayerTurn]["inJail"]= True
            players[PlayerTurn]["PlayerLocation"] = 10
            print("Oh no you are now in jail")
        elif CommunityChest.index(ChanceCardPick) == 6:
            count = 0
            for pp in range(len(players)):
                money = players[pp]["money"]
                money -=50
                count +=1
            moneyGain = (50 * count) +50
            players[PlayerTurn]["money"] -= moneyGain
            print("You got $50 from everyone") 
        
        elif CommunityChest.index(ChanceCardPick) == 7:
            money = int(players[PlayerTurn]["money"])   
            money += 100
            print("You made $100")
            players[PlayerTurn]["money"] = money
        elif CommunityChest.index(ChanceCardPick) == 8:
            money = int(players[PlayerTurn]["money"])   
            money += 20
            print("You made $20")
            players[PlayerTurn]["money"] = money
        elif CommunityChest.index(ChanceCardPick) == 9:
            money = int(players[PlayerTurn]["money"])   
            money += 10
            print("You made $10")
            players[PlayerTurn]["money"] = money
        elif CommunityChest.index(ChanceCardPick) == 10:
            money = int(players[PlayerTurn]["money"])   
            money += 100
            print("You made $100")
            players[PlayerTurn]["money"] = money
            money = players[PlayerTurn]["money"]
        elif CommunityChest.index(ChanceCardPick) == 11:
            money -=150
            print("You paid $150")
            players[PlayerTurn]["money"] = money
        elif CommunityChest.index(ChanceCardPick) == 12:
            money = players[PlayerTurn]["money"]
            money +=25
            print("You made $25")
            players[PlayerTurn]["money"] = money
        elif CommunityChest.index(ChanceCardPick) == 13:
            money = players[PlayerTurn]["money"]
            money +=10
            print("You made $10")
            players[PlayerTurn]["money"] = money
        elif CommunityChest.index(ChanceCardPick) == 14:
            money = players[PlayerTurn]["money"]
            money +=100
            print("You made $100")
            players[PlayerTurn]["money"] = money

# A function that clears the screen for users when the next player comes on
def playerChange():
    print("Next Player")
    print("***************************************")
    print("*")
    print("*")
    print("*")
    print("*")
    print("***************************************")
    return

# A game settings file that allows the user to setup their game to their liking
def gameSettingsSetup():
    settingsCheck = open("settings.txt", "r")
    print("Lets setup")
    # Int Setup questions
    numPlayers = str(inputs('How many real players are playing: ', "intger", 1, 10))
    AIEnabled = input("Would you like to enable Ai players for this game? ")
    while True:    
        if AIEnabled == "y" or "Y":
            startingMoney = str(inputs("How much money does everyone start with? Max: 10 000 (Keep in mind "
                                    "this does not affect the property prices) ", "integer", 100, 10000))
            for i in range(int(numPlayers)):
                name = input("What is the players name? ")
                players.append({"playerName": name, "money":startingMoney, "properties": [], "railroads": []})
                break
        elif AIEnabled == "n" or "N":
            startingMoney = str(inputs("How much money does everyone start with? Max: 10 000 (Keep in mind "
                                    "this does not affect the property prices) ", "integer", 100, 10000))
            for i in range(int(numPlayers)):
                name = input("What is the players name? ")
                players.append({"playerName": name, "money":startingMoney, "properties": [], "railroads": []})
            break
        else:
            print("Please enter either y or n")
            AIEnabled = input("Would you like to enable Ai players for this game? ")

    print("Alright the setup is complete, Your game will start now....")
    time.sleep(1)

    # sends over the settings into the text file as well as monoset check
    if "MonoSet1-1" in settingsCheck.read():
        with open("settings.txt", "w") as file:
            file.write("MonoSet1-1: true" + "\n")
            file.write("numPlayer: " + numPlayers + "\n")
            file.write("numAIplayer: " + AIEnabled + "\n")
            file.write("startingMoney: " + startingMoney + "\n")
            file.close()

    return settingsCheck, players


# Picks a random card from the chance lists
def chancePickUp():
    cardPick = random.randint(0, 12)
    return chanceCards[cardPick]
 
# Picks a random card from the community chest lists

def communityPickUp():
    cardPick = random.randint(0, 13)
    return CommunityChest[cardPick]
# emmulates the dice roll 
def dice_roll():
    snakeEyes = False
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 == die2:
        snakeEyes = True
    total = die1 + die2
    return die1, die2, total, snakeEyes

def is_property_owned(property_name):
    for p in players:
        if property_name in p['properties']:
            return p['playerName']  # Returns the owner of property
        else:
            for a in aiPlayerList:
                if property_name in a['properties']:
                    return a['AiName']  # Returns the owner of property
    return None

def buy_rand():
    buyEasy = random.randint(0, 1)
    return buyEasy

# AI EASY FULL PROGRAM
aiPlayerList = []
propLoc = 0
for PlayerAi in range(settings[2]):
    aiPlayerList.append(
        {
        "AiName": PlayerAi,
        "money": settings[4],
        "properties": [],
        "Colors": [],
        "railroads": [],
        "inJail":   False,
        "PlayerLocation": propLoc,
        "Getoutajail": False
         }
    )

# AI program
def Ai_easy():
    ChanceCardPick = chancePickUp()
    CommunityCardPick = communityPickUp()
    print("The Ai is going now please wait....")
    time.sleep(1)
    BigBoi = "(ง ͠° ͟ل͜ ͡°)ง"
    for a in range(settings[2]):
        money = int(aiPlayerList[0]["money"])
        if money > 50: 
            buyEasy = buy_rand()
            die1, die2, total, snakeEyes = dice_roll()
            AD = property.index(property[total])
            if AD > 40:
                newLoop = AD - 40
                AD = 0 + newLoop
                aiPlayerList[PlayerTurn]["PlayerLocation"] += AD
                AI_update = aiPlayerList[PlayerTurn]["PlayerLocation"]
                print("You passed go and collected $200")
                money = int(aiPlayerList[PlayerTurn]["money"])
                money += 200
                aiPlayerList[0]["money"] = money
            elif AD < 40:
                aiPlayerList[0]["PlayerLocation"] += AD
                AI_update = aiPlayerList[0]["PlayerLocation"]

            propertycheck = is_property_owned(property[AI_update])
            if property[total] != "Chance":
                if property[total] != "Community Chest":
                    if property[total] != "jail/Just Visiting":
                        if property[total] != "Income Tax" and property[total] != "Luxury Tax":
                            if buyEasy == 1:
                                if propertycheck == None:
                                        aiPlayerList[a]["properties"].append(property[AI_update])
                                        aiPlayerList[a]["Colors"].append(propertyColor[AI_update])
                                        print("The Computer rolled a", die1,"and a", die2, "and landed on", property[AI_update], "and bought it")  
                                        if snakeEyes == True:
                                                print("The computer also got Snake eyes! and gets to roll again")   
                                                die1, die2, total1, snakeEyes = dice_roll()
                                                buyEasy = buy_rand()
                                                if buyEasy == 1: 
                                                        if propertycheck == None: 
                                                                aiPlayerList[a]["properties"].append(property[AI_update+total1])
                                                                aiPlayerList[a]["Colors"].append(propertyColor[AI_update+total])
                                                                aiPlayerList[a]["PlayerLocation"] = AI_update+total
                                                                print("The Computer rolled a", die1,"and a", die2, "and landed on", property[AI_update+total], "and bought it")  
                                                        elif propertycheck != None:
                                                                print("The Computer rolled a", die1,"and a", die2, "and landed on", property[AI_update], "which is owned by", propertycheck)
                                                                for i in range(len(players)):
                                                                    if propertycheck in players[i]["playerName"]:
                                                                        propOwn = players[i]
                                                                rentValue = propertyPrice[AI_update] * 0.60
                                                                money = int(aiPlayerList[0]["money"])
                                                                money -= rentValue
                                                                aiPlayerList[0]["money"] = money
                                                                moneyErn = int(propOwn["money"])
                                                                moneyErn +=rentValue
                                                                propOwn["money"] = int(moneyErn)
                                                                print("The bot paid rent to ", propOwn["playerName"], "of a total of", rentValue)
                                                elif buyEasy == 0:
                                                        aiPlayerList[0]["PlayerLocation"] = AI_update 
                                                        print("The Computer rolled a", die1,"and a", die2, "and landed on", property[AI_update], "and did not buy it")
                                elif propertycheck != None:
                                    print("The Computer rolled a", die1,"and a", die2, "and landed on", property[AI_update], "which is owned by", propertycheck)
                                    for i in range(len(players)):
                                        if propertycheck in players[i]["playerName"]:
                                                propOwn = players[i]
                                        rentValue = propertyPrice[AI_update] * 0.60
                                        money = int(aiPlayerList[0]["money"])
                                        money -= rentValue
                                        aiPlayerList[0]["money"] = money
                                        moneyErn = int(propOwn["money"])
                                        moneyErn +=rentValue
                                        propOwn["money"] = int(moneyErn)
                                        print("The bot paid rent to ", propOwn["playerName"], "of a total of", rentValue)   
                            elif buyEasy == 0:
                                        aiPlayerList[a]["PlayerLocation"] = AI_update 
                                        print("The Computer rolled a", die1,"and a", die2, "and landed on", property[AI_update], "and did not buy it") 
                        # If the AI lands on the Income Tax then it will be deducted from their account
                        elif property[total] == "Income Tax":
                            print("The bot had to pay income tax of $200")
                            money = int(aiPlayerList[0]["money"])
                            money -= 200
                            aiPlayerList[0]["money"] = money
                        # If the AI lands on the luxury tax then it will be deducted from their account
                        elif property[total] == "Luxury Tax":
                            print("The bot had to pay Luxury Tax of $200")
                            money = int(aiPlayerList[0]["money"])
                            money -= 200
                            aiPlayerList[0]["money"] = money
                    elif property[total] == "jail/Just Visiting":
                        print("The Bot landed on Jail/ Just Visiting")
                elif  property[total] == "Community Chest":
                    print("The Computer rolled a", die1,"and a", die2, "and landed on", property[AI_update], "the card states", CommunityCardPick) 
                elif property[total] == "Income Tax":
                    print("The Computer rolled a", die1,"and a", die2, "landed on", property[AI_update], "and had to pay", propertyPrice[AI_update])
                    money = int(aiPlayerList[a]["money"])
                    money -= propertyPrice[total]
                    aiPlayerList[0]["money"] = money 
            elif property[total] == "Chance":
                print("The Computer rolled a", die1,"and a", die2, "and landed on", property[AI_update], "the card states", CommunityCardPick) 
        elif money < 50:
            print("The Ai ran out of money and is forfiting")
            aiPlayerList.remove(0)

# A summary of all the player information
def playerInfo():
    print("\nName:", players[PlayerTurn]["playerName"] )
    print("Money:", players[PlayerTurn]["money"])
    print("Properties:")
    for u in range(len(players[PlayerTurn]["properties"])):
        print(u+1, players[PlayerTurn]["properties"][u])

    if players[PlayerTurn]["inJail"]:
        print("You are in jail")
    else: 
        print("You are not in jail")
    if players[PlayerTurn]["Getoutajail"]:
        print("You have a Get out of jail card")
    else:
        print("you have no get out of jail card \n")     

# The main player list which will cointain all the player information
players = []

# Intro
settingsCheck = open("settings.txt", "r")
print("Hello! Welcome to the game of monopoly, Terminal version before we can start we have to make sure "
      "everything is set up properly... \n")
time.sleep(2)
# Settings check, checks if a settings file exists and if so checks if the user wants to use them. s
importSetyn = input("You have saved settings in you setting file, would you like to use them? (y or n): ")
if "MonoSet1-1" in settingsCheck.read():
    while True:
        if importSetyn == "y" or importSetyn == "Y":
            print("Alright lets start your game... ")
            time.sleep(1)
            players = []
            for i in range(int(settings[1])):
                name = input("What is the players name? ")

                players.append(
                    {
                    "playerName": name,
                    "money": settings[4],
                    "properties": [],
                    "Colors": [],
                    "APTS": [],
                    "Hotels": [],
                    "inJail":   False,
                    "PlayerLocation": 0,
                    "Getoutajail": False
                    }
                )
            break
        elif importSetyn == "n" or importSetyn == "N":
            time.sleep(1)
            gameSettingsSetup()
            break
        else:
            print("Invalid Input")
            importSetyn = input("You have saved settings in you setting file, would you like to use them? "
                                "(y or n): ")
elif "" in settingsCheck.read(1):
    print("You dont have any saved settings lets fix that.....")
    gameSettingsSetup()
else:
    print("Your setting file seems to be corrupted please either remove any random text or delete the file...")



# Main code, a for loop for all the real players
PlayerTurn = 0
while True: 
    money = int(players[PlayerTurn]["money"])
    if money > 50:
        playerInfo()
        print("It is now", players[PlayerTurn]["playerName"]+ "'s", "turn \n")
        print("1. Roll (rolls the dice)")
        print("2. Skip (skips turn to the next person)")
        print("3. Mortgage Property (Mortgage the property to get some money back)")
        print("4. Post Bail (only works if you are in jail and have the money to pay)")
        print("5. Quit game")
        playerAction = inputs("Please enter your action: ", "integer", 1, 7)
        
        if playerAction == 1 :
           while True: 
                if players[PlayerTurn]["inJail"] == False: 
                        die1, die2, total, snakeEyes = dice_roll()
                        # Calls either chance or community function to pick a random card and give it to the player
                        ChanceCardPick = chancePickUp()
                        CommunityCardPick = communityPickUp()
                        # property owned check, sees if anyone owns the property and returns either none or the playerName
                        time.sleep(1)
                        pd = property.index(property[total])
                        if pd > 40:
                            newLoop = pd - 40
                            pd = 0 + newLoop
                            players[PlayerTurn]["PlayerLocation"] += pd
                            player_update = players[PlayerTurn]["PlayerLocation"]
                            print("You passed go and collected $200")
                            money = int(players[PlayerTurn]["money"])
                            money += 200
                            players[PlayerTurn]["money"] = money
                        elif pd < 40:
                            players[PlayerTurn]["PlayerLocation"] += pd
                            player_update = players[PlayerTurn]["PlayerLocation"]

                        print("You rolled a", die1, "and a", die2, "you move forward",total, "steps \n")
                        time.sleep(1)
                        print("You landed on", property[player_update] + "\n")
                        time.sleep(1)
                        if property[player_update] == "Community Chest" or property[player_update] == "Chance":
                            if property[player_update] == "Community Chest":
                                print("The card you picked states", CommunityCardPick, "\n")
                                chance_community()
                                if PlayerTurn == settings[1]-1:
                                        print("It is now the Ai's turn")
                                        playerChange()
                                        Ai_easy()
                                        PlayerTurn = 0
                                elif PlayerTurn < settings[1]:
                                        PlayerTurn +=1
                                        playerChange()

                            elif property[player_update] == "Chance":
                                print("The card you picked states", ChanceCardPick)
                                chance_community()
                                if PlayerTurn == settings[1]-1:
                                        print("It is now the Ai's turn")
                                        playerChange()
                                        Ai_easy()
                                        PlayerTurn = 0
                                elif PlayerTurn < settings[1]:
                                        PlayerTurn +=1
                                        playerChange()
                            else:
                                print("Something went wrong, sorry")
                        elif property[player_update] != "Community Chest":
                            # checks if the user landed on income tax and will deduct it from their money
                            if property[player_update] == "Income Tax":
                                    print("You have to pay", propertyPrice[player_update])
                                    money = int(players[PlayerTurn]["money"])
                                    money -= propertyPrice[player_update]
                                    players[PlayerTurn]["money"] = money
                                    print("You now have", money, "dollars \n")
                            elif property[player_update] != "Income Tax":   
                                if property[player_update] != "Chance":
                                    # Checks if any one owns the property
                                    propertycheck = is_property_owned(property[player_update])
                                    # if the property check results in a player name it will state that name
                                    if propertycheck != None:
                                        # Property Check and rent 
                                        print("This property is owned by", propertycheck, "and you now need to pay a rent")
                                        ##########
                                        # rent original value * 0.20 and for each apt og value + 20% hotel  200% of inital  value
                                        #########
                                        for i in range(len(players)):
                                            if propertycheck in players[i]["playerName"]:
                                                propOwn = players[i]
                                        rentValue = propertyPrice[player_update] * 0.60
                                        money = int(players[PlayerTurn]["money"])
                                        money -= rentValue
                                        players[PlayerTurn]["money"] = int(money)
                                        moneyErn = int(propOwn["money"])
                                        moneyErn +=rentValue
                                        propOwn["money"] = int(moneyErn)

                                        print("You paid rent to", propertycheck, "for a total of", rentValue) 
                                        if PlayerTurn == settings[1]-1:
                                                    print("It is now the Ai's turn")
                                                    playerChange()
                                                    Ai_easy()
                                                    PlayerTurn = 0
                                        elif PlayerTurn < settings[1]:
                                                    PlayerTurn +=1
                                                    playerChange()
                                    # checks if no one owns the property and is not on jail
                                    elif propertycheck == None and property[player_update] != "jail/Just Visiting":
                                        # prints the price of the property as long as it costs more than 0
                                        if propertyPrice[player_update] > 0:
                                            print("It costs " + str(propertyPrice[player_update]) + " dollars  ")
                                            propertyBuyChoice = str(input("Do you want to buy this property? " + "\n"))
                                            while True:
                                                if propertyBuyChoice == "y" or propertyBuyChoice == "Y":
                                                    if int(players[PlayerTurn]["money"]) > propertyPrice[player_update]:
                                                        print("You have", players[PlayerTurn]["money"], "dollars \n")
                                                        buyCheck = input("You have enough money to buy this property, are you sure you want to buy it?: \n")
                                                        while True:        
                                                            if buyCheck == "y" or buyCheck == "Y":
                                                                money = int(players[PlayerTurn]["money"])
                                                                players[PlayerTurn]["money"] -= int(propertyPrice[player_update])
                                                                players[PlayerTurn]["properties"].append(property[player_update])
                                                                players[PlayerTurn]["Colors"].append(propertyColor[player_update])
                                                                print("You now own", property[player_update] + "\n")
                                                                time.sleep(2)
                                                                break
                                                            elif buyCheck == "n" or buyCheck == "N":
                                                                print("Ok Buy canceled... \n")
                                                                break    
                                                            else:
                                                                print("Please enter either a n or y ")
                                                                buyCheck = input("You have enough money to buy this property, are you sure you want to buy it?: \n")
                                                    elif players[PlayerTurn]["money"] < propertyPrice[player_update]:
                                                        print("You do not have enough money to buy this property")
                                                        
                                                        playerChange()
                                                    elif players[PlayerTurn]["money"] == 0:
                                                        print("Boi you are broke, you can't buy anything \n")
                                                        
                                                        playerChange()
                                                    break
                                                elif propertyBuyChoice == "n" or propertyBuyChoice == "N":
                                                    print("Alright buy canceled")
                                                    break
                                                else:
                                                    print("Please input either y or n")
                                                    propertyBuyChoice = str(input("Do you want to buy this property? " + "\n"))
                                            
                                            if PlayerTurn == settings[1]-1:
                                                    print("It is now the Ai's turn")
                                                    playerChange()
                                                    Ai_easy()
                                                    PlayerTurn = 0
                                            elif PlayerTurn < settings[1]:
                                                    PlayerTurn +=1
                                                    playerChange()
                                    elif property[player_update] == "jail/Just Visiting":
                                        print("Don't worry you are just visiting")
                                        if PlayerTurn == settings[1]-1:
                                            print("It is now the Ai's turn")
                                            playerChange()
                                            Ai_easy()
                                            PlayerTurn = 0
                                        elif PlayerTurn < settings[1]:
                                            PlayerTurn +=1
                                            playerChange()
                                        time.sleep(2)
                        # If the player lands on the GO TO JAIL property, sets the players jail setting to true and moves them back to jail
                        elif property[player_update] == "Go to Jail":
                            print("You are being sent to jail")
                            players[PlayerTurn]["inJail"] = True
                            player_update = property[10]
                            if PlayerTurn == settings[1]-1:
                                print("It is now the Ai's turn")
                                playerChange()
                                Ai_easy()
                                PlayerTurn = 0
                            elif PlayerTurn != settings[1]:
                                PlayerTurn +=1
                                playerChange()
                        # Snake eyes for players
                        if snakeEyes == False:
                            break
                        else:    
                            print("You got snake eyes and get to roll again")
        elif playerAction == 2:
            print("Alright next player is going now..")
            if PlayerTurn == settings[1]-1:
                print("It is now the Ai's turn")
                 
                playerChange()
                 
                Ai_easy()
                PlayerTurn = 0
            elif PlayerTurn < settings[1]:
                PlayerTurn +=1
                 
                playerChange()
        elif playerAction == 3:
            if len(players[PlayerTurn]["properties"]) == 0:
                print("You have no properties")
            elif  len(players[PlayerTurn]["properties"]) > 0:
                print("Warning Mortgaging a property will remove it from your pack and will be on the open market again")
                choice = input("Do you want to continue?: ")
                while True:
                    if choice == "Y" or "y":
                        for prop in range(len(players[PlayerTurn]["properties"])):
                            print(prop, players[PlayerTurn]["properties"][0+prop])
                        mortChoice = inputs("Which property would you like to mortgage: ", "integer", 0, len(players[PlayerTurn]["properties"]))
                        PropChoiceMort = property.index(players[PlayerTurn]["properties"][mortChoice])
                        propPriceMort = propertyPrice[PropChoiceMort]
                        mortValue = int(propPriceMort *0.55)
                        money = int(players[PlayerTurn]["money"])
                        money += mortValue
                        players[PlayerTurn]["money"] = money
                        players[PlayerTurn]["properties"].remove(players[PlayerTurn]["properties"][mortChoice])
                        players[PlayerTurn]["Colors"].remove(players[PlayerTurn]["Colors"][mortChoice])
                        print("Your property is now mortgaged and you made", mortValue, "dollers")
                        break
                    elif choice == "N" or "n":
                        break 
                    else: 
                        print("Please enter either y or n")
                        choice = input("Do you want to continue?")
        elif playerAction == 4:
            if players[PlayerTurn]["inJail"] == True:
                while True:    
                    bailChoice = input("The price of bail is $300, would you like to pay it?: ")
                    if bailChoice == "y" or "Y":
                        money = int(players[PlayerTurn]["money"])
                        money -= 300
                        players[PlayerTurn]["money"] = money
                        players[PlayerTurn]["inJail"] = False
                        print("You now have", players[PlayerTurn]["money"], "dollars")
                        if PlayerTurn == settings[1]-1:
                            print("It is now the Ai's turn")
                             
                            playerChange()
                             
                            Ai_easy()
                            PlayerTurn = 0
                        elif PlayerTurn < settings[1]:
                            PlayerTurn +=1
                             
                            playerChange()
                        break
                    elif bailChoice == "n" or "N":
                        print("Alright")
                        if PlayerTurn == settings[1]-1:
                            print("It is now the Ai's turn")
                             
                            playerChange()
                             
                            Ai_easy()
                            PlayerTurn = 0
                        elif PlayerTurn < settings[1]:
                            PlayerTurn +=1
                             
                            playerChange()
                        break
                    else:
                        print("Please enter either y or n")
                        bailChoice = input("The price of bail is $300, would you like to pay it?: ")
            elif players[PlayerTurn]["inJail"] == False:
                print("You are not in jail")
        elif playerAction == 5:
            print("Good bye")
            break
        else:
            print("Please enter a valid integer")
            playerAction = inputs("Please enter your action: ", "integer", 1, 6)
    elif money < 50:
        if len(players[PlayerTurn]["properties"]) > 0:
            print("You do not have enough money to play please do one of the following: ")
            print("1. Forfit Game (You will lose)")
            print("2. Mortgage a property")
            playChoice = input("Please enter one of the options: ", "integer", 1, 2)
        elif len(players[PlayerTurn]["properties"]) == 0:
            print("You do not have enough money to play")
            print("You dont have any properties, your only choice is to forfit... Sorry")
            time.sleep(1)
            print("Sorry to see this end so soon... ")
            players.remove(players[PlayerTurn])
            time.sleep(1)
            if len(players) == 1:
                print("Congrats", players[0]["playerName"], "You WON!!!!!!!!!!!")
                print("*\n"*6)
                print("You won!")
                break
