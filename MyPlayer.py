import pygame


class MyPlayer:
    def __init__(self, x, y, width, height, screen_rect):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 0, 0)
        self.screen_rect = screen_rect

    def move(self, key, walls, bots):
        # Store the original position in case we need to revert due to collision
        original_rect = self.rect.copy()

        # Move the player
        if key[pygame.K_w] or key[pygame.K_UP]:
            self.rect.move_ip(0, -2)
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.rect.move_ip(-2, 0)
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            self.rect.move_ip(0, 2)
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.rect.move_ip(2, 0)

        # Keep the player within the screen
        self.rect.clamp_ip(self.screen_rect)

        # Collision detection with walls
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                # Collision detected, move back to the original position
                self.rect = original_rect
                break

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)