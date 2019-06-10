import random
import time
from Main import players, chancePickUp, communityPickUp, ChanceCardPick, communityPickUp, x, player_update
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
propertyColor = [
    "None", "Brown", "None", "Brown", "None", "None", "Navy", "None", "Navy", "Navy", "None", "Pink", "None", "Pink", "Pink", "None", "Orange", 
    "None", "Orange", "Orange", "None", "Red", "None", "Red", "Red", "None", "Yellow", "Yellow", "None", "Yellow", "None", "Green", "Green", "None",
    "Green", "None", "None", "Blue", "None", "Blue"    
]
Color=["Brown", "Navy", "Pink", "Orange", "Red", "Yellow", "Green", "Blue"]
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


"""
    {
    "playerName": name,
    "money": settings[4],
    "properties": ["Mediterranean Ave", "Baltic Ave"],
    "Colors": ["Brown", "Brown"],
    "railroads": [],
    "inJail":   False,
    "PlayerLocation": 0
    "Getoutajail": False
    }
"""
def chance_community():
    if property[player_update] == "Chance":
        if chanceCards.index(ChanceCardPick) == 0:
            players[x]["PlayerLocation"] = 0
            money = int(players[x]["money"])
            money += 200
            print("You were moved back to go and gained $200")
        elif chanceCards.index(ChanceCardPick) == 1:
            ill = property.index("Illinois Ave") 
            
            players[x]["PlayerLocation"] = ill
            print("You are now on Illinois Ave")
        elif chanceCards.index(ChanceCardPick) == 2:
            cill = property.index("St. Charles Place")
            players[x]["PlayerLocation"] = ill
            print("You are now on St. Charles Place")
        elif chanceCards.index(ChanceCardPick) == 3:
            money = int(players[x]["money"])
            money += 50
            print("You earned 5$0")
        elif chanceCards.index(ChanceCardPick) == 4:
            if players[x]["Getoutajail"] == True:
                print("You already have a get outa jail free card so no more for you..")
            elif players[x]["Getoutajail"] == False:
                players[x]["Getoutajail"] == True
                print("You now own a get out of jail free card")
        elif chanceCards.index(ChanceCardPick) == 5:
            players[x]["PLayerLocation"] -= 3
            print("You Got moved back 3 spaces")
        elif chanceCards.index(ChanceCardPick) == 6:
            players[x]["inJail"]= True
            players[x]["PlayerLocation"] = 10
            print("Oh no you are now in jail")
        elif chanceCards.index(ChanceCardPick) == 7:
            money = int(players[x]["money"])   
            money -= 15
        elif chanceCards.index(ChanceCardPick) == 8:
            players[x]["PlayerLocation"] = 5
            print("You went to reading railroad")
        elif chanceCards.index(ChanceCardPick) == 9:
            bord = property.index("Boardwalk")
            players[x]["PlayerLocation"] = bord
            print("You went to Boardwalk")
        elif chanceCards.index(ChanceCardPick) == 10:
            count = 0
            for pp in range(len(players)):
                money = players[pp]["money"]
                money +=50
                count +=1
            moneylost = (50 * count) -50
            players[x]["money"] -= moneylost
            print("You paid everyone $50") 
        elif chanceCards.index(ChanceCardPick) == 11:
            money = players[x]["money"]
            money +=150
            print("You made $150")
        elif chanceCards.index(ChanceCardPick) == 12:
            money = players[x]["money"]
            money +=100
            print("You made $100")

    elif property[player_update] == "Community Chest":
        if CommunityChest.index(ChanceCardPick) == 0:
            players[x]["PlayerLocation"] = 0
            money = int(players[x]["money"])
            money += 200
            print("You were moved back to go and gained $200")
        elif CommunityChest.index(ChanceCardPick) == 1:
            money = int(players[x]["money"])
            money += 200
            print("You made $200")
        elif CommunityChest.index(ChanceCardPick) == 2:
            money = int(players[x]["money"])
            money += 50
            print("You paid $50")
        elif CommunityChest.index(ChanceCardPick) == 3:
            money = int(players[x]["money"])
            money += 50
            print("You earned $50")
        elif CommunityChest.index(ChanceCardPick) == 4:
            if players[x]["Getoutajail"] == True:
                print("You already have a get outa jail free card so no more for you..")
            elif players[x]["Getoutajail"] == False:
                players[x]["Getoutajail"] == True
                print("You now own a get out of jail free card")
        elif CommunityChest.index(ChanceCardPick) == 5:
            players[x]["inJail"]= True
            players[x]["PlayerLocation"] = 10
            print("Oh no you are now in jail")
        elif CommunityChest.index(ChanceCardPick) == 6:
            count = 0
            for pp in range(len(players)):
                money = players[pp]["money"]
                money -=50
                count +=1
            moneyGain = (50 * count) +50
            players[x]["money"] -= moneyGain
            print("You got $50 from everyone") 
        
        elif CommunityChest.index(ChanceCardPick) == 7:
            money = int(players[x]["money"])   
            money += 100
            print("You made $100")
        elif CommunityChest.index(ChanceCardPick) == 8:
            money = int(players[x]["money"])   
            money += 20
            print("You made $20")
        elif CommunityChest.index(ChanceCardPick) == 9:
            money = int(players[x]["money"])   
            money += 10
            print("You made $10")
        elif CommunityChest.index(ChanceCardPick) == 10:
            money = int(players[x]["money"])   
            money += 100
            print("You made $100")
        elif CommunityChest.index(ChanceCardPick) == 11:
            money = players[x]["money"]
            money -=150
            print("You paid $150")
        elif CommunityChest.index(ChanceCardPick) == 12:
            money = players[x]["money"]
            money +=25
            print("You made $25")
        elif CommunityChest.index(ChanceCardPick) == 13:
            money = players[x]["money"]
            money +=10
            print("You made $10")
        elif CommunityChest.index(ChanceCardPick) == 14:
            money = players[x]["money"]
            money +=100
            print("You made $100")