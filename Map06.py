import pygame
from Ground import Ground
from MyPlayer import MyPlayer
from Bot import Bot
from Wall import Wall
from InvisibleWall import InvisibleWall


def map06(x_pos, y_pos, developer_mode):
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
    ground_texture = pygame.image.load('assets/map06/ground/ground.jpg')

    wall_texture = pygame.image.load('assets/map06/wall/wall.png')

    idle = pygame.image.load('assets/map06/player/idle.png')

    walk_up = None

    walk_left = [pygame.image.load('assets/map06/player/L1.png'), pygame.image.load('assets/map06/player/L2.png'),
                 pygame.image.load('assets/map06/player/L3.png'), pygame.image.load('assets/map06/player/L4.png'),
                 pygame.image.load('assets/map06/player/L5.png'), pygame.image.load('assets/map06/player/L6.png')]

    walk_down = None

    walk_right = [pygame.image.load('assets/map06/player/R1.png'), pygame.image.load('assets/map06/player/R2.png'),
                  pygame.image.load('assets/map06/player/R3.png'), pygame.image.load('assets/map06/player/R4.png'),
                  pygame.image.load('assets/map06/player/R5.png'), pygame.image.load('assets/map06/player/R6.png')]

    bot_idle = None

    bot_up = None

    bot_left = [pygame.image.load('assets/map06/bot/L1.png'), pygame.image.load('assets/map06/bot/L2.png'),
                pygame.image.load('assets/map06/bot/L3.png'), pygame.image.load('assets/map06/bot/L4.png'),
                pygame.image.load('assets/map06/bot/L5.png'), pygame.image.load('assets/map06/bot/L6.png')]

    bot_down = None

    bot_right = [pygame.image.load('assets/map06/bot/R1.png'), pygame.image.load('assets/map06/bot/R2.png'),
                 pygame.image.load('assets/map06/bot/R3.png'), pygame.image.load('assets/map06/bot/R4.png'),
                 pygame.image.load('assets/map06/bot/R5.png'), pygame.image.load('assets/map06/bot/R6.png')]

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

    # Define the bots
    # Each bot is initialized with specific parameters:
    # - (x, y): Initial position on the screen
    # - screen: Pygame screen object
    # - Textures for different directions (up, left, down, right, idle)
    # - Speed (9th input): Controls how fast the bot moves (higher values mean faster movement)
    # - developer_mode: A flag indicating whether to enable developer-specific features
    bots = [Bot(210, 420, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            Bot(390, 420, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            Bot(360, 540, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            Bot(570, 180, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            Bot(510, 300, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode),
            Bot(690, 300, screen, bot_up, bot_left, bot_down, bot_right, bot_idle, 1, developer_mode)]

    # Define the walls
    # Each wall is represented by a rectangular area with specific dimensions:
    # - (x, y): Top-left corner coordinates
    # - Width and height of the wall
    # - Texture (wall_texture) used for rendering
    walls = [Wall(0, 0, 1535, 90, wall_texture), Wall(0, 90, 120, 150, wall_texture),
             Wall(300, 180, 120, 150, wall_texture), Wall(540, 390, 120, 150, wall_texture),
             Wall(0, 330, 120, 533, wall_texture), Wall(120, 750, 120, 113, wall_texture),
             Wall(240, 630, 480, 233, wall_texture), Wall(720, 780, 330, 83, wall_texture),
             Wall(840, 240, 695, 420, wall_texture), Wall(1140, 660, 395, 203, wall_texture)]

    # Hidden walls that change maps
    # These invisible walls act as triggers to transition between different maps :
    # - (x, y): Top-left corner coordinates
    # - Width and height of the trigger area
    # - InvisibleWall objects handle map transitions
    mp = [InvisibleWall(1533, 90, 2, 150), InvisibleWall(1050, 861, 90, 2),
          InvisibleWall(0, 240, 2, 90)]

    # Define a temporary wall
    Temp_Wall = [Wall(840, 90, 60, 150, wall_texture)]

    # Create two buttons at different positions
    # Note : The second button is hidden 60 pixels to the right of the temporary wall
    buttons = [InvisibleWall(150, 690, 60, 30), InvisibleWall(960, 90, 30, 150)]

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

        # Check if there is a temporary wall (Temp_Wall) present.
        if Temp_Wall:
            # Draw the element of the Temp_Wall list on the screen.
            Temp_Wall[0].draw(screen)

        # Check if there are buttons present.
        if buttons:
            # Draw the first button with an orange color (255, 126, 0) on the screen.
            buttons[0].draw(screen, (255, 126, 0))

        # Iterate through each button.
        for button in buttons:
            # Check if the player's rectangle collides with the button.
            if player.rect.colliderect(button):
                # If there is a temporary wall, play a sound effect and remove both the wall and buttons.
                if Temp_Wall:
                    sound_effect = pygame.mixer.Sound('assets/map06/sound/open.wav')
                    sound_effect.set_volume(0.4)
                    sound_effect.play()
                    Temp_Wall.clear()
                    buttons.clear()

        # Draw the bots and check collision
        for bot in bots:
            bot.move()
            bot.check_collision(walls)
            bot.check_collision(Temp_Wall)
            bot.check_collision(mp)
            # if player collide bots it goes to game over screen and pass player position of map01 for new start
            if player.rect.colliderect(bot.rect):
                sound_effect = pygame.mixer.Sound('assets/map06/sound/lose.wav')
                sound_effect.set_volume(0.2)
                sound_effect.play()
                pygame.mixer.music.stop()
                return "game_over", 780, 390

        # player collide check with walls and temporary wall
        player.check_collision(walls)
        player.check_collision(Temp_Wall)

        # options for developer mode
        # show position of mouse on screen
        # show player and bots rect and also hidden map changer and hidden second button with blue color
        # If the space key is pressed, the player teleport to mouse position
        if developer_mode:
            font = pygame.font.SysFont("", 24)
            x, y = pygame.mouse.get_pos()
            coord_text = font.render(f'X: {x}, Y: {y}', True, (255, 0, 0))
            screen.blit(coord_text, (10, 10))  # Draw the text

            if key[pygame.K_SPACE]:
                player.x = x
                player.y = y

            player.draw_rect(screen)
            for bot in bots:
                bot.draw_rect(screen)
            for mp_dev in mp:
                mp_dev.draw(screen, (0, 0, 255))

            if buttons:
                buttons[1].draw(screen, (0, 0, 255))

        # Frame rate
        pygame.time.Clock().tick(30)

        # player collide with map changer
        # return map number and player new position on that map
        if player.rect.colliderect(mp[0]):
            return "map11", 3, player.y

        if player.rect.colliderect(mp[1]):
            return "map03", player.x, 3

        if player.rect.colliderect(mp[2]):
            return "map02", 1494, player.y

        # update display
        pygame.display.flip()

    pygame.quit()
