import pygame
from MyPlayer import MyPlayer
from Bot import Bot
from Wall import Wall
from MapChanger import MapChanger


def map00(x_pos, y_pos, developer_mode):
    pygame.init()
    pygame.display.set_caption('Prison Escape')
    screen = pygame.display.set_mode((800, 600))

    screen_rect = screen.get_rect()

    idle = pygame.image.load('Images/Game/standing.png')

    walk_up = None

    walk_left = [pygame.image.load('Images/Game/L1.png'), pygame.image.load('Images/Game/L2.png'),
                 pygame.image.load('Images/Game/L3.png'), pygame.image.load('Images/Game/L4.png'),
                 pygame.image.load('Images/Game/L5.png'), pygame.image.load('Images/Game/L6.png'),
                 pygame.image.load('Images/Game/L7.png'), pygame.image.load('Images/Game/L8.png'),
                 pygame.image.load('Images/Game/L9.png')]

    walk_down = None

    walk_right = [pygame.image.load('Images/Game/R1.png'), pygame.image.load('Images/Game/R2.png'),
                  pygame.image.load('Images/Game/R3.png'), pygame.image.load('Images/Game/R4.png'),
                  pygame.image.load('Images/Game/R5.png'), pygame.image.load('Images/Game/R6.png'),
                  pygame.image.load('Images/Game/R7.png'), pygame.image.load('Images/Game/R8.png'),
                  pygame.image.load('Images/Game/R9.png')]

    bot_idle = pygame.image.load('Images/Game/standing.png')

    bot_up = None

    bot_left = [pygame.image.load('Images/Game/L1E.png'), pygame.image.load('Images/Game/L2E.png'),
                 pygame.image.load('Images/Game/L3E.png'), pygame.image.load('Images/Game/L4E.png'),
                 pygame.image.load('Images/Game/L5E.png'), pygame.image.load('Images/Game/L6E.png'),
                 pygame.image.load('Images/Game/L7E.png'), pygame.image.load('Images/Game/L8E.png'),
                pygame.image.load('Images/Game/L1E.png')]

    bot_down = None

    bot_right = [pygame.image.load('Images/Game/R1E.png'), pygame.image.load('Images/Game/R2E.png'),
                  pygame.image.load('Images/Game/R3E.png'), pygame.image.load('Images/Game/R4E.png'),
                  pygame.image.load('Images/Game/R5E.png'), pygame.image.load('Images/Game/R6E.png'),
                  pygame.image.load('Images/Game/R7E.png'), pygame.image.load('Images/Game/R8E.png'),
                 pygame.image.load('Images/Game/R1E.png')]

    player = MyPlayer(x_pos, y_pos, screen, walk_up, walk_left, walk_down, walk_right, idle, developer_mode)
    # define the bots
    bots = [Bot(200, 5, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 10, developer_mode),
            Bot(600, 300, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 5, developer_mode)]
    # define the walls
    walls = [Wall(0, 0, 150, 250), Wall(0, 400, 150, 200), Wall(300, 0, 300, 200), Wall(600, 0, 200, 80),
             Wall(760, 230, 40, 170), Wall(650, 400, 200, 200), Wall(300, 400, 40, 200), Wall(340, 525, 160, 75)
        , Wall(460, 400, 40, 125)]

    Mapchanger = [MapChanger(763, 80, 150, 250)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.fill((0, 0, 0))
        key = pygame.key.get_pressed()
        player.move(key)

        # Draw the Objects
        for wall in walls:
            wall.draw(screen)

        for bot in bots:
            bot.move()
            bot.check_collision(walls)
            if player.rect.colliderect(bot.rect):
                return "game_over", 390, 435

            if developer_mode:
                bot.draw_rect(screen)

        player.check_collision(walls)

        if developer_mode:
            font = pygame.font.SysFont("", 24)
            x, y = pygame.mouse.get_pos()
            coord_text = font.render(f'X: {x}, Y: {y}', True, (255, 0, 0))
            screen.blit(coord_text, (10, 10))  # Draw the text
            player.draw_rect(screen)

        # Frame rate
        pygame.time.Clock().tick(120)

        if player.rect.colliderect(Mapchanger[0]):
            return "01", 34, 321
        pygame.display.flip()

    pygame.quit()
