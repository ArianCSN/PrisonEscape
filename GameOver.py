import pygame
import sys


def game_over():
    # set up screen
    screen_width = 1536
    screen_height = 864
    pygame.display.set_caption('Game Over')
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    # Makes the mouse cursor visible
    pygame.mouse.set_visible(True)

    # Display the game over message
    font = pygame.font.Font(None, 80)
    screen.fill((0, 0, 0))  # Clear the screen
    text = font.render('Game Over', True, (255, 0, 0))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 100))
    screen.blit(text, text_rect)

    # Display the try again button
    try_again_button = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2, 200, 50)
    pygame.draw.rect(screen, (42, 89, 26), try_again_button)
    button_font = pygame.font.Font(None, 36)
    button_text = button_font.render('Try Again', True, (255, 255, 255))
    button_text_rect = button_text.get_rect(center=try_again_button.center)
    screen.blit(button_text, button_text_rect)

    # Display the main menu button
    main_menu_button = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 + 80, 200, 50)
    pygame.draw.rect(screen, (42, 89, 26), main_menu_button)
    main_menu_font = pygame.font.Font(None, 36)
    main_menu_text = main_menu_font.render('Main menu', True, (255, 255, 255))
    main_menu_text_rect = main_menu_text.get_rect(center=main_menu_button.center)
    screen.blit(main_menu_text, main_menu_text_rect)

    # Display the exit button
    exit_button = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2 + 160, 200, 50)
    pygame.draw.rect(screen, (89, 26, 26), exit_button)
    exit_font = pygame.font.Font(None, 36)
    exit_text = exit_font.render('Exit', True, (255, 255, 255))
    exit_text_rect = exit_text.get_rect(center=exit_button.center)
    screen.blit(exit_text, exit_text_rect)

    pygame.display.flip()  # Update the display

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if try_again_button.collidepoint(mouse_pos):
                    sound_effect = pygame.mixer.Sound('assets/main_menu/sound/start.mp3')
                    sound_effect.set_volume(0.2)
                    sound_effect.play()

                    # load music
                    pygame.mixer.music.load('assets/sound/music.wav')
                    # adjust the music volume to 0.4
                    pygame.mixer.music.set_volume(0.4)
                    # loop the music
                    pygame.mixer.music.play(-1)

                    # The try again button was clicked
                    return "map01", 780, 390  # Exit the game over screen
                if main_menu_button.collidepoint(mouse_pos):
                    # The main menu button was clicked
                    return "main_menu", 780, 390  # Exit the game over screen
                if exit_button.collidepoint(mouse_pos):
                    # The exit button was clicked
                    exit()  # Exit the game completely
