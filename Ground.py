import pygame


class Ground:
    def __init__(self, screen_width, screen_height, ground_texture):
        self.texture = ground_texture.convert()  # Load the texture
        self.ground_texture = pygame.transform.scale(self.texture, (screen_width, screen_height))

    def draw(self, screen):
        screen.blit(self.ground_texture, (0, 0))