import pygame
from Ground import Ground
from MyPlayer import MyPlayer
from Bot import Bot
from Wall import Wall
from InvisibleWall import InvisibleWall


def map09(x_pos, y_pos, developer_mode):
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
    ground_texture = pygame.image.load('assets/map09/ground/ground.jpg')

    wall_texture = pygame.image.load('assets/map09/wall/wall.png')

    idle = pygame.image.load('assets/map09/player/idle.png')

    walk_up = None

    walk_left = [pygame.image.load('assets/map09/player/L1.png'), pygame.image.load('assets/map09/player/L2.png'),
                 pygame.image.load('assets/map09/player/L3.png'), pygame.image.load('assets/map09/player/L4.png'),
                 pygame.image.load('assets/map09/player/L5.png'), pygame.image.load('assets/map09/player/L6.png')]

    walk_down = None

    walk_right = [pygame.image.load('assets/map09/player/R1.png'), pygame.image.load('assets/map09/player/R2.png'),
                  pygame.image.load('assets/map09/player/R3.png'), pygame.image.load('assets/map09/player/R4.png'),
                  pygame.image.load('assets/map09/player/R5.png'), pygame.image.load('assets/map09/player/R6.png')]
    
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

    # Define the walls
    # Each wall is represented by a rectangular area with specific dimensions:
    # - (x, y): Top-left corner coordinates
    # - Width and height of the wall
    # - Texture (wall_texture) used for rendering
    walls = [Wall(0, 0, 1535, 60, wall_texture), Wall(0, 60, 120, 180, wall_texture),
             Wall(60, 240, 60, 30, wall_texture), Wall(60, 300, 30, 30, wall_texture),
             Wall(0, 330, 90, 450, wall_texture), Wall(120, 60, 60, 690, wall_texture),
             Wall(210, 90, 60, 690, wall_texture), Wall(300, 60, 60, 690, wall_texture),
             Wall(390, 90, 60, 690, wall_texture), Wall(480, 60, 60, 690, wall_texture),
             Wall(570, 90, 60, 690, wall_texture), Wall(660, 60, 60, 690, wall_texture),
             Wall(750, 90, 60, 690, wall_texture), Wall(840, 60, 60, 690, wall_texture),
             Wall(930, 90, 60, 690, wall_texture), Wall(1020, 60, 60, 690, wall_texture),
             Wall(1110, 90, 60, 690, wall_texture), Wall(1200, 60, 60, 690, wall_texture),
             Wall(1290, 90, 60, 690, wall_texture), Wall(1380, 60, 60, 690, wall_texture),
             Wall(1440, 60, 95, 360, wall_texture), Wall(1440, 420, 60, 30, wall_texture),
             Wall(1470, 480, 30, 30, wall_texture), Wall(1470, 510, 65, 270, wall_texture),
             Wall(0, 780, 1535, 83, wall_texture)]

    # Hidden walls that change maps
    # These invisible walls act as triggers to transition between different maps :
    # - (x, y): Top-left corner coordinates
    # - Width and height of the trigger area
    # - InvisibleWall objects handle map transitions
    mp = [InvisibleWall(1533, 420, 2, 90), InvisibleWall(0, 240, 2, 90)]

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

        # player collide check with walls
        player.check_collision(walls)

        # options for developer mode
        # show position of mouse on screen
        # show player and bots rect and also hidden map changer with blue color
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
            for mp_dev in mp:
                mp_dev.draw(screen, (0, 0, 255))

        # Frame rate
        pygame.time.Clock().tick(240)

        # player collide with map changer
        # return map number and player new position on that map
        # Due to differentiation in player texture length between map09 and other maps
        # subtract from player's x position to ensure no collision with the wall occurs.
        if player.rect.colliderect(mp[0]):
            if player.y > 485:
                player.y -= 7
            return "map02", 3, player.y

        if player.rect.colliderect(mp[1]):
            pass

        # update display
        pygame.display.flip()

    pygame.quit()
