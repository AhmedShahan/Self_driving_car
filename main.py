import pygame
pygame.init()
window= pygame.display.set_mode((1200,720))
track=pygame.image.load('road/road1.png')

while True:
    window.blit(track,(0,0))

    pygame.display.update()