import pygame
pygame.init()

# basic screen setup
pygame.display.set_caption("Monopoly Python Version")
screen = pygame.display.set_mode((1000, 600))

myfont = pygame.font.Font("MONOPOLY_INLINE.ttf",50)

#images 
cover = pygame.image.load("Images and assets/MONOCOVER.bmp")





# Color Definitions 
black = pygame.Color(0,0,0)
white = pygame.Color(255, 255, 255)
# Game Exit Loop
gameExit = False
while not gameExit:
    for event in pygame.event.get():
        # Cover Screen
        screen.blit(cover, (0,0))

        # All Rectangles 
        PlayButton = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(324, 380, 354, 35))
        instructButton = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(324, 450, 354, 35))
        settingsButton = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(324, 515, 354, 35))
        
        # text write
        text = myfont.render("Play", True, white)
        screen.blit(text, (324,380))
       
        # Mouse over button if statment 
        if PlayButton.collidepoint(pygame.mouse.get_pos()):
                print ('mouse is over newGameButton')
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(324, 380, 354, 35), 3)
                
        elif instructButton.collidepoint(pygame.mouse.get_pos()):
            print ('mouse is over InstructGameButton')
        elif settingsButton.collidepoint(pygame.mouse.get_pos()):
            print ('mouse is over SettingsGameButton')

        # Updates Screen
        pygame.display.update()
pygame.quit
quit()
