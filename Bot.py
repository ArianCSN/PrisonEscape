import pygame
import random


class Bot:
    def __init__(self, x, y, width, height, color1, color2, color3, speed, screen_rect):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (color1, color2, color3)
        self.screen_rect = screen_rect
        self.direction = 0
        self.flag = 0
        self.speed = speed
    import random

    def move(self, walls):
        # Store the original position in case we need to revert due to collision
        original_rect = self.rect.copy()
        # Speed and movement direction of bots
        self.flag += random.randint(1, 4)
        if self.flag >= 20:
            direction = random.randint(1, 4)
            if direction == 1:
                self.rect.move_ip(0, self.speed)
            if direction == 2:
                self.rect.move_ip(-self.speed, 0)
            if direction == 3:
                self.rect.move_ip(0, -self.speed)
            if direction == 4:
                self.rect.move_ip(self.speed, 0)
            self.flag = 0

        # Keep the bots within the screen
        self.rect.clamp_ip(self.screen_rect)

        # Collision detection with walls
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                # Collision detected, move back to the original position
                self.rect = original_rect
                # Choose a new random direction to move in next time
                self.direction = random.choice([(0, -5), (0, 5), (-5, 0), (5, 0)])
                break

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
