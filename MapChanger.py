import pygame


class MapChanger:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 0, 255)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
