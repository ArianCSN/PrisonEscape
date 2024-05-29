import pygame
import random
from Ground import Ground
from MyPlayer import MyPlayer
from Bot import Bot
from Wall import Wall
from InvisibleWall import InvisibleWall


def map07(x_pos, y_pos, developer_mode):
    # start the pygame and pygame mixer
    pygame.init()
    pygame.mixer.init()

    # set up screen
    screen_width = 1536
    screen_height = 864
    pygame.display.set_caption('Prison Escape')
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    # Hide the mouse cursor
    if not developer_mode:
        pygame.mouse.set_visible(False)

    # load texture
    ground_texture = pygame.image.load('assets/map07/ground/ground.jpg')

    wall_texture = pygame.image.load('assets/map07/wall/wall.png')

    idle = pygame.image.load('assets/map07/player/idle.png')

    walk_up = None

    walk_left = [pygame.image.load('assets/map07/player/L1.png'), pygame.image.load('assets/map07/player/L2.png'),
                 pygame.image.load('assets/map07/player/L3.png'), pygame.image.load('assets/map07/player/L4.png'),
                 pygame.image.load('assets/map07/player/L5.png'), pygame.image.load('assets/map07/player/L6.png')]

    walk_down = None

    walk_right = [pygame.image.load('assets/map07/player/R1.png'), pygame.image.load('assets/map07/player/R2.png'),
                  pygame.image.load('assets/map07/player/R3.png'), pygame.image.load('assets/map07/player/R4.png'),
                  pygame.image.load('assets/map07/player/R5.png'), pygame.image.load('assets/map07/player/R6.png')]

    bot_idle = pygame.image.load('assets/map07/bot/idle.png')

    bot_up = None

    bot_left = [pygame.image.load('assets/map07/bot/L1.png'), pygame.image.load('assets/map07/bot/L2.png'),
                pygame.image.load('assets/map07/bot/L3.png'), pygame.image.load('assets/map07/bot/L4.png'),
                pygame.image.load('assets/map07/bot/L5.png'),pygame.image.load('assets/map07/bot/L6.png')]

    bot_down = None

    bot_right = [pygame.image.load('assets/map07/bot/R1.png'), pygame.image.load('assets/map07/bot/R2.png'),
                 pygame.image.load('assets/map07/bot/R3.png'), pygame.image.load('assets/map07/bot/R4.png'),
                 pygame.image.load('assets/map07/bot/R5.png'),pygame.image.load('assets/map07/bot/R6.png')]

    # define the ground
    ground = Ground(screen_width, screen_height, ground_texture)

    # Create the player character
    # The player is represented by an instance of the MyPlayer class:
    # - (x_pos, y_pos): Initial position on the screen
    # - screen: Pygame screen object
    # - Textures for different directions (walk_up, walk_left, walk_down, walk_right, idle)
    # - Speed (5th input): Controls how fast the player moves (higher values mean faster movement)
    # - developer_mode: A flag indicating whether to enable developer-specific features
    player = MyPlayer(x_pos, y_pos, screen, walk_up, walk_left, walk_down, walk_right, idle, 5, developer_mode)

    # Bot Spawning Logic
    # - Initializes a list of bots.
    # - Randomly generates between 5 and 15 bots.
    # - Each bot is placed within a specified area:
    #   - x position: random value between 510 and 1117.
    #   - y position: random value between 330 and 720.
    # - Bots are created with textures for different directions (up, left, down, right, idle),
    #   a movement speed of 2, and developer mode settings.
    bots = []

    for i in range(random.randint(5, 15)):
        bots.append(Bot(random.randint(510, 1117), random.randint(330, 720), screen,
                        bot_up, bot_left, bot_down, bot_right, bot_idle, 2, developer_mode))

    # Define the walls
    # Each wall is represented by a rectangular area with specific dimensions:
    # - (x, y): Top-left corner coordinates
    # - Width and height of the wall
    # - Texture (wall_texture) used for rendering
    walls = [Wall(0, 0, 1050, 180, wall_texture), Wall(0, 300, 480, 563, wall_texture),
             Wall(480, 750, 300, 113, wall_texture), Wall(900, 750, 300, 113, wall_texture),
             Wall(1200, 0, 335, 863, wall_texture)]

    # Hidden walls that change maps
    # These invisible walls act as triggers to transition between different maps :
    # - (x, y): Top-left corner coordinates
    # - Width and height of the trigger area
    # - InvisibleWall objects handle map transitions
    mp = [InvisibleWall(1050, 0, 150, 2), InvisibleWall(780, 861, 120, 2),
          InvisibleWall(0, 180, 2, 120)]

    # Additional border walls:
    # - The player can pass through these borders, but bots are prevented from doing so.
    border = [InvisibleWall(450, 270, 750, 30), InvisibleWall(780, 750, 120, 30)]

    # main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # clear screen
        screen.fill((0, 0, 0))

        ground.draw(screen)

        # key press for player
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            exit()

        player.move(key)

        # Draw the walls
        for wall in walls:
            wall.draw(screen)

        # Draw the bots
        for bot in bots:
            bot.move()
            bot.check_collision(walls)
            bot.check_collision(mp)
            bot.check_collision(border)
            # if player collide bots it goes to game over screen and pass player position of map01 for new start
            if player.rect.colliderect(bot.rect):
                sound_effect = pygame.mixer.Sound('assets/map07/sound/lose.wav')
                sound_effect.set_volume(0.2)
                sound_effect.play()
                pygame.mixer.music.stop()
                return "game_over", 780, 390

        # player collide check with walls
        player.check_collision(walls)

        # Options for developer mode:
        # - Show map number
        # - Show position of mouse and player on screen
        # - Show player, map changers, walls, borders and bots rect
        # - If the space key is pressed, the player teleports to the mouse position
        if developer_mode:
            font = pygame.font.SysFont("", 24)
            x, y = pygame.mouse.get_pos()
            screen.blit(font.render(f"Developer Mode - Map07", True, (255, 0, 0)), (10, 5))
            screen.blit(font.render(f'X: {x}, Y: {y}', True, (255, 0, 0)), (10, 25))
            screen.blit(font.render(f'player x : {player.x}', True, (255, 0, 0)), (10, 45))
            screen.blit(font.render(f'player x : {player.y}', True, (255, 0, 0)), (10, 65))

            if key[pygame.K_SPACE]:
                player.x = x
                player.y = y

            player.draw_rect(screen)

            for bot in bots:
                bot.draw_rect(screen)

            for mp_dev in mp:
                mp_dev.draw(screen, (0, 0, 255))

            for wall in walls:
                wall.rect_draw(screen, (0, 255, 0))

            for br in border:
                br.draw(screen, (178, 34, 34))

        # Frame rate
        pygame.time.Clock().tick(30)

        # player collide with map changer
        # return map number and player new position on that map
        # Due to differentiation in player texture length between map03 and other maps
        # subtract from player's x position to ensure no collision with the wall occurs.
        if player.rect.colliderect(mp[0]):
            return "map03", player.x, 826

        if player.rect.colliderect(mp[1]):
            return "map12", player.y, 3

        if player.rect.colliderect(mp[2]):
            if player.y > 268:
                player.y -= 5
            return "map04", 1504, player.y

        # update display
        pygame.display.flip()

    pygame.quit()
