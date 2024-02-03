# Python code using Pygame for a simple player-controlled spaceship game

import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Spaceship Game")

# Colors
white = (0, 0, 0)

# Load spaceship image
spaceship_img = pygame.image.load('base_spaceship.png')
# Rotate the original image to get the spaceship facing upwards
spaceship = pygame.transform.rotate(spaceship_img, -90)
spaceship_rect = spaceship.get_rect()
spaceship_x = window_width / 2
spaceship_y = window_height / 2

# Initial velocity and acceleration
velocity = 0
acceleration = 0
angle = 0

# Game loop
running = True
while running:
    game_window.fill(white)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key states for controlling the spaceship
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle += 5
    if keys[pygame.K_RIGHT]:
        angle -= 5
    if keys[pygame.K_UP]:
        acceleration += 0.1
        spaceship_x += velocity * math.sin(math.radians(angle))
        spaceship_y += velocity * math.cos(math.radians(angle))

    # Rotate the spaceship image based on the current angle
    rotated_spaceship = pygame.transform.rotate(spaceship, angle)
    rotated_rect = rotated_spaceship.get_rect(center=(spaceship_x, spaceship_y))

    # Draw the rotated spaceship on the game window
    game_window.blit(rotated_spaceship, rotated_rect.topleft)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
