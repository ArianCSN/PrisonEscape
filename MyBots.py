import pygame
import random


class MyBots:
    def __init__(self, x, y, width, height, color1, color2, color3, screen_rect):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (color1, color2, color3)
        self.screen_rect = screen_rect

    def move(self):
        self.rect.move_ip(random.randint(-4, 4), random.randint(-4, 4))
        self.rect.clamp_ip(self.screen_rect)  # Keep the Bots within the screen

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
