import pygame


class Wall:
    def __init__(self, x, y, width, height, wall_texture):
        self.rect = pygame.Rect(x, y, width, height)
        self.texture = wall_texture.convert()  # Load the texture
        self.texture_width, self.texture_height = self.texture.get_size()

    def draw(self, screen):
        # Tile the texture within the wall's boundaries
        for i in range(self.rect.left, self.rect.right, self.texture_width):
            for j in range(self.rect.top, self.rect.bottom, self.texture_height):
                # Calculate the area to blit on screen
                area = pygame.Rect(i, j, min(self.texture_width, self.rect.right - i), min(self.texture_height, self.rect.bottom - j))
                screen.blit(self.texture, area, area)