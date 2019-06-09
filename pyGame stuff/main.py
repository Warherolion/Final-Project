import pygame
import pygame as pg
pygame.init()

# basic screen setup
pygame.display.set_caption("Monopoly Python Version")
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))

myfont = pygame.font.Font("Fonts/MONOPOLY_INLINE.ttf",50)

clock = pygame.time.Clock()
#images 
cover = pygame.image.load("Images and assets/MONOCOVER.bmp")
instruct = pygame.image.load("Images and assets/instruct.bmp")
settingsSavedImg = pygame.image.load("Images and assets/SavedSettings.bmp")


#Monopoly Board
board = pygame.image.load("Images and assets/monopolyBoard.bmp")
# Name Asker
PlayerName2 = pygame.image.load("Images and assets/PlayerName2.bmp")
PlayerName4 = pygame.image.load("Images and assets/PlayerName4.bmp")
# Color Definitions 
black = pygame.Color(0,0,0)
white = pygame.Color(255, 255, 255)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive


players = []
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


def MainGame():
    pass

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
                            #screen.fill((0, 0, 0))
                            print("no negg")

                        
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


