import pygame
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

# Color Definitions 
black = pygame.Color(0,0,0)
white = pygame.Color(255, 255, 255)


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
                        height = 600
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
        height = 600
        screen = pygame.display.set_mode((width, height))
        while True:
            screen.blit(settingsSavedImg, ((9.17/35.28)*width,(5.54/23.28)*height))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:            
                    if mouseX>((25.15/35.28)*width) and mouseX<((34.64/35.28)*width):
                        if mouseY > ((0.71/23.04)*height) and mouseY <((21.41/23.04) * height):
                            height = 600
                            screen = pygame.display.set_mode((width, height))
                            return 
            pygame.display.update() 
    else:
        print(settingsSaved)

# Game Exit Loop
gameExit = False

while not gameExit:
    # Cover Screen
    screen.blit(cover, (0,0))
    
    # Main screen
    mouseX, mouseY = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:            
            if mouseX>((11.36/35.28)*width) and mouseX<((23.85/35.28)*width):
                if mouseY > ((13.58/21.17)*height) and mouseY <((14.78/21.17) * height):
                        settingsSaved()
                        print("No saved Settings")
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


