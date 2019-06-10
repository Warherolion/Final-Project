import pygame
from random import *

pygame.init()
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



# basic screen setup
pygame.display.set_caption("Monopoly Python Version")
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))

myfont = pygame.font.Font("Fonts/MONOPOLY_INLINE.ttf",50)
subfont = pygame.font.Font("Fonts/MONOPOLY_INLINE.ttf",30)
clock = pygame.time.Clock()
#images 
cover = pygame.image.load("Images and assets/MONOCOVER.bmp")
instruct = pygame.image.load("Images and assets/instruct.bmp")
settingsSavedImg = pygame.image.load("Images and assets/SavedSettings.bmp")

RollButton = pygame.image.load("Images and assets/RollButton.bmp")
SkipButton = pygame.image.load("Images and assets/skipButton.png")

# Player Pieces
Player1 = pygame.image.load("Images and assets/PlayPiece1.bmp")
Player2 = pygame.image.load("Images and assets/PlayPiece2.bmp")
Player3 = pygame.image.load("Images and assets/PlayPiece3.bmp")
Player4 = pygame.image.load("Images and assets/PlayPiece4.bmp")

#Monopoly Board
board = pygame.image.load("Images and assets/MonoBoard.bmp")
# Name Asker
PlayerName2 = pygame.image.load("Images and assets/PlayerName2.bmp")
PlayerName4 = pygame.image.load("Images and assets/PlayerName4.bmp")
# Color Definitions 
black = pygame.Color(0,0,0)
white = pygame.Color(255, 255, 255)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive

# Dice Roll function 
def dice_roll():
    snakeEyes = False
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    if die1 == die2:
        snakeEyes = True
    total = die1 + die2
    return die1, die2, total, snakeEyes
# Picks a random card from the chance lists
def chancePickUp():
    cardPick = random.randint(0, 15)
    return chanceCards[cardPick]

# Picks a random card from the community chest lists

def communityPickUp():
    cardPick = random.randint(0, 16)
    return CommunityChest[cardPick]


# File access
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

settingsCheck = open("settings.txt", "r")

if "MonoSet1-1" in settingsCheck.read():
    settingsSaved = True
else:
    settingsSaved = False

players = []


