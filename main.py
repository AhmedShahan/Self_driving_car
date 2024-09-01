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
    sensor_x=car_x + (220/2)
    sensor_y= car_y + (170/2)
    for events in pygame.event.get():
        # print(events)
        if events.type == pygame.QUIT:
            visibility=False
    window.blit(track,(0,0))
    window.blit(car_scal,(car_x,car_y))
    car_x=car_x+2
    pygame.draw.circle(window,(0,255,0),(sensor_x,sensor_y),5,5)
    pygame.display.update()