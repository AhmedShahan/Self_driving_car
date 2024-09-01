import pygame
pygame.init()
track=pygame.image.load('road/road2.png')
car=pygame.image.load('car/car2.png')

car_scal=pygame.transform.scale(car,(220,170))

window= pygame.display.set_mode((1280,720))

visibility=True

car_x=10
car_y=270
while visibility:
    for events in pygame.event.get():
        # print(events)
        if events.type == pygame.QUIT:
            visibility=False
    window.blit(track,(0,0))
    window.blit(car_scal,(car_x,car_y))
    car_x=car_x+2
    pygame.display.update()