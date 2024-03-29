import pygame
from MyPlayer import MyPlayer
from Bot import Bot
from Wall import Wall
from MapChanger import MapChanger


def map01(x_pos, y_pos, developer_mode):
    pygame.init()
    # set screen
    pygame.display.set_caption('Prison Escape - Map 01')
    screen = pygame.display.set_mode((800, 600))

    # load textures
    idle = pygame.image.load('assets/map01/player/standing.png')

    walk_up = None

    walk_left = [pygame.image.load('assets/map01/player/L1.png'), pygame.image.load('assets/map01/player/L2.png'),
                 pygame.image.load('assets/map01/player/L3.png'), pygame.image.load('assets/map01/player/L4.png'),
                 pygame.image.load('assets/map01/player/L5.png'), pygame.image.load('assets/map01/player/L6.png'),
                 pygame.image.load('assets/map01/player/L7.png'), pygame.image.load('assets/map01/player/L8.png'),
                 pygame.image.load('assets/map01/player/L9.png')]

    walk_down = None

    walk_right = [pygame.image.load('assets/map01/player/R1.png'), pygame.image.load('assets/map01/player/R2.png'),
                  pygame.image.load('assets/map01/player/R3.png'), pygame.image.load('assets/map01/player/R4.png'),
                  pygame.image.load('assets/map01/player/R5.png'), pygame.image.load('assets/map01/player/R6.png'),
                  pygame.image.load('assets/map01/player/R7.png'), pygame.image.load('assets/map01/player/R8.png'),
                  pygame.image.load('assets/map01/player/R9.png')]

    bot_idle = None

    bot_up = None

    bot_left = [pygame.image.load('assets/map01/bot/L1E.png'), pygame.image.load('assets/map01/bot/L2E.png'),
                pygame.image.load('assets/map01/bot/L3E.png'), pygame.image.load('assets/map01/bot/L4E.png'),
                pygame.image.load('assets/map01/bot/L5E.png'), pygame.image.load('assets/map01/bot/L6E.png'),
                pygame.image.load('assets/map01/bot/L7E.png'), pygame.image.load('assets/map01/bot/L8E.png'),
                pygame.image.load('assets/map01/bot/L1E.png')]

    bot_down = None

    bot_right = [pygame.image.load('assets/map01/bot/R11E.png'), pygame.image.load('assets/map01/bot/R2E.png'),
                 pygame.image.load('assets/map01/bot/R3E.png'), pygame.image.load('assets/map01/bot/R4E.png'),
                 pygame.image.load('assets/map01/bot/R5E.png'), pygame.image.load('assets/map01/bot/R6E.png'),
                 pygame.image.load('assets/map01/bot/R7E.png'), pygame.image.load('assets/map01/bot/R8E.png'),
                 pygame.image.load('assets/map01/bot/R1E.png')]

    wall_texture = pygame.image.load('assets/map01/wall/grey_bricks.jpg')

    # define player
    player = MyPlayer(x_pos, y_pos, screen, walk_up, walk_left, walk_down, walk_right, idle, 5, developer_mode)

    # define the bots
    bots = [Bot(200, 300, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            Bot(600, 300, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode)]

    # define the walls
    walls = [Wall(0, 0, 150, 250, wall_texture), Wall(300, 0, 300, 200, wall_texture),
             Wall(600, 0, 200, 80, wall_texture), Wall(760, 230, 40, 170, wall_texture),
             Wall(650, 400, 200, 200, wall_texture), Wall(340, 525, 160, 75, wall_texture),
             Wall(0, 400, 150, 200, wall_texture)]

    # hidden walls that change maps
    mp = [MapChanger(150, 1, 150, 1), MapChanger(799, 80, 1, 150), MapChanger(500, 599, 150, 1),
          MapChanger(150, 599, 190, 1), MapChanger(0, 250, 1, 150)]

    # main loop of the map
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # clear screen
        screen.fill((0, 0, 0))

        # key press for player
        key = pygame.key.get_pressed()
        player.move(key)

        # Draw the walls
        for wall in walls:
            wall.draw(screen)

        # Draw the bots
        for bot in bots:
            bot.move()
            bot.check_collision(walls)
            bot.check_collision(mp)
            # if player collide bots it goes to game over screen and pass player position of map00 for new start
            if player.rect.colliderect(bot.rect):
                return "game_over", 390, 435

        # player collide check with walls
        player.check_collision(walls)

        # options for developer mode
        # show position of mouse on screen
        # show player and bots rect and also hidden map changer with blue color
        if developer_mode:
            font = pygame.font.SysFont("", 24)
            x, y = pygame.mouse.get_pos()
            coord_text = font.render(f'X: {x}, Y: {y}', True, (255, 0, 0))
            screen.blit(coord_text, (10, 10))  # Draw the text

            player.draw_rect(screen)
            for bot in bots:
                bot.draw_rect(screen)
            for mp_dev in mp:
                mp_dev.draw(screen)

        # Frame rate
        pygame.time.Clock().tick(30)

        # player collide with map changer
        # return map number and player new position on that map
        if player.rect.colliderect(mp[0]):
            pass
            # return "02", 34, 321

        if player.rect.colliderect(mp[1]):
            pass
            # return "03", 34, 321

        if player.rect.colliderect(mp[2]):
            pass
            # return "04", 34, 321

        if player.rect.colliderect(mp[3]):
            pass
            # return "04", 34, 321

        if player.rect.colliderect(mp[4]):
            # return "05", 34, 321
            pass

        # update display
        pygame.display.flip()

    pygame.quit()
