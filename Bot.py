import pygame
import random


class Bot:
    def __init__(self, x, y, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, speed, developer_mode):
        self.random_move = random.choice(["1", "2", "3", "4", "5"])
        self.speed = speed
        self.max_travel = random.randint(25//self.speed, 75//self.speed)
        self.facing = random.choice(["left", "right"])
        self.screen = screen
        self.bot_up = bot_up
        self.bot_left = bot_left
        self.bot_down = bot_down
        self.bot_right = bot_right
        self.bot_idle = bot_idle
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
        self.dx = 0
        self.dy = 0

        # Bot Movement Logic
        # - Determines bot movement based on the value of self.random_move.
        # - Updates the bot direction and facing accordingly.
        # - Adjusts the bot speed and idle state.
        if self.random_move == "1":
            self.dy = -self.speed
            self.max_travel -= 1
            if self.bot_up:
                self.direction = 'up'
                self.facing = "up"
            elif self.direction == 'idle':
                self.direction = 'right'
            else:
                self.facing = "right"
        elif self.random_move == "2":
            self.dx = -self.speed
            self.max_travel -= 1
            self.direction = 'left'
            self.facing = "left"
        elif self.random_move == "3":
            self.dy = self.speed
            self.max_travel -= 1
            if self.bot_down:
                self.direction = 'down'
                self.facing = "down"
            elif self.direction == 'idle':
                self.direction = 'left'
            else:
                self.facing = "left"
        elif self.random_move == "4":
            self.dx = self.speed
            self.max_travel -= 1
            self.direction = 'right'
            self.facing = "right"
        else:
            self.max_travel -= 1
            self.direction = 'idle'

        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y

        if self.max_travel <= 0:
            self.random_move = random.choice(["1", "2", "3", "4", "5"])
            self.max_travel = random.randint(20//self.speed, 50//self.speed)

        if self.bot_up and self.bot_down:
            if self.walk_count + 1 >= min(len(self.bot_up), len(self.bot_left)
                                          , len(self.bot_down), len(self.bot_right))*3:
                self.walk_count = 0

        else:
            if self.walk_count + 1 >= min(len(self.bot_left), len(self.bot_right))*3:
                self.walk_count = 0

        # Animation Logic for Bot Movement and Idle State
        if self.direction == 'up':
            # Animate walking texture when moving up
            self.screen.blit(self.bot_up[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        elif self.direction == 'left':
            # Animate walking texture when moving left
            self.screen.blit(self.bot_left[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        elif self.direction == 'down':
            # Animate walking texture when moving down
            self.screen.blit(self.bot_down[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        elif self.direction == 'right':
            # Animate walking texture when moving right
            self.screen.blit(self.bot_right[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        elif self.bot_idle is not None and self.direction == 'idle':
            # Handle idle state
            if self.facing == "right" or self.facing == "up":
                # Animate idle texture (normal orientation)
                self.screen.blit(self.bot_idle, (self.x, self.y))
            elif self.facing == "left" or self.facing == "down":
                # Flip and animate idle texture horizontally
                self.screen.blit(pygame.transform.flip(self.bot_idle, True, False), (self.x, self.y))
        else:
            # No idle texture available, use the first texture of every move
            if self.facing == "up":
                self.screen.blit(self.bot_up[0], (self.x, self.y))
            elif self.facing == "left":
                self.screen.blit(self.bot_left[0], (self.x, self.y))
            elif self.facing == "down":
                self.screen.blit(self.bot_down[0], (self.x, self.y))
            elif self.facing == "right":
                self.screen.blit(self.bot_right[0], (self.x, self.y))

    # Calculate Bot Rectangular Size
    # - Determines the maximum width and height required to enclose the bot textures.
    # - Iterates through each texture (up, left, down, right) to find the largest dimensions.
    # - Sets self.max_width and self.max_height accordingly.
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
                if self.random_move == "1":
                    self.random_move = random.choice(["2", "3", "4"])
                elif self.random_move == "2":
                    self.random_move = random.choice(["1", "3", "4"])
                elif self.random_move == "3":
                    self.random_move = random.choice(["1", "2", "4"])
                elif self.random_move == "4":
                    self.random_move = random.choice(["1", "2", "3"])

                self.max_travel = random.randint(20 // self.speed, 50 // self.speed)
                # If it collides, move back to the original position
                self.x -= self.dx
                self.y -= self.dy
                break

    def draw_rect(self, screen):
        # Draw the rect with a distinct color (e.g., blue)
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)  # The '1' specifies the thickness of the line