def MainGame():
    x1 = 640; y1 = 640
    x2 = 650; y2 = 650
    x3 = 670; y3 = 670
    x4 = 680; y4 = 680
    while True: 
        die1, die2, total, snakeEyes = dice_roll()
        width = 1100
        height = 707
        screen = pygame.display.set_mode((width, height))
        screen.blit(board, (0,0))
        # Creates player information tab on side of board
        if int(settings[1]) == 1:
            PlayInfor = pygame.Rect(710, 0, 390, 707)
        elif int(settings[1]) == 2:
            mouseX, mouseY = pygame.mouse.get_pos()
            PlayInfor = pygame.draw.rect(screen, white, (710, 0, 390, 707))
            x = 0
            playerinfo = myfont.render(players[0]["playerName"], False, (0, 0, 0))
            playerProperties = subfont.render("Owned Properties: ", False, (0, 0, 0))
            propHeight = 100
            for c in range (len(players[x]["properties"])):
                playerProp = subfont.render(players[x]["properties"][c], False, (0, 0, 0))
                screen.blit (playerProp, (730, propHeight))
                print(propHeight)
                propHeight += 30
            playerMoney = subfont.render("Money: " + str(players[0]["money"]), False, (0, 0, 0))
            screen.blit (playerMoney, (730, propHeight+20))
            screen.blit(RollButton, (730, 650))
            screen.blit(SkipButton, (1000, 650))
            for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:            
                        if mouseX>((7.573/11.448)*width) and mouseX<((8.344 /11.448)*width):
                            if mouseY > ((6.670/7.354)*height) and mouseY <((7.031/7.354) * height):
                                if x == 0:
                                    # Calls either chance or community function to pick a random card and give it to the player
                                    ChanceCardPick = chancePickUp()
                                    CommunityCardPick = communityPickUp()
                                    # property owned check, sees if anyone owns the property and returns either none or the playerName
                                    def is_property_owned(property_name):
                                        for p in players:
                                            if property_name in p['properties']:
                                                return p['playerName']  # Returns the owner of property
                                            """
                                            else:
                                                for a in aiPlayerList:
                                                    if property_name in a['properties']:
                                                        return a['AiName']  # Returns the owner of property
                                            """
                                        return None
                                    pd = property.index(property[total])
                                    players[0 + x]["PlayerLocation"] += pd
                                    player_update = players[0 + x]["PlayerLocation"]
                                
                                    print("You rolled a", die1, "and a", die2, "you move forward",total, "steps \n")
                                    
                                    print("You landed on", property[player_update] + "\n")
                                    
                                    if property[player_update] == "Community Chest" or property[player_update] == "Chance":
                                        if property[player_update] == "Community Chest":
                                            print(CommunityChest.index(CommunityCardPick))
                                            print("The card you picked states", CommunityCardPick, "\n")
                                        elif property[player_update] == "Chance":
                                            print(chanceCards.index(ChanceCardPick))
                                            print("The card you picked states", ChanceCardPick)
                                        else:
                                            print("Something went wrong, sorry")
                                    elif property[player_update] != "Community Chest":
                                        # checks if the user landed on income tax and will deduct it from their money
                                        if property[player_update] == "Income Tax":
                                                print("You have to pay", propertyPrice[player_update])
                                                money = int(players[x]["money"])
                                                money -= propertyPrice[player_update]
                                                print("You now have", money, "dollars \n")
                                        elif property[player_update] != "Income Tax":   
                                            if property[player_update] != "Chance":
                                                # Checks if any one owns the property
                                                propertycheck = is_property_owned(property[player_update])
                                                # if the property check results in a player name it will state that name
                                                if propertycheck != None:
                                                    print("This property is owned by", propertycheck)
                                                # checks if no one owns the property and is not on jail
                                                elif propertycheck == None and property[player_update] != "jail/Just Visiting":
                                                    # prints the price of the property as long as it costs more than 0
                                                    if propertyPrice[player_update] > 0:
                                                        print("It costs " + str(propertyPrice[player_update]) + " dollars  ")
                                                        propertyBuyChoice = str(input("Do you want to buy this property? " + "\n"))
                                                        if propertyBuyChoice == "y" or propertyBuyChoice == "Y":
                                                            if int(players[0 + x]["money"]) > propertyPrice[player_update]:
                                                                print("You have", players[0 + x]["money"], "dollars \n")
                                                                buyCheck = input(
                                                                    "You have enough money to buy this property, are you sure you want to buy it?: \n")
                                                                if buyCheck == "y" or buyCheck == "Y":
                                                                    money = int(players[0 + x]["money"])
                                                                    money -= int(propertyPrice[player_update])
                                                                    players[0 + x]["properties"] = property[player_update]
                                                                    players[x]["Colors"] = propertyColor[player_update]
                                                                    print("You now own", property[player_update] + "\n")
                                                                elif buyCheck == "n" or buyCheck == "N":
                                                                    print("Ok Buy canceled... \n")
                                                                else:
                                                                    print("Please enter either a n or y ")
                                                            elif players[x]["money"] < propertyPrice[player_update]:
                                                                print("You do not have enough money to buy this property")
                                                            elif players[x]["money"] == 0:
                                                                print("Boi you are broke, you can't buy anything \n")
                                                        elif propertyBuyChoice == "n" or propertyBuyChoice == "N":
                                                            print("Alright")
                                                        else:
                                                            print("Please input either y or n")
                                                            propertyBuyChoice = str(input("Do you want to buy this property? " + "\n"))
                                                            print(x1, y1)
                                                            print(total)
                                    if y1 < (((0.177 * total) / 11.48)) * width:
                                        upValve1 = (total - 10) + total
                                        print("B", y1)
                                        y1 = 30
                                        print("c", x1)
                                        x1 += (((0.625 * upValve1) / 11.48)) * width
                                    elif x1 > (((0.281 * total) / 11.48)) * width:
                                        x1 -= (((0.625 * total) / 11.48)) * width
                                    elif x1 < (((0.281 * total) / 11.48)) * width:
                                        upValve = (total - 10) + total
                                        x1 = 40                                       
                                        y1 -= (((0.625 * upValve) / 7.354)) * height
                                
        elif int(settings[1]) == 3:
            PlayInfor = pygame.draw.rect(screen, white, (710, 0, 390, 707))
            PlayInfor2 = pygame.draw.rect(screen, white, (710, 0, 390, 707))
            PlayInfor3 = pygame.draw.rect(screen, white, (710, 0, 390, 707))
        elif int(settings[1]) == 4:
            PlayInfor = pygame.draw.rect(screen, white, (710, 0, 390, 707))
            PlayInfor2 = pygame.draw.rect(screen, white, (710, 0, 390, 707))
            PlayInfor3 = pygame.draw.rect(screen, white, (710, 0, 390, 707))
            PlayInfor4 = pygame.draw.rect(screen, white, (710, 0, 390, 707))
        
        
        screen.blit(playerinfo, (730, 10))
        screen.blit (playerProperties, (730, 60))
        
        
        # Checks to see how many people are playing
        if int(settings[1]) == 1:
            screen.blit(Player1, (x1,y1))
        elif int(settings[1]) == 2:
            screen.blit(Player1, (x1,y1))
            screen.blit(Player2, (x2, y2))
        elif int(settings[1]) == 3:
            screen.blit(Player1, (x1,y1))
            screen.blit(Player2, (x2, y2))
            screen.blit(Player3, (x3,y3))
        elif int(settings[1]) == 4:
            screen.blit(Player1, (x1,y1))
            screen.blit(Player2, (x2, y2))
            screen.blit(Player3, (x3,y3))
            screen.blit(Player4, (x4,y4))
        
        pygame.display.update()
        screen.fill((255, 255, 255))
        return  die1, die2, total, snakeEyes
