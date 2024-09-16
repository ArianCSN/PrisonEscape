import random
import time
import pygame
import os
from Ground import Ground
from MyPlayer import MyPlayer
from Wall import Wall
from InvisibleWall import InvisibleWall

# Get the directory of the current script
base_dir = os.path.dirname(os.path.abspath(__file__))


def map16(x_pos, y_pos, developer_mode):
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
    ground_texture = pygame.image.load(os.path.join(base_dir, 'assets/map16/ground/ground.jpg'))

    wall_texture = pygame.image.load(os.path.join(base_dir, 'assets/map16/wall/wall.png'))

    idle = pygame.image.load(os.path.join(base_dir, 'assets/map16/player/idle.png'))

    walk_up = None

    walk_left = [pygame.image.load(os.path.join(base_dir, 'assets/map16/player/L1.png')), pygame.image.load(os.path.join(base_dir, 'assets/map16/player/L2.png')),
                 pygame.image.load(os.path.join(base_dir, 'assets/map16/player/L3.png')), pygame.image.load(os.path.join(base_dir, 'assets/map16/player/L4.png')),
                 pygame.image.load(os.path.join(base_dir, 'assets/map16/player/L5.png')), pygame.image.load(os.path.join(base_dir, 'assets/map16/player/L6.png'))]

    walk_down = None

    walk_right = [pygame.image.load(os.path.join(base_dir, 'assets/map16/player/R1.png')), pygame.image.load(os.path.join(base_dir, 'assets/map16/player/R2.png')),
                  pygame.image.load(os.path.join(base_dir, 'assets/map16/player/R3.png')), pygame.image.load(os.path.join(base_dir, 'assets/map16/player/R4.png')),
                  pygame.image.load(os.path.join(base_dir, 'assets/map16/player/R5.png')), pygame.image.load(os.path.join(base_dir, 'assets/map16/player/R6.png'))]

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
    walls = [Wall(0, 0, 720, 240, wall_texture), Wall(840, 0, 696, 240, wall_texture),
             Wall(0, 360, 360, 240, wall_texture), Wall(1200, 360, 336, 240, wall_texture),
             Wall(360, 360, 60, 504, wall_texture), Wall(1140, 360, 60, 504, wall_texture),
             Wall(0, 720, 240, 144, wall_texture), Wall(1320, 720, 216, 144, wall_texture),
             Wall(420, 630, 300, 234, wall_texture), Wall(840, 630, 300, 234, wall_texture)]

    # Hidden walls that change maps
    # These invisible walls act as triggers to transition between different maps :
    # - (x, y): Top-left corner coordinates
    # - Width and height of the trigger area
    # - InvisibleWall objects handle map transitions
    mp = [InvisibleWall(720, 0, 120, 2), InvisibleWall(1534, 240, 2, 120),
          InvisibleWall(1534, 600, 2, 120), InvisibleWall(1200, 862, 120, 2),
          InvisibleWall(720, 862, 120, 2), InvisibleWall(240, 862, 120, 2),
          InvisibleWall(0, 600, 2, 120), InvisibleWall(0, 240, 2, 120)]

    # Teleports that teleports you
    # These rects act as triggers to teleport from one point to another :
    # - (x, y): Top-left corner coordinates
    # - Width and height of the trigger area
    # - Teleports objects handle teleportation
    tps = [InvisibleWall(690, 390, 180, 120)]

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

        # Draw the Teleport Areas
        for tp in tps:
            tp.draw(scaled_surface, (111, 49, 152))

        # initialized the font
        font = pygame.font.SysFont("", 24)

        # Text lines for the teleportation room description
        teleport_lines = [
            "Teleportation Room",
            "You can use the teleporter in this room to randomly teleport.",
            "There's a 4% chance of getting trapped upon teleportation.",
            "Additionally, there's a 4% chance of teleporting to exit room."
        ]

        # Blit the text lines onto the screen
        for i, line in enumerate(teleport_lines):
            scaled_surface.blit(font.render(line, True, (255, 0, 0)), (454, 260 + i * 20))

        # Teleportation Logic
        if player.rect.colliderect(tps[0]):

            random_tp = [
                ["map01", 66, 390],
                ["map02", 224, 449],
                ["map03", 1087, 860],
                ["map04", 1417, 220],
                ["map05", 32, 370],
                ["map06", 1265, 144],
                ["map07", 807, 800],
                ["map08", 23, 106],
                ["map09", 20, 274],
                ["map10", 257, 283],
                ["map11", 1052, 405],
                ["map12", 1322, 641],
                ["map13", 813, 575],
                ["map14", 755, 305],
                ["map15", 721, 124],
                ["map16", 1253, 650],
                ["map17", 681, 576],
                ["map18", 1481, 398],
                ["map19", 768, 384],
                ["map20", 723, 651],
                ["map21", 603, 287],
                ["map22", 1038, 385],
                ["map23", 106, 286],
                ["map24", 1368, 787],
                ["map25", 977, 597],
                # trapped
                ["map02", 921, 484],
                # exit room
                ["map25", 786, 243]
            ]

            # randomly picked one of the maps
            randomize = random.choice(random_tp)

            # Play teleportation sound effect
            if randomize == ["map02", 921, 484]:
                sound_effect = pygame.mixer.Sound(os.path.join(base_dir, 'assets/map16/sound/trapped.wav'))
                sound_effect.set_volume(1)
                sound_effect.play()
            elif randomize == ["map25", 786, 243]:
                sound_effect = pygame.mixer.Sound(os.path.join(base_dir, 'assets/map16/sound/lucky.mp3'))
                sound_effect.set_volume(1)
                sound_effect.play()
            else:
                sound_effect = pygame.mixer.Sound(os.path.join(base_dir, 'assets/map16/sound/teleport.wav'))
                sound_effect.set_volume(1)
                sound_effect.play()

            # Create a white flash effect (you can adjust the duration and intensity)
            flash_surface = pygame.Surface(screen.get_size())
            flash_surface.fill((255, 255, 255))  # White color
            flash_surface.set_alpha(100)  # Adjust transparency (0 to 255)
            scaled_surface.blit(flash_surface, (0, 0))
            pygame.display.flip()

            return randomize

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
            scaled_surface.blit(font.render(f"Developer Mode - Map16", True, (255, 0, 0)), (10, 5))
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
        # Due to differentiation in player texture length between map03 and other maps
        # subtract from player's x position to ensure no collision with the wall occurs.
        if player.rect.colliderect(mp[0]):
            if player.x > 776:
                player.x -= 9
            return "map04", player.x, 826

        if player.rect.colliderect(mp[1]):
            if player.y > 300:
                player.y -= 1
            return "map12", 3, player.y

        if player.rect.colliderect(mp[2]):
            if player.y > 660:
                player.y -= 1
            return "map12", 3, player.y

        if player.rect.colliderect(mp[6]):
            if player.y > 660:
                player.y -= 2
            return "map20", 1511, player.y

        if player.rect.colliderect(mp[7]):
            if player.y > 300:
                player.y -= 2
            return "map20", 1511, player.y

        # update display
        pygame.display.flip()

    pygame.quit()
