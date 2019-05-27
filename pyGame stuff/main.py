import pygame
pygame.init()

pygame.display.set_caption("Monopoly Python Version")

screen = pygame.display.set_mode((1000, 600))

cover = pygame.image.load("Images and assets/MONOCOVER.bmp")
black = pygame.Color(0,0,0)
gameExit = False
while not gameExit:
    for event in pygame.event.get():
        screen.blit(cover, (0,0))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(324, 385, 354, 35))
        pygame.display.update()
pygame.quit
quit()