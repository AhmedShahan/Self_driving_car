import pygame
pygame.init()
track=pygame.image.load('road/road2.png')
car=pygame.image.load('car/car1.png')

car_scal=pygame.transform.scale(car,(200,150))

window= pygame.display.set_mode((1280,720))

visibility=True
while visibility:
    for events in pygame.event.get():
        # print(events)
        if events.type == pygame.QUIT:
            visibility=False
    window.blit(track,(0,0))
    window.blit(car_scal,(0,0))

    pygame.display.update()