import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
x = WIDTH // 2
y = HEIGHT // 2
speed = 5
TILE_SIZE = 30  # Still used for Pac-Man size

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman-Demo")

clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += speed

    screen.fill((0, 0, 0))  # Black background
    pygame.draw.circle(screen, (255, 255, 0), (x, y), TILE_SIZE // 2)  # Yellow Pac-Man
    pygame.display.flip()
    clock.tick(60)
