import pygame
import time
import os
from Ground import Ground
from MyPlayer import MyPlayer
from Wall import Wall
from InvisibleWall import InvisibleWall

# Get the directory of the current script
base_dir = os.path.dirname(os.path.abspath(__file__))


def map11(x_pos, y_pos, developer_mode):
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
    ground_texture = pygame.image.load(os.path.join(base_dir, 'assets/map11/ground/ground.jpg'))

    wall_texture = pygame.image.load(os.path.join(base_dir, 'assets/map11/wall/wall.png'))

    idle = pygame.image.load(os.path.join(base_dir, 'assets/map11/player/idle.png'))

    walk_up = None

    walk_left = [pygame.image.load(os.path.join(base_dir, 'assets/map11/player/L1.png')), pygame.image.load(os.path.join(base_dir, 'assets/map11/player/L2.png')),
                 pygame.image.load(os.path.join(base_dir, 'assets/map11/player/L3.png')), pygame.image.load(os.path.join(base_dir, 'assets/map11/player/L4.png')),
                 pygame.image.load(os.path.join(base_dir, 'assets/map11/player/L5.png')), pygame.image.load(os.path.join(base_dir, 'assets/map11/player/L6.png'))]

    walk_down = None

    walk_right = [pygame.image.load(os.path.join(base_dir, 'assets/map11/player/R1.png')), pygame.image.load(os.path.join(base_dir, 'assets/map11/player/R2.png')),
                  pygame.image.load(os.path.join(base_dir, 'assets/map11/player/R3.png')), pygame.image.load(os.path.join(base_dir, 'assets/map11/player/R4.png')),
                  pygame.image.load(os.path.join(base_dir, 'assets/map11/player/R5.png')), pygame.image.load(os.path.join(base_dir, 'assets/map11/player/R6.png'))]

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

    # Define the walls
    # Each wall is represented by a rectangular area with specific dimensions:
    # - (x, y): Top-left corner coordinates
    # - Width and height of the wall
    # - Texture (wall_texture) used for rendering
    walls = [Wall(0, 0, 420, 90, wall_texture), Wall(0, 240, 240, 624, wall_texture),
             Wall(420, 0, 570, 864, wall_texture), Wall(1140, 0, 396, 360, wall_texture),
             Wall(1140, 480, 396, 384, wall_texture)]

    # Hidden walls that change maps
    # These invisible walls act as triggers to transition between different maps :
    # - (x, y): Top-left corner coordinates
    # - Width and height of the trigger area
    # - InvisibleWall objects handle map transitions
    mp = [InvisibleWall(990, 0, 150, 2), InvisibleWall(1534, 360, 2, 120),
          InvisibleWall(990, 862, 150, 2), InvisibleWall(240, 862, 180, 2),
          InvisibleWall(0, 90, 2, 150)]

    # Teleports that teleports you
    # These rects act as triggers to teleport from one point to another :
    # - (x, y): Top-left corner coordinates
    # - Width and height of the trigger area
    # - Teleports objects handle teleportation
    tps = [InvisibleWall(419, 90, 1, 150), InvisibleWall(990, 360, 1, 120)]

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

        # Draw the walls
        for wall in walls:
            wall.draw(scaled_surface)

        # Teleportation Logic
        if player.rect.colliderect(tps[0]):

            player.x = 992
            player.y = 390

            # Play teleportation sound effect
            sound_effect = pygame.mixer.Sound(os.path.join(base_dir, 'assets/map11/sound/teleport.wav'))
            sound_effect.set_volume(0.2)
            sound_effect.play()

        # Second teleportation
        if player.rect.colliderect(tps[1]):

            player.x = 386
            player.y = 150

            # Play teleportation sound effect
            sound_effect = pygame.mixer.Sound(os.path.join(base_dir, 'assets/map11/sound/teleport.wav'))
            sound_effect.set_volume(0.2)
            sound_effect.play()

        # player collide check with walls
        player.check_collision(walls)

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
            scaled_surface.blit(font.render(f"Developer Mode - Map11", True, (255, 0, 0)), (10, 5))
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

                for tp in tps:
                    tp.draw(scaled_surface, (111, 49, 152))

                for mp_dev in mp:
                    mp_dev.draw(scaled_surface, (0, 0, 255))

                for wall in walls:
                    wall.rect_draw(scaled_surface, (0, 255, 0))

            if not view_toggle:
                scaled_surface.blit(font.render('Player View', True, (255, 0, 0)), (10, 85))

        # Draw the scaled surface on the screen with scaling and centering
        screen.fill((0, 0, 0))
        scaled_screen = pygame.transform.scale(scaled_surface, (scaled_width, scaled_height))
        screen.blit(scaled_screen, (offset_x, offset_y))

        # Frame rate
        pygame.time.Clock().tick(30)

        # player collide with map changer
        # return map number and player new position on that map
        # Due to differentiation in player texture length between map11 and other maps
        # subtract from player's x position to ensure no collision with the wall occurs.
        if player.rect.colliderect(mp[0]):
            return "map22", player.x, 827

        if player.rect.colliderect(mp[2]):
            return "map15", 720, 120

        if player.rect.colliderect(mp[3]):
            return "map15", 300, 92

        if player.rect.colliderect(mp[4]):
            if player.y > 206:
                player.y -= 2
            return "map06", 1498, player.y

        # update display
        pygame.display.flip()

    pygame.quit()
