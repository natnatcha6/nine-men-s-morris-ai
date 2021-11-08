import pygame

pygame.init()

vec = pygame.math.Vector2

WIDTH = 800
HEIGHT = 800
ACC = 0.5
FRIC = -0.12
FPS = 60

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nine men's morris")