import pygame
pygame.init()

# basic screen setup
pygame.display.set_caption("Monopoly Python Version")
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))

myfont = pygame.font.Font("MONOPOLY_INLINE.ttf",50)

clock = pygame.time.Clock()
#images 
cover = pygame.image.load("Images and assets/MONOCOVER.bmp")





# Color Definitions 
black = pygame.Color(0,0,0)
white = pygame.Color(255, 255, 255)

# Game Exit Loop
gameExit = False
while not gameExit:
    # Cover Screen
    screen.blit(cover, (0,0))
    """
    # All Rectangles 
    
    PlayButton = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(324, 380, 354, 35))
    instructButton = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(324, 450, 354, 35))
    settingsButton = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(324, 515, 354, 35))
    
    
    playDems = PlayButton.width
    playDemsheight = PlayButton.height
    # text write
    playText = myfont.render("PLAY", True, white) 
    
    settingsText = myfont.render("SETTINGS", True, white)

    instructText = myfont.render("INSTRUCTIONS", True, white)

    screen.blit(playText, (PlayButton.centerx - 32, 370))
    screen.blit(settingsText, (PlayButton.centerx - 20, 450))
    screen.blit(instructText, (PlayButton.centerx - 32, 515))
    
    # Mouse over button if statment 
    if PlayButton.collidepoint(pygame.mouse.get_pos()):
            print ('mouse is over newGameButton')
            print(PlayButton.x, PlayButton.y)
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(324, 380, 354, 35), 3)
            
    elif instructButton.collidepoint(pygame.mouse.get_pos()):
        print ('mouse is over InstructGameButton')
    elif settingsButton.collidepoint(pygame.mouse.get_pos()):
        print ('mouse is over SettingsGameButton')
    """
    mouseX, mouseY = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:            
            if mouseX>((11.36/35.28)*width) and mouseX<((23.85/35.28)*width):
                if mouseY > ((13.58/21.17)*height) and mouseY <((14.78/21.17) * height):
                    print("play")
                elif mouseY > ((16.02/21.17)* height) and mouseY < ((17.5/21.17) *  height):
                    print("Settings")
                elif mouseY > ((18.27/21.17) * height) and mouseY < ((19.51/21.17) * height):
                    print("Instructions")
    # Updates Screen
    
    pygame.display.update()
    
    clock.tick(60)
pygame.quit
quit()


