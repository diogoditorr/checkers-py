import pygame
import os
from pathlib import Path


path = Path(os.path.dirname(__file__))

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# RGB
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (220, 220, 220)
GRAY_BLACK = (128, 128, 128)

CROWN_IMAGE_PATH = path.joinpath("assets", "crown.png")
CROWN = pygame.transform.scale(pygame.image.load(CROWN_IMAGE_PATH), (44, 25))