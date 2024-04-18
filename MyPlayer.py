import pygame


class MyPlayer:
    def __init__(self, x, y, screen, walk_up, walk_left, walk_down, walk_right, idle, player_speed, developer_mode):
        self.speed = player_speed
        self.screen = screen
        self.walk_up = walk_up
        self.walk_left = walk_left
        self.walk_down = walk_down
        self.walk_right = walk_right
        self.idle = idle
        self.x = x
        self.y = y
        self.walk_count = 0
        self.direction = 'idle'
        self.developer_mode = developer_mode
        self.dx = 0
        self.dy = 0
        self.check_size()
        self.rect = pygame.Rect(self.x, self.y, self.max_width, self.max_height)

    def move(self, key):
        self.dx = 0
        self.dy = 0
        # Move the player
        if (key[pygame.K_w] or key[pygame.K_UP]) and self.y > 1:
            self.dy = -self.speed
            if self.walk_up:
                self.direction = 'up'
            elif self.direction == 'idle':
                self.direction = 'right'
        elif (key[pygame.K_a] or key[pygame.K_LEFT]) and self.x > 1:
            self.dx = -self.speed
            self.direction = 'left'
        elif (key[pygame.K_s] or key[pygame.K_DOWN]) and self.y < 600 - self.max_height:
            self.dy = self.speed
            if self.walk_down:
                self.direction = 'down'
            elif self.direction == 'idle':
                self.direction = 'left'
        elif (key[pygame.K_d] or key[pygame.K_RIGHT]) and self.x < 800 - self.max_width:
            self.dx = self.speed
            self.direction = 'right'
        else:
            self.direction = 'idle'
            self.walk_count = 0

        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y

        if self.walk_count + 1 >= len(self.walk_left)*3:
            self.walk_count = 0

        if self.direction == 'up':
            self.screen.blit(self.walk_up[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        elif self.direction == 'left':
            self.screen.blit(self.walk_left[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        elif self.direction == 'down':
            self.screen.blit(self.walk_down[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        elif self.direction == 'right':
            self.screen.blit(self.walk_right[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        else:
            self.screen.blit(self.idle, (self.x, self.y))
            self.walk_count = 0

    def check_collision(self, objects):
        # Create a new rect for the position we moved to
        for obj in objects:
            if self.rect.colliderect(obj.rect):
                # If it collides, move back to the original position
                self.x -= self.dx
                self.y -= self.dy
                break

    def check_size(self):

        self.max_width = 0
        self.max_height = 0
        if self.walk_up:
            for x in self.walk_up:
                if self.max_width < x.get_width():
                    self.max_width = x.get_width()

                if self.max_height < x.get_height():
                    self.max_height = x.get_height()

        if self.walk_left:
            for x in self.walk_left:
                if self.max_width < x.get_width():
                    self.max_width = x.get_width()

                if self.max_height < x.get_height():
                    self.max_height = x.get_height()

        if self.walk_down:
            for x in self.walk_down:
                if self.max_width < x.get_width():
                    self.max_width = x.get_width()

                if self.max_height < x.get_height():
                    self.max_height = x.get_height()


        if self.walk_right:
            for x in self.walk_right:
                if self.max_width < x.get_width():
                    self.max_width = x.get_width()

                if self.max_height < x.get_height():
                    self.max_height = x.get_height()

        if self.max_width < self.idle.get_width():
            self.max_width =self.idle.get_width()

        if self.max_height < self.idle.get_height():
            self.max_height = self.idle.get_height()

    def draw_rect(self, screen):
        # Draw the rect with a distinct color (e.g., blue)
        pygame.draw.rect(screen, (0, 255, 0), self.rect, 1)  # The '1' specifies the thickness of the line

