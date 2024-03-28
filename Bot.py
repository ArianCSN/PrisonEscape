import pygame
import random


class Bot:
    def __init__(self, x, y, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, speed, developer_mode):
        self.screen = screen
        self.bot_up = bot_up
        self.bot_left = bot_left
        self.bot_down = bot_down
        self.bot_right = bot_right
        self.bot_idle = bot_idle
        self.speed = speed
        self.x = x
        self.y = y
        self.walk_count = 0
        self.direction = 'idle'
        self.developer_mode = developer_mode
        self.dx = 0
        self.dy = 0
        self.flag = 0
        self.check_size()
        self.rect = pygame.Rect(self.x, self.y, self.max_width, self.max_height)

    def move(self):
        self.flag += random.randint(1, 4)
        self.dx = 0
        self.dy = 0
        # Move the player
        if self.flag >= 20:
            random_move = random.randint(1, 4)
            if random_move == 1 and self.y > 1:
                self.dy = -self.speed
                if self.bot_up:
                    self.direction = 'up'
                elif self.direction == 'idle':
                    self.direction = 'right'
            elif random_move == 2 and self.x > 1:
                self.dx = -self.speed
                self.direction = 'left'
            elif random_move == 3 and self.y < 600 - self.max_height:
                self.dy = self.speed
                if self.bot_down:
                    self.direction = 'down'
                elif self.direction == 'idle':
                    self.direction = 'left'
            elif random_move == 4 and self.x < 800 - self.max_width:
                self.dx = self.speed
                self.direction = 'right'

            self.flag = 0

        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y

        if self.walk_count + 1 >= 27:
            self.walk_count = 0

        if self.direction == 'up':
            self.screen.blit(self.bot_up[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        elif self.direction == 'left':
            self.screen.blit(self.bot_left[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        elif self.direction == 'down':
            self.screen.blit(self.bot_down[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        elif self.direction == 'right':
            self.screen.blit(self.bot_right[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1

    # def check_collision(self, objects):
    #     # Create a new rect for the position we moved to
    #     new_rect = pygame.Rect(self.x, self.y, self.max_width, self.max_height)
    #     if self.developer_mode:
    #         pygame.draw.rect(self.screen, (255, 0, 0), new_rect, 1)
    #
    #     for obj in objects:
    #         if new_rect.colliderect(obj.rect):
    #             # If it collides, move back to the original position
    #             self.x -= self.dx
    #             self.y -= self.dy
    #             return 1

    def check_size(self):
        self.max_width = 0
        self.max_height = 0

        if self.bot_up:
            for x in self.bot_up:
                if self.max_width < x.get_width():
                    self.max_width = x.get_width()

                if self.max_height < x.get_height():
                    self.max_height = x.get_height()

        if self.bot_left:
            for x in self.bot_left:
                if self.max_width < x.get_width():
                    self.max_width = x.get_width()

                if self.max_height < x.get_height():
                    self.max_height = x.get_height()

        if self.bot_down:
            for x in self.bot_down:
                if self.max_width < x.get_width():
                    self.max_width = x.get_width()

                if self.max_height < x.get_height():
                    self.max_height = x.get_height()

        if self.bot_right:
            for x in self.bot_right:
                if self.max_width < x.get_width():
                    self.max_width = x.get_width()

                if self.max_height < x.get_height():
                    self.max_height = x.get_height()

    def check_collision(self, objects):
        # Create a new rect for the position we moved to
        for obj in objects:
            if self.rect.colliderect(obj.rect):
                # If it collides, move back to the original position
                self.x -= self.dx
                self.y -= self.dy
                break

    def draw_rect(self, screen):
        # Draw the rect with a distinct color (e.g., blue)
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)  # The '1' specifies the thickness of the line

