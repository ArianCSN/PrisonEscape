import pygame
import time
import random
import os
from Ground import Ground
from MyPlayer import MyPlayer
from Wall import Wall
from InvisibleWall import InvisibleWall

# Get the directory of the current script
base_dir = os.path.dirname(os.path.abspath(__file__))


def map13(x_pos, y_pos, developer_mode):
    # start the pygame and pygame mixer
    pygame.init()
    pygame.mixer.init()

    # Native resolution of the map
    map_width = 1536
    map_height = 864
    map_aspect_ratio = map_width / map_height

    # Get screen resolution
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h
    screen_aspect_ratio = screen_width / screen_height

    if screen_aspect_ratio >= map_aspect_ratio:
        scale_factor = screen_height / map_height
        scaled_width = int(map_width * scale_factor)
        scaled_height = screen_height
        offset_x = (screen_width - scaled_width) // 2
        offset_y = 0
    else:
        scale_factor = screen_width / map_width
        scaled_width = screen_width
        scaled_height = int(map_height * scale_factor)
        offset_x = 0
        offset_y = (screen_height - scaled_height) // 2

    # Create a scaled surface
    scaled_surface = pygame.Surface((map_width, map_height))

    # Set up the screen to full resolution
    pygame.display.set_caption('Prison Escape')
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    # Hide the mouse cursor
    if not developer_mode:
        pygame.mouse.set_visible(False)

    # flag for toggle between player view and developer view
    view_toggle = True

    # load texture
    ground_texture = pygame.image.load(os.path.join(base_dir, 'assets/map13/ground/ground.jpg'))

    wall_texture = pygame.image.load(os.path.join(base_dir, 'assets/map13/wall/wall.png'))

    idle = pygame.image.load(os.path.join(base_dir, 'assets/map13/player/idle.png'))

    walk_up = None

    walk_left = [pygame.image.load(os.path.join(base_dir, 'assets/map13/player/L1.png')), pygame.image.load(os.path.join(base_dir, 'assets/map13/player/L2.png')),
                 pygame.image.load(os.path.join(base_dir, 'assets/map13/player/L3.png')), pygame.image.load(os.path.join(base_dir, 'assets/map13/player/L4.png')),
                 pygame.image.load(os.path.join(base_dir, 'assets/map13/player/L5.png')), pygame.image.load(os.path.join(base_dir, 'assets/map13/player/L6.png'))]

    walk_down = None

    walk_right = [pygame.image.load(os.path.join(base_dir, 'assets/map13/player/R1.png')), pygame.image.load(os.path.join(base_dir, 'assets/map13/player/R2.png')),
                  pygame.image.load(os.path.join(base_dir, 'assets/map13/player/R3.png')), pygame.image.load(os.path.join(base_dir, 'assets/map13/player/R4.png')),
                  pygame.image.load(os.path.join(base_dir, 'assets/map13/player/R5.png')), pygame.image.load(os.path.join(base_dir, 'assets/map13/player/R6.png'))]

    # define the ground
    ground = Ground(map_width, map_height, ground_texture)

    # Create the player character
    # The player is represented by an instance of the MyPlayer class:
    # - (x_pos, y_pos): Initial position on the screen
    # - screen: Pygame screen object
    # - Textures for different directions (walk_up, walk_left, walk_down, walk_right, idle)
    # - Speed (5th input): Controls how fast the player moves (higher values mean faster movement)
    # - developer_mode: A flag indicating whether to enable developer-specific features
    player = MyPlayer(x_pos, y_pos, scaled_surface, walk_up, walk_left, walk_down, walk_right, idle, 5, developer_mode)

    # Adjust the player's rectangle size to prevent it from getting stuck at the edges
    player.rect = pygame.Rect(x_pos, y_pos, 20, 22)

    # Define the walls
    # Each wall is represented by a rectangular area with specific dimensions:
    # - (x, y): Top-left corner coordinates
    # - Width and height of the wall
    # - Texture (wall_texture) used for rendering
    walls = [Wall(0, 0, 1536, 60, wall_texture), Wall(0, 60, 270, 120, wall_texture),
             Wall(0, 180, 60, 684, wall_texture), Wall(60, 210, 240, 360, wall_texture),

             Wall(60, 600, 60, 264, wall_texture), Wall(120, 600, 270, 60, wall_texture),
             Wall(150, 690, 270, 60, wall_texture), Wall(120, 780, 570, 84, wall_texture),

             Wall(300, 90, 330, 150, wall_texture), Wall(330, 270, 300, 180, wall_texture),
             Wall(330, 450, 60, 210, wall_texture), Wall(420, 480, 240, 90, wall_texture),

             Wall(420, 570, 180, 180, wall_texture), Wall(630, 720, 60, 60, wall_texture),
             Wall(630, 600, 180, 120, wall_texture), Wall(690, 810, 30, 54, wall_texture),

             Wall(660, 60, 150, 510, wall_texture), Wall(840, 90, 30, 480, wall_texture),
             Wall(840, 600, 600, 120, wall_texture), Wall(720, 750, 816, 114, wall_texture),

             Wall(870, 540, 540, 30, wall_texture), Wall(1260, 120, 180, 90, wall_texture),
             Wall(1440, 120, 60, 600, wall_texture), Wall(1500, 60, 36, 690, wall_texture),

             Wall(840, 60, 660, 30, wall_texture), Wall(900, 120, 240, 30, wall_texture),
             Wall(870, 180, 240, 30, wall_texture), Wall(900, 240, 240, 30, wall_texture),

             Wall(870, 300, 240, 30, wall_texture), Wall(900, 360, 240, 30, wall_texture),
             Wall(870, 420, 240, 30, wall_texture), Wall(900, 480, 240, 30, wall_texture),

             Wall(1140, 120, 30, 390, wall_texture), Wall(1200, 90, 30, 180, wall_texture),
             Wall(1230, 240, 180, 30, wall_texture), Wall(1170, 300, 210, 30, wall_texture),

             Wall(1200, 390, 30, 60, wall_texture), Wall(1380, 300, 30, 240, wall_texture),
             Wall(1320, 360, 30, 120, wall_texture), Wall(1200, 360, 120, 30, wall_texture),

             Wall(1170, 480, 180, 30, wall_texture), Wall(1230, 420, 60, 30, wall_texture)]

    # Hidden walls that change maps
    # These invisible walls act as triggers to transition between different maps :
    # - (x, y): Top-left corner coordinates
    # - Width and height of the trigger area
    # - InvisibleWall objects handle map transitions
    mp = [InvisibleWall(810, 60, 30, 30), InvisibleWall(1470, 90, 30, 30),
          InvisibleWall(1470, 720, 30, 30), InvisibleWall(690, 780, 30, 30),
          InvisibleWall(60, 570, 30, 30), InvisibleWall(60, 180, 30, 30)]

    # Create eight buttons at different positions
    buttons = [InvisibleWall(1230, 390, 30, 30), InvisibleWall(870, 570, 30, 30),
               InvisibleWall(810, 360, 30, 30), InvisibleWall(750, 720, 30, 30),
               InvisibleWall(690, 720, 30, 30), InvisibleWall(390, 510, 30, 30),
               InvisibleWall(300, 450, 30, 30), InvisibleWall(240, 180, 30, 30)]

    # Create four doors at different positions
    doors = [InvisibleWall(900, 570, 30, 30), InvisibleWall(780, 720, 30, 30),
             InvisibleWall(390, 540, 30, 30), InvisibleWall(270, 180, 30, 30)]

    # main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # clear screen
        scaled_surface.fill((0, 0, 0))

        ground.draw(scaled_surface)

        # key press for player
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            exit()

        player.move(key)

        # Draw the walls , map changers , buttons and doors
        for wall in walls:
            wall.draw(scaled_surface)

        for mp_dev in mp:
            mp_dev.draw(scaled_surface, (0, 0, 255))

        for button in buttons:
            button.draw(scaled_surface, (245, 228, 156))

        for door in doors:
            door.draw(scaled_surface, (156, 90, 60))

        # player collide check with walls and doors
        player.check_collision(walls)
        player.check_collision(doors)

        if player.rect.colliderect(buttons[0]) or player.rect.colliderect(buttons[1]):
            buttons[0].__init__(0, 0, 0, 0)
            buttons[1].__init__(0, 0, 0, 0)
            doors[0].__init__(0, 0, 0, 0)
            sound_effect = pygame.mixer.Sound(os.path.join(base_dir, 'assets/map13/sound/door.wav'))
            sound_effect.set_volume(0.2)
            sound_effect.play()

        if player.rect.colliderect(buttons[2]) or player.rect.colliderect(buttons[3]):
            buttons[2].__init__(0, 0, 0, 0)
            buttons[3].__init__(0, 0, 0, 0)
            doors[1].__init__(0, 0, 0, 0)
            sound_effect = pygame.mixer.Sound(os.path.join(base_dir, 'assets/map13/sound/door.wav'))
            sound_effect.set_volume(0.2)
            sound_effect.play()

        if player.rect.colliderect(buttons[4]) or player.rect.colliderect(buttons[5]):
            buttons[4].__init__(0, 0, 0, 0)
            buttons[5].__init__(0, 0, 0, 0)
            doors[2].__init__(0, 0, 0, 0)
            sound_effect = pygame.mixer.Sound(os.path.join(base_dir, 'assets/map13/sound/door.wav'))
            sound_effect.set_volume(0.2)
            sound_effect.play()

        if player.rect.colliderect(buttons[6]) or player.rect.colliderect(buttons[7]):
            buttons[6].__init__(0, 0, 0, 0)
            buttons[7].__init__(0, 0, 0, 0)
            doors[3].__init__(0, 0, 0, 0)
            sound_effect = pygame.mixer.Sound(os.path.join(base_dir, 'assets/map13/sound/door.wav'))
            sound_effect.set_volume(0.2)
            sound_effect.play()

        # Developer Mode Options:
        # - Display map number
        # - Show mouse position on screen
        # - Show player X and Y coordinates
        # - Show bounding rectangles of all objects when developer view is enabled
        # - Teleport player to mouse position when the space key is pressed
        # - Toggle between player view and developer view using the left-alt key
        if developer_mode:
            font = pygame.font.SysFont("", 24)

            # Get the scaled mouse position
            scaled_mouse_x = (pygame.mouse.get_pos()[0] - offset_x) / scale_factor
            scaled_mouse_y = (pygame.mouse.get_pos()[1] - offset_y) / scale_factor

            # Display developer information on the scaled surface
            scaled_surface.blit(font.render(f"Developer Mode - Map13", True, (255, 0, 0)), (10, 5))
            scaled_surface.blit(font.render(f'X: {scaled_mouse_x:.0f}, Y: {scaled_mouse_y:.0f}', True, (255, 0, 0)),
                                (10, 25))
            scaled_surface.blit(font.render(f'player x : {player.x}', True, (255, 0, 0)), (10, 45))
            scaled_surface.blit(font.render(f'player y : {player.y}', True, (255, 0, 0)), (10, 65))

            # Teleport player to scaled mouse position when the space key is pressed
            if key[pygame.K_SPACE]:
                player.x = scaled_mouse_x
                player.y = scaled_mouse_y

            if key[pygame.K_LALT]:
                time.sleep(0.2)
                if not view_toggle:
                    view_toggle = True
                else:
                    view_toggle = False

            if view_toggle:
                scaled_surface.blit(font.render('Developer View', True, (255, 0, 0)), (10, 85))
                player.draw_rect(scaled_surface)

                for wall in walls:
                    wall.rect_draw(scaled_surface, (0, 255, 0))

            if not view_toggle:
                scaled_surface.blit(font.render('Player View', True, (255, 0, 0)), (10, 85))

        # Draw the scaled surface on the screen with scaling and centering
        screen.fill((0, 0, 0))
        scaled_screen = pygame.transform.scale(scaled_surface, (scaled_width, scaled_height))
        screen.blit(scaled_screen, (offset_x, offset_y))

        # Frame rate
        pygame.time.Clock().tick(60)

        # player collide with map changer
        # return map number and player new position on that map
        if player.rect.colliderect(mp[0]):
            return "map17", random.randint(630, 742), 703

        if player.rect.colliderect(mp[1]):
            return "map08", 3, 90

        if player.rect.colliderect(mp[2]):
            return "map08", 3, 660

        if player.rect.colliderect(mp[3]):
            return "map24", random.randint(694, 784), 3

        # update display
        pygame.display.flip()

    pygame.quit()