# Instructions Page 
def instructPage():
    #updates screen to size that fits the instructions page
    height = 660
    screen = pygame.display.set_mode((width, height))
    
    while True:
        # Gets the users mouse position
        mouseX, mouseY = pygame.mouse.get_pos()
        screen.blit(instruct, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:            
                if mouseX>((25.15/35.28)*width) and mouseX<((34.64/35.28)*width):
                    if mouseY > ((0.71/23.04)*height) and mouseY <((21.41/23.04) * height):
                        height= 600
                        screen = pygame.display.set_mode((width, height))
                        return 
        pygame.display.update() 


def settingsSaved():

    settingsCheck = open("settings.txt", "r")
    if "MonoSet1-1" in settingsCheck.read():
        settingsSaved = True
    else:
        settingsSaved = False
    if settingsSaved == True:
        while True:
            mouseX, mouseY = pygame.mouse.get_pos()
            screen.blit(settingsSavedImg, ((9.17/35.28)*width,(5.54/23.28)*height))
            for event in pygame.event.get():            
                if event.type == pygame.MOUSEBUTTONDOWN:             
                    # Checks if the user clicked on the Yes button
                    if mouseX>((10.48/35.28)*width) and mouseX<((14.04 /35.28)*width):
                        if mouseY > ((12.88/21.17)*height) and mouseY <((13.62/21.17) * height):
                            # asks the user for the names based off of the settings
                            return True
                    # Checks if the user clicks on the No button
                    elif mouseX>((21.59/35.28)*width) and mouseX<((25.15 /35.28)*width):
                        if mouseY > ((12.88/21.17)*height) and mouseY <((13.62/21.17) * height):
                            print("no")
                            return False   

            pygame.display.update() 
    else:
        print(settingsSaved)

# Game Exit Loop
gameExit = False
draw = False
while not gameExit:
    # Cover Screen
    screen.blit(cover, (0,0))
    
    # Main screen
    mouseX, mouseY = pygame.mouse.get_pos()
    text = ''
    if draw:
        if int(settings[1]) == 2:
            for playNum in range (int(settings[1])):
                name = input("Please enter your player name: ")
                players.append( 
                    {
                    "playerName": name,
                    "money": settings[4],
                    "properties": [],
                    "Colors": [],
                    "railroads": [],
                    "inJail":   False,
                    "PlayerLocation": 0
                    }
                )  
            draw = False
            MainGame()
        elif int(settings[1] == 4):
            screen.blit(PlayerName4, (9.17/35.28)*width,(5.54/23.28)*height)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:            
            if mouseX>((11.36/35.28)*width) and mouseX<((23.85/35.28)*width):
                if mouseY > ((13.58/21.17)*height) and mouseY <((14.78/21.17) * height):
                        done = settingsSaved()
                        print("Yes")
                        if done == False:
                            print("No saved Settings")
                        if done:
                            if int(settings[1]) == 2:
                                screen.blit(cover, (0,0))
                                screen.blit(PlayerName2, (0,0))
                            elif int(settings[1] == 4):
                                screen.blit(PlayerName4, (9.17/35.28)*width,(5.54/23.28)*height)
                            draw = True
   
                elif mouseY > ((16.02/21.17)* height) and mouseY < ((17.5/21.17) *  height):
                    print("Settings")
                elif mouseY > ((18.27/21.17) * height) and mouseY < ((19.51/21.17) * height):
                    print("Instructions")
                    instructPage()
        # Updates Screen
        pygame.display.update()

clock.tick(60)

pygame.quit
quit()


