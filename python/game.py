import pygame
import time
import random

snake_speed = 15

window_x = 720
window_y = 480

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Hello Pygame")

fps = pygame.time.Clock()

snake_pos = [100,50]

snake_body =[ [100,50],
            [90,50],
            [80,50],
            [70,50]
]

fruit_pos = [random.randrange(1, (window_x//10)) * 10,
            random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

direction = 'RIGHT'
change_to = direction

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()