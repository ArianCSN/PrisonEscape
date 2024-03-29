import pygame
import sys

# Initialize Pygame
pygame.init()

screen_width = 800
screen_height = 600
# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Main menu')


# Main menu loop
def main_menu():
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

        # Draw the hidden "Developer Mode" button
        dev_mode_button = pygame.Rect(790, 589, 200, 50)
        pygame.draw.rect(screen, (0, 0, 0), dev_mode_button)

        # Draw the "Exit" button
        exit_button = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 80, 200, 50)
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
                    # Start the game
                    return "01", 0
                elif dev_mode_button.collidepoint(mouse_pos):
                    # Toggle developer mode
                    return "01", 1
                elif exit_button.collidepoint(mouse_pos):
                    # Exit the game
                    exit()

        # Update the display
        pygame.display.flip()
