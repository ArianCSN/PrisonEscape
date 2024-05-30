import pygame
import sys

# Initialize Pygame
pygame.init()

# set up screen
screen_width = 1536
screen_height = 864
pygame.display.set_caption('Main menu')
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)


def main_menu():
    # Initializes Pygame's mixer module for audio playback.
    pygame.mixer.init()
    # Loads the background music
    pygame.mixer.music.load('assets/main_menu/sound/music.mp3')
    # Sets the music to loop indefinitely
    pygame.mixer.music.play(-1)
    # Adjusts the music volume to 20%
    pygame.mixer.music.set_volume(0.2)
    # Makes the mouse cursor visible
    pygame.mouse.set_visible(True)

    # Enters the main menu loop
    menu_running = True
    while menu_running:
        screen.fill((0, 0, 0))  # Clear the screen
        font = pygame.font.Font(None, 80)
        text = font.render('Prison Escape', True, (255, 0, 0))

        # Draw the text
        text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 100))
        screen.blit(text, text_rect)

        # Draw the "Play" button
        play_button = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2, 200, 50)
        pygame.draw.rect(screen, (42, 89, 26), play_button)
        play_font = pygame.font.Font(None, 36)
        play_text = play_font.render('Play', True, (255, 255, 255))
        play_text_rect = play_text.get_rect(center=play_button.center)
        screen.blit(play_text, play_text_rect)

        # Draw the "Exit" button
        exit_button = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 + 80, 200, 50)
        pygame.draw.rect(screen, (89, 26, 26), exit_button)
        exit_font = pygame.font.Font(None, 36)
        exit_text = exit_font.render('Exit', True, (255, 255, 255))
        exit_text_rect = exit_text.get_rect(center=exit_button.center)
        screen.blit(exit_text, exit_text_rect)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # Get the mouse position
                if play_button.collidepoint(mouse_pos):
                    sound_effect = pygame.mixer.Sound('assets/main_menu/sound/start.mp3')
                    sound_effect.set_volume(0.2)
                    sound_effect.play()
                    pygame.mixer.music.stop()

                    # load music
                    pygame.mixer.music.load('assets/sound/music.wav')
                    pygame.mixer.music.set_volume(0.4)
                    pygame.mixer.music.play(-1)

                    # Start the game
                    return "map01", 780, 390, 0

                elif exit_button.collidepoint(mouse_pos):
                    # Exit the game
                    exit()

        # Update the display
        pygame.display.flip()
