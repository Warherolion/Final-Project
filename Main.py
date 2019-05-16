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
#  Figure out how to use the settings variable in the code
# Make sure to add a check to weather it is the main players role or if the AI rolled
# add snake eye implementation '
# finish all the setup questions
# Turn the chance cards into commands
# figure out how to ask for player names
# Make a function that will add what ever the player and Ai buys to a list
# Make the AI work based off an easy, normal and hard setting.
# Finish if statment for if the player lands on a chance
# add a money part to the players list
# add a list for the price of the properties
# see if you want to add a save game in memory function, use the shelve option
import time
import random
from filename import add






property = ["Go", "Mediterranean Ave", "Community Chest", "Baltic Ave", "Income Tax", "Reading Railroad",
            "Oriental Ave", "Chance", "Vermont Ave", "Connecticut Ave", "jail/Just Visiting", "St. Charles Place",
            "Electric Company", "States Ave", "Virginia Ave", "Pennsylvania Railroad", "St. James Place",
            "Community Chest", "Tennessee Ave", "New York Ave", "Free Parking", "Kentucky Ave", "Chance",
            "Indiana Ave", "Illinois Ave", "B. & O. Railroad", "Atlantic Ave", "Ventnor Ave", "Water Works",
            "Marvin Gardens", "Go to Jail", "Pacific Ave", "North Carolina Ave", "Community Chest",
            "Pennsylvania Ave", "Short Line Railroad", "Chance", "Park Place", "Luxury Tax", "Boardwalk"]
propertyPrice= [
    200, 60, 0, 60,100, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160,200, 180, 0,180, 200, 0, 220, 0, 220, 240,
    200, 260, 260, 150, 280, 0, 300, 300, 0, 320, 200, 0, 350, 300, 400
]

chanceCards = ["Advance to Go (Collect $200)", "Advance to Illinois Ave—If you pass Go, collect $200",
               "Advance to St. Charles Place – If you pass Go, collect $200", "Advance token to nearest Utility",
               "Advance token to the nearest Railroad and pay owner twice the rental to which they areotherwise "
               "entitled to", "Bank pays you dividend of $50", "Get Out of Jail Free", "Go Back 3 Spaces",
               "Go to Jail", "Make general repairs on all your property–For each house pay $25–For each hotel $100",
               "Pay poor tax of $15", "Take a trip to Reading Railroad–If you pass Go, collect $200",
               "Take a walk on the Boardwalk–Advance token to Boardwalk", "You have been elected Chairman of the "
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
                  "You are assessed for street repairs–$40 per house–$115 per hotel", "You have won second prize in "
                                                                                      "a beauty contest–Collect $10",
                  "You inherit $100"]
players = []

playerMoveCount = []

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


def playerChange():
    print("Next Player")
    print("***************************************")
    print("*")
    print("*")
    print("*")
    print("*")
    print("***************************************")
# Settings file, if user chooses to run setup this is all the setup questions


def gameSettingsSetup():
    settingsCheck = open("settings.txt", "r")
    print("Lets setup")
    # Int Setup questions
    numPlayers = str(inputs('How many real players are playing: ', "intger"))
    numAIplayers = str(inputs('How many AI players will be playing?: ', "integer"))
    if numAIplayers != "0":
        AILevel = str(inputs("What AI difficulty level would you like? (Easy, Normal, Hard): "))
        while True:
            if AILevel == "Easy" or AILevel == "Normal" or AILevel == "Hard":
                startingMoney = str(inputs("How much money does everyone start with? Max: 10 000 (Keep in mind "
                                           "this does not affect the property prices) ", "integer", 100, 10000))

                for i in range(int(numPlayers)):
                    name = input("What is the players name? ")
                    players.append({"playerName": name, "money":startingMoney, "properties": [], "railroads": []})

                break
            else:
                print("Please enter a valid input (make sure to capitalize the first letter)")
                AILevel = str(inputs("What AI difficulty level would you like? (Easy, Normal, Hard): "))

    elif numAIplayers == "0":
        startingMoney = str(inputs("How much money does everyone start with? Max: 10 000 (Keep in mind "
                                   "this does not affect the property prices) ", "integer", 100, 10000))

        for i in range(int(numPlayers)):
            name = input("What is the players name? ")
            players.append(name)

    print("Alright the setup is complete, Your game will start now....")
    time.sleep(1)

    # sends over the settings into the text file as well as monoset check
    if "MonoSet1-1" in settingsCheck.read():
        with open("settings.txt", "w") as file:
            file.write("MonoSet1-1: true" + "\n")
            file.write("numPlayer: " + numPlayers + "\n")
            file.write("numAIplayer: " + numAIplayers + "\n")
            file.write("AI Level: " + AILevel + "\n")
            file.write("startingMoney: " + startingMoney + "\n")
            file.close()

    return settingsCheck, players


# Intro
settingsCheck = open("settings.txt", "r")
print("Hello! Welcome to the game of monopoly, Terminal version before we can start we have to make sure "
      "everything is set up properly... \n")
