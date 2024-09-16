import pygame
import sys
import os

# Get the directory of the current script
base_dir = os.path.dirname(os.path.abspath(__file__))


def game_over():
    # Native resolution of the game over screen
    screen_width = 1536
    screen_height = 864
    aspect_ratio = screen_width / screen_height

    # Get current screen resolution
    screen_info = pygame.display.Info()
    current_screen_width = screen_info.current_w
    current_screen_height = screen_info.current_h
    current_aspect_ratio = current_screen_width / current_screen_height

    # Calculate the scale factor and determine scaled dimensions
    if current_aspect_ratio >= aspect_ratio:
        scale_factor = current_screen_height / screen_height
        scaled_width = int(screen_width * scale_factor)
        scaled_height = current_screen_height
        offset_x = (current_screen_width - scaled_width) // 2
        offset_y = 0
    else:
        scale_factor = current_screen_width / screen_width
        scaled_width = current_screen_width
        scaled_height = int(screen_height * scale_factor)
        offset_x = 0
        offset_y = (current_screen_height - scaled_height) // 2

    # Set up Pygame window
    pygame.display.set_caption('Game Over')
    screen = pygame.display.set_mode((current_screen_width, current_screen_height), pygame.FULLSCREEN)

    # Makes the mouse cursor visible
    pygame.mouse.set_visible(True)

    game_over_running = True
    while game_over_running:
        # Draw everything on a scaled surface
        scaled_surface = pygame.Surface((screen_width, screen_height))
        scaled_surface.fill((0, 0, 0))  # Clear the screen

        # Scaling fonts and buttons
        font_size = int(80 * scale_factor)
        button_font_size = int(36 * scale_factor)

        # Display the game over message
        font = pygame.font.Font(None, font_size)
        text = font.render('Game Over', True, (255, 0, 0))
        text_rect = text.get_rect(center=(screen_width / 2, screen_height / 2 - 100))
        scaled_surface.blit(text, text_rect)

        # Try Again button
        try_again_button = pygame.Rect(screen_width / 2 - 100, screen_height / 2, 200, 50)
        pygame.draw.rect(scaled_surface, (42, 89, 26), try_again_button)
        button_font = pygame.font.Font(None, button_font_size)
        button_text = button_font.render('Try Again', True, (255, 255, 255))
        button_text_rect = button_text.get_rect(center=try_again_button.center)
        scaled_surface.blit(button_text, button_text_rect)

        # Main Menu button
        main_menu_button = pygame.Rect(screen_width / 2 - 100, screen_height / 2 + 80, 200, 50)
        pygame.draw.rect(scaled_surface, (42, 89, 26), main_menu_button)
        main_menu_text = button_font.render('Main Menu', True, (255, 255, 255))
        main_menu_text_rect = main_menu_text.get_rect(center=main_menu_button.center)
        scaled_surface.blit(main_menu_text, main_menu_text_rect)

        # Exit button
        exit_button = pygame.Rect(screen_width / 2 - 100, screen_height / 2 + 160, 200, 50)
        pygame.draw.rect(scaled_surface, (89, 26, 26), exit_button)
        exit_text = button_font.render('Exit', True, (255, 255, 255))
        exit_text_rect = exit_text.get_rect(center=exit_button.center)
        scaled_surface.blit(exit_text, exit_text_rect)

        # Scale the surface and blit it to the screen with an offset
        scaled_surface = pygame.transform.scale(scaled_surface, (scaled_width, scaled_height))
        screen.blit(scaled_surface, (offset_x, offset_y))

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Adjust mouse position to match the scaled surface
                mouse_x = (event.pos[0] - offset_x) / scale_factor
                mouse_y = (event.pos[1] - offset_y) / scale_factor
                if try_again_button.collidepoint((mouse_x, mouse_y)):
                    sound_effect = pygame.mixer.Sound(os.path.join(base_dir, 'assets/main_menu/sound/start.mp3'))
                    sound_effect.set_volume(0.2)
                    sound_effect.play()

                    # load music
                    pygame.mixer.music.load(os.path.join(base_dir, 'assets/sound/music.wav'))
                    pygame.mixer.music.set_volume(0.4)
                    pygame.mixer.music.play(-1)

                    # The try again button was clicked
                    return "map01", 780, 390  # Exit the game over screen
                elif main_menu_button.collidepoint((mouse_x, mouse_y)):
                    # The main menu button was clicked
                    return "main_menu", 780, 390  # Exit the game over screen
                elif exit_button.collidepoint((mouse_x, mouse_y)):
                    # The exit button was clicked
                    exit()  # Exit the game completely

        # Update the display
        pygame.display.flip()
