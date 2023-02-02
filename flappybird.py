import pygame
from sys import exit

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 700))
background_image = pygame.image.load("assets/background-day.png").convert_alpha()
background_image = pygame.transform.smoothscale(background_image, (600,700))
while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_image, (0, 0))

    pygame.display.update()
    clock.tick(60)
