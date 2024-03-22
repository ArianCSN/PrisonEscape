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
    bot1 = Bot(300, 300, 25, 50, 0, 0, 250, screen_rect)
    bot2 = Bot(300, 300, 25, 25, 0, 150, 0, screen_rect)
    bot3 = Bot(300, 300, 25, 25, 0, 0, 200, screen_rect)
    bot4 = Bot(300, 300, 25, 25, 0, 0, 150, screen_rect)

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
        player.move(key, walls)
        bot1.move(walls)
        # bot2.move(walls)
        # bot3.move(walls)
        # bot4.move(walls)

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the Objects
        for wall in walls:
            wall.draw(screen)

        player.draw(screen)
        bot1.draw(screen)
        # bot2.draw(screen)
        # bot3.draw(screen)
        # bot4.draw(screen)
        x, y = pygame.mouse.get_pos()
        coord_text = font.render(f'X: {x}, Y: {y}', True, (255, 0, 0))
        screen.blit(coord_text, (10, 10))  # Draw the text
        # Update the display
        pygame.display.flip()

        # Frame rate
        pygame.time.Clock().tick(60)

    pygame.quit()
