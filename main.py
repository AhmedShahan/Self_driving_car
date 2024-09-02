import pygame
import numpy as np
pygame.init()

# Load images
track = pygame.image.load('road/road2.png')
car = pygame.image.load('car/car2.png')

# Scale car image
car_scal = pygame.transform.scale(car, (220, 170))

# Create window
window = pygame.display.set_mode((1280, 720))

visibility = True

# Initial car position
car_x = 10
car_y = 270
threshold = 110
move_left = False
move_right = False

while visibility:
    # Calculate sensor position
    sensor_x = car_x + (220 / 2)
    sensor_y = car_y + (170 / 2)
    
    # Calculate detect point position
    detectPoint_x1 = sensor_x + threshold
    detectPoint_y1 = sensor_y
    
    detectPoint_x2 = sensor_x - threshold
    detectPoint_y2 = sensor_y

    detectPoint_x3 = sensor_x 
    detectPoint_y3 = sensor_y - threshold

    detectPoint_x4 = sensor_x 
    detectPoint_y4 = sensor_y + threshold

    detectPoint_x5 = sensor_x + 77.78
    detectPoint_y5 = sensor_y + 77.78

    detectPoint_x6 = sensor_x - 77.78
    detectPoint_y6 = sensor_y + 77.78
    
    detectPoint_x7 = sensor_x - 77.78
    detectPoint_y7 = sensor_y - 77.78

    detectPoint_x8 = sensor_x + 77.78
    detectPoint_y8 = sensor_y - 77.78

    # Draw the track and car on the window
    window.blit(track, (0, 0))
    window.blit(car_scal, (car_x, car_y))
    
    # Extract RGB value at detect point
    forward_pxR = window.get_at((int(detectPoint_x1), int(detectPoint_y1)))
    backward_pxR = window.get_at((int(detectPoint_x2), int(detectPoint_y2)))

    left_pxR = window.get_at((int(detectPoint_x3), int(detectPoint_y3)))
    right_pxR = window.get_at((int(detectPoint_x4), int(detectPoint_y4)))

    upper_rightCorner_pxR = window.get_at((int(detectPoint_x5), int(detectPoint_y5)))
    upper_leftCorner_pxR = window.get_at((int(detectPoint_x6), int(detectPoint_y6)))
    
    lower_leftCorner_pxR = window.get_at((int(detectPoint_x7), int(detectPoint_y7)))
    lower_rightCorner_pxR = window.get_at((int(detectPoint_x8), int(detectPoint_y8)))

    # Check for events
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            visibility = False
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT:
                move_left = True
            elif events.key == pygame.K_RIGHT:
                move_right = True
        elif events.type == pygame.KEYUP:
            if events.key == pygame.K_LEFT:
                move_left = False
            elif events.key == pygame.K_RIGHT:
                move_right = False

    # Move car based on key presses and RGB value
    # if forward_pxR[0] == 255:  # Assuming you're checking for red
    #     car_x += 2
    if move_left:
        car_x -= 2
    if move_right:
        car_x += 2
    
    # Draw circles to visualize sensor and detect points
    pygame.draw.circle(window, (0, 255, 0), (int(sensor_x), int(sensor_y)), 5, 5)
    pygame.draw.circle(window, (255, 255, 0), (int(detectPoint_x1), int(detectPoint_y1)), 5, 5)
    pygame.draw.circle(window, (0, 255, 0), (int(detectPoint_x2), int(detectPoint_y2)), 5, 5)
    pygame.draw.circle(window, (0, 255, 0), (int(detectPoint_x3), int(detectPoint_y3)), 5, 5)
    pygame.draw.circle(window, (0, 255, 0), (int(detectPoint_x4), int(detectPoint_y4)), 5, 5)
    pygame.draw.circle(window, (0, 255, 0), (int(detectPoint_x5), int(detectPoint_y5)), 5, 5)
    pygame.draw.circle(window, (0, 255, 0), (int(detectPoint_x6), int(detectPoint_y6)), 5, 5)
    pygame.draw.circle(window, (0, 255, 0), (int(detectPoint_x7), int(detectPoint_y7)), 5, 5)
    pygame.draw.circle(window, (0, 255, 0), (int(detectPoint_x8), int(detectPoint_y8)), 5, 5)
    
    # Update the display
    pygame.display.update()

pygame.quit()
