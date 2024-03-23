import pygame
import sys


def show_game_over():
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 74)
    # Display the game over message
    screen.fill((0, 0, 0))  # Clear the screen
    text = font.render('Game Over', True, (255, 0, 0))
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text, text_rect)

    # Display the try again button
    try_again_button = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 + 100, 200, 50)
    pygame.draw.rect(screen, (0, 255, 0), try_again_button)
    button_font = pygame.font.Font(None, 36)
    button_text = button_font.render('Try Again', True, (255, 255, 255))
    button_text_rect = button_text.get_rect(center=try_again_button.center)
    screen.blit(button_text, button_text_rect)

    # Display the exit button
    exit_button = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 + 170, 200, 50)
    pygame.draw.rect(screen, (0, 255, 0), exit_button)
    button_font = pygame.font.Font(None, 36)
    button_text = button_font.render('Exit', True, (255, 255, 255))
    button_text_rect = button_text.get_rect(center=exit_button.center)
    screen.blit(button_text, button_text_rect)

    pygame.display.flip()  # Update the display

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if try_again_button.collidepoint(mouse_pos):
                    # The try again button was clicked
                    return  # Exit the game over screen
                if exit_button.collidepoint(mouse_pos):
                    # The exit button was clicked
                    exit()  # Exit the game completely
