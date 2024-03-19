import pygame


class MyPlayer:
    def __init__(self, x, y, width, height, color1, color2, color3, screen_rect):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (color1, color2, color3)
        self.screen_rect = screen_rect

    def move(self, key):
        if key[pygame.K_w] or key[pygame.K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -2)
        if key[pygame.K_a] or key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-2, 0)
        if key[pygame.K_s] or key[pygame.K_DOWN] and self.rect.bottom > self.screen_rect.height:
            self.rect.move_ip(0, 2)
        if key[pygame.K_d] or key[pygame.K_RIGHT] and self.rect.right > self.screen_rect.width:
            self.rect.move_ip(2, 0)

        self.rect.clamp_ip(self.screen_rect)  # Keep the player within the screen

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
