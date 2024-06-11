import pygame
import time
from Bot import Bot

def win():
    # set up screen
    screen_width = 1536
    screen_height = 864
    pygame.display.set_caption('You Win')
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    # Initializes Pygame's mixer module for audio playback.
    pygame.mixer.init()
    # Loads the background music
    pygame.mixer.music.load('assets/win/sound/music.wav')
    # Sets the music to loop indefinitely
    pygame.mixer.music.play(-1)
    # Adjusts the music volume to 20%
    pygame.mixer.music.set_volume(0.2)

    # Makes the mouse cursor visible
    pygame.mouse.set_visible(True)

    win_screen_image = pygame.image.load('assets/win/img/win.jpg')
    win_screen_image = pygame.transform.scale(win_screen_image, (1536, 864))

    # Initial positions of text and buttons (off the screen at the bottom)
    start_y = 864
    end_y = 170

    # Positions for text and buttons
    text_position = start_y
    button_positions = [start_y + i * 80 for i in range(3)]  # Spacing between buttons

    # Speed of floating animation
    speed = 5

    def draw_win_screen(screen):
        screen.blit(win_screen_image, (0, 0))  # Draw the win screen image

        # Display the win message
        font = pygame.font.Font(None, 80)
        text = font.render('You Escaped', True, (255, 0, 0))
        text_rect = text.get_rect(midleft=(50, text_position))  # Text floats to the middle left
        screen.blit(text, text_rect)

        # Display the developed by message
        dev_font = pygame.font.Font(None, 36)
        dev_text = dev_font.render('Developed by ArianCSN', True, (255, 255, 255))
        dev_text_rect = dev_text.get_rect(midleft=(50, text_position + 50))  # Below the main text
        screen.blit(dev_text, dev_text_rect)

        # Display the play again button
        try_again_button = pygame.Rect(50, button_positions[0], 200, 50)
        pygame.draw.rect(screen, (42, 89, 26), try_again_button)
        button_font = pygame.font.Font(None, 36)
        button_text = button_font.render('Play Again', True, (255, 255, 255))
        button_text_rect = button_text.get_rect(center=try_again_button.center)
        screen.blit(button_text, button_text_rect)

        # Display the main menu button
        main_menu_button = pygame.Rect(50, button_positions[1], 200, 50)
        pygame.draw.rect(screen, (42, 89, 26), main_menu_button)
        main_menu_text = button_font.render('Main Menu', True, (255, 255, 255))
        main_menu_text_rect = main_menu_text.get_rect(center=main_menu_button.center)
        screen.blit(main_menu_text, main_menu_text_rect)

        # Display the exit button
        exit_button = pygame.Rect(50, button_positions[2], 200, 50)
        pygame.draw.rect(screen, (89, 26, 26), exit_button)
        exit_text = button_font.render('Exit', True, (255, 255, 255))
        exit_text_rect = exit_text.get_rect(center=exit_button.center)
        screen.blit(exit_text, exit_text_rect)

        pygame.display.flip() # Update the display

        return try_again_button, main_menu_button, exit_button

    running = True
    animation_done = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and animation_done:
                if try_again_button.collidepoint(event.pos):
                    sound_effect = pygame.mixer.Sound('assets/win/sound/start.mp3')
                    sound_effect.set_volume(0.2)
                    sound_effect.play()

                    # load music
                    pygame.mixer.music.load('assets/sound/music.wav')
                    # adjust the music volume to 0.4
                    pygame.mixer.music.set_volume(0.4)
                    # loop the music
                    pygame.mixer.music.play(-1)
                    # The play again button was clicked
                    return "map01", 780, 390  # Exit the game over screen

                elif main_menu_button.collidepoint(event.pos):
                    # The main menu button was clicked
                    return "main_menu", 780, 390
                elif exit_button.collidepoint(event.pos):
                    # The exit button was clicked
                    exit()  # Exit the game completely

        if not animation_done:
            text_position = max(text_position - speed, end_y)
            for i in range(3):
                button_positions[i] = max(button_positions[i] - speed, end_y + 80 + i * 80)

            if text_position == end_y and all(pos == end_y + 80 + i * 80 for i, pos in enumerate(button_positions)):
                animation_done = True

        try_again_button, main_menu_button, exit_button = draw_win_screen(screen)
        time.sleep(0.01)  # Adjust to control the speed of the animation