time.sleep(2)
# Settings check, checks if a settings file exists and if so checks if the user wants to use them. s
importSetyn = input("You have saved settings in you setting file, would you like to use them? (y or n): \n")
if "MonoSet1-1" in settingsCheck.read():
    while True:
        if importSetyn == "y" or importSetyn == "Y":
            print("Alright lets start your game... \n")
            time.sleep(1)
            players = []
            for i in range(int(settings[1])):
                name = input("What is the players name? ")
                players.append(
                    {
                    "playerName": name,
                    "money": settings[4],
                    "properties": [],
                    "railroads": [],
                    "inJail":   False,
                    "PlayerLocation": property[0]
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





# Picks a random card from the chance lists


def chancePickUp():
    cardPick = random.randint(0, len(chanceCards))
    return chanceCards[cardPick]

# Picks a random card from the community chest lists

def communityPickUp():
    cardPick = random.randint(0, len(CommunityChest))
    return CommunityChest[cardPick]


def dice_roll():

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    total = die1 + die2
    return die1, die2, total


# Main code, a for loop for all the real players
for x in range(0, int(settings[1])):
    die1, die2, total = dice_roll()

    # Calls either chance or community function to pick a random card and give it to the player
    ChanceCardPick = chancePickUp()
    CommunityCardPick = communityPickUp()


    # property owned check, sees if anyone owns the property and returns either none or the playerName
    def is_property_owned(property_name):
        for p in players:
            if property_name in p['properties']:
                return p['playerName']  # Returns the owner of property
        return None


    print("It is now", players[0+x]["playerName"] , "turn \n")

    time.sleep(1)
    print("You rolled a", die1, "and a", die2, "you move forward",total, "steps \n")

    time.sleep(1)

    print("You landed on", property[total] + "\n")

    player_update = players[0 + x]["PlayerLocation"] = property[total]

    time.sleep(1)

    if property[total] == "Community Chest" or property[total] == "Chance":
        if property[total] == "Community Chest":
            print("The card you picked states", CommunityCardPick, "\n")
        elif property[total] == "Chance":
            print("The card you picked states", ChanceCardPick)
        else:
            print("Something went wrong, sorry")
    elif property[total] != "Community Chest":
            if property[total] != "Chance":

                # Checks if any one owns the property
                propertycheck = is_property_owned(property[total])

                # if the property check results in a player name it will state that name
                if propertycheck != None:
                    print("This property is owned by", propertycheck)

                # checks if no one owns the property and is not on jail
                elif propertycheck == None and property[total] != "jail/Just Visiting":

                    # prints the price of the property as long as it costs more than 0
                    if propertyPrice[total] > 0:
                        print("It costs " + str(propertyPrice[total]) + " dollars  ")

                        propertyBuyChoice = str(input("Do you want to buy this property? " + "\n"))

                        if propertyBuyChoice == "y" or propertyBuyChoice == "Y":

                            if int(players[0 + x]["money"]) > propertyPrice[total]:

                                print("You have", players[0 + x]["money"], "dollars \n")

                                buyCheck = input(
                                    "You have enough money to buy this property, are you sure you want to buy it?: \n")

                                if buyCheck == "y" or buyCheck == "Y":

                                    money = int(players[0 + x]["money"])

                                    money -= int(propertyPrice[total])

                                    players[0 + x]["properties"] = property[total]

                                    print("You now own", property[total] + "\n")

                                    time.sleep(2)

                                    if int(settings[1]) >= 2 and x != int(settings[1]):

                                        print("Your turn has now ended please switch to the next person \n")

                                        playerChange()


                                        time.sleep(3)

                                    elif int(settings[1]) == 1:

                                        print("It is now the AI's turn.... \n")

                                        playerChange()

                                        time.sleep(3)


                                    elif int(settings[1]) == x:

                                        print("It is now the AI's turn.... \n")

                                        playerChange()

                                        time.sleep(3)

                                elif buyCheck == "n" or buyCheck == "N":

                                    print("Ok Buy canceled... \n")

                                else:
                                    print("Please enter either a n or y ")

                            elif players[x]["money"] < propertyPrice[total]:
                                print("You do not have enough money to buy this property")
                                playerChange()
                            elif players[x]["money"] == 0:
                                print("Boi you are broke, you can't buy anything \n")
                                playerChange()
                        elif propertyBuyChoice == "n" or propertyBuyChoice == "N":

                            print("Alright")

                        else:
                            print("Please input either y or n")
                            propertyBuyChoice = str(input("Do you want to buy this property? " + "\n"))

    elif property[total] == "jail/Just Visiting":
        print("Don't worry you are just visiting")
    # If the player lands on the GO TO JAIL property, sets the players jail setting to true and moves them back to jail
    elif property[total] == "Go to Jail":
        print("You are being sent to jail")
        players[x]["isJail"] = True
        player_update = property[10]

