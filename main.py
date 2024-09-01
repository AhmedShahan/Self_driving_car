import pygame
pygame.init()
track=pygame.image.load('road/road1.png')
window= pygame.display.set_mode((1600,900))

visibility=True
while visibility:
    for events in pygame.event.get():
        # print(events)
        if events.type == pygame.QUIT:
            visibility=False
    window.blit(track,(0,0))
    pygame.display.update()