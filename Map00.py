import pygame
from MyPlayer import MyPlayer
from Bot import Bot
from Wall import Wall


def map00():
    pygame.init()
    pygame.display.set_caption('Prison Escape')
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont(None, 24)
    screen_rect = screen.get_rect()

    player = MyPlayer(390, 435, 25, 50, screen_rect)
    bots = [Bot(200, 300, 25, 50, 0, 0, 255, 20, screen_rect), Bot(600, 300, 25, 50, 0, 0, 255, 5, screen_rect)]
    # define the walls
    walls = [Wall(0, 0, 150, 250), Wall(0, 400, 150, 200), Wall(300, 0, 300, 200), Wall(600, 0, 200, 80),
             Wall(760, 230, 40, 170), Wall(650, 400, 200, 200), Wall(300, 400, 40, 200), Wall(340, 525, 160, 75)
             , Wall(460, 400, 40, 125)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        key = pygame.key.get_pressed()
        player.move(key, walls, bots)

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the Objects
        for wall in walls:
            wall.draw(screen)

        player.draw(screen)

        for bot in bots:
            bot.move(walls)
            bot.draw(screen)

        x, y = pygame.mouse.get_pos()
        coord_text = font.render(f'X: {x}, Y: {y}', True, (255, 0, 0))
        screen.blit(coord_text, (10, 10))  # Draw the text
        # Update the display
        pygame.display.flip()

        # Frame rate
        pygame.time.Clock().tick(60)

        for bot in bots:
            if player.rect.colliderect(bot.rect):
                return "game_over"

    pygame.quit()
