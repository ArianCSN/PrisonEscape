import pygame
import time

def win():
    # Native resolution of the win screen
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
    pygame.display.set_caption('You Win')
    screen = pygame.display.set_mode((current_screen_width, current_screen_height), pygame.FULLSCREEN)

    # Initializes Pygame's mixer module for audio playback.
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(base_dir, 'assets/win/sound/music.wav'))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

    pygame.mouse.set_visible(True)

    # Load and scale the win screen background image
    win_screen_image = pygame.image.load(os.path.join(base_dir, 'assets/win/img/win.jpg'))
    win_screen_image = pygame.transform.scale(win_screen_image, (scaled_width, scaled_height))

    # Initial positions of text and buttons (off the screen at the bottom)
    start_y = scaled_height
    end_y = int(170 * scale_factor)

    # Positions for text and buttons
    text_position = start_y
    button_positions = [start_y + i * int(80 * scale_factor) for i in range(3)]

    # Speed of floating animation
    speed = 5 * scale_factor

    # Font scaling
    font_size = int(80 * scale_factor)
    button_font_size = int(36 * scale_factor)
    dev_font_size = int(36 * scale_factor)

    def draw_win_screen(scaled_surface):
        scaled_surface.blit(win_screen_image, (0, 0))  # Draw the win screen image

        # Display the win message
        font = pygame.font.Font(None, font_size)
        text = font.render('You Escaped', True, (255, 0, 0))
        text_rect = text.get_rect(midleft=(int(50 * scale_factor), text_position))
        scaled_surface.blit(text, text_rect)

        # Display the developed by message
        dev_font = pygame.font.Font(None, dev_font_size)
        dev_text = dev_font.render('Developed by ArianCSN', True, (255, 255, 255))
        dev_text_rect = dev_text.get_rect(midleft=(int(50 * scale_factor), text_position + int(50 * scale_factor)))
        scaled_surface.blit(dev_text, dev_text_rect)

        # Display the play again button
        try_again_button = pygame.Rect(int(50 * scale_factor), button_positions[0], int(200 * scale_factor), int(50 * scale_factor))
        pygame.draw.rect(scaled_surface, (42, 89, 26), try_again_button)
        button_font = pygame.font.Font(None, button_font_size)
        button_text = button_font.render('Play Again', True, (255, 255, 255))
        button_text_rect = button_text.get_rect(center=try_again_button.center)
        scaled_surface.blit(button_text, button_text_rect)

        # Display the main menu button
        main_menu_button = pygame.Rect(int(50 * scale_factor), button_positions[1], int(200 * scale_factor), int(50 * scale_factor))
        pygame.draw.rect(scaled_surface, (42, 89, 26), main_menu_button)
        main_menu_text = button_font.render('Main Menu', True, (255, 255, 255))
        main_menu_text_rect = main_menu_text.get_rect(center=main_menu_button.center)
        scaled_surface.blit(main_menu_text, main_menu_text_rect)

        # Display the exit button
        exit_button = pygame.Rect(int(50 * scale_factor), button_positions[2], int(200 * scale_factor), int(50 * scale_factor))
        pygame.draw.rect(scaled_surface, (89, 26, 26), exit_button)
        exit_text = button_font.render('Exit', True, (255, 255, 255))
        exit_text_rect = exit_text.get_rect(center=exit_button.center)
        scaled_surface.blit(exit_text, exit_text_rect)

        pygame.display.flip()  # Update the display

        return try_again_button, main_menu_button, exit_button

    running = True
    animation_done = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and animation_done:
                # Scale the mouse position to the original coordinate space
                mouse_x = (event.pos[0] - offset_x) / scale_factor
                mouse_y = (event.pos[1] - offset_y) / scale_factor
                if try_again_button.collidepoint((mouse_x, mouse_y)):
                    sound_effect = pygame.mixer.Sound(os.path.join(base_dir, 'assets/win/sound/start.mp3'))
                    sound_effect.set_volume(0.2)
                    sound_effect.play()

                    # load music
                    pygame.mixer.music.load(os.path.join(base_dir, 'assets/sound/music.wav'))
                    pygame.mixer.music.set_volume(0.4)
                    pygame.mixer.music.play(-1)
                    return "map01", 780, 390  # Exit the win screen

                elif main_menu_button.collidepoint((mouse_x, mouse_y)):
                    return "main_menu", 780, 390

                elif exit_button.collidepoint((mouse_x, mouse_y)):
                    exit()  # Exit the game completely

        if not animation_done:
            text_position = max(text_position - speed, end_y)
            for i in range(3):
                button_positions[i] = max(button_positions[i] - speed, end_y + int(80 * scale_factor) + i * int(80 * scale_factor))

            if text_position == end_y and all(pos == end_y + int(80 * scale_factor) + i * int(80 * scale_factor) for i, pos in enumerate(button_positions)):
                animation_done = True

        # Draw everything on a scaled surface
        scaled_surface = pygame.Surface((scaled_width, scaled_height))
        try_again_button, main_menu_button, exit_button = draw_win_screen(scaled_surface)

        # Clear the screen and draw the scaled surface centered
        screen.fill((0, 0, 0))
        screen.blit(scaled_surface, (offset_x, offset_y))

        time.sleep(0.01)  # Adjust to control the speed of the animation

    pygame.quit()
