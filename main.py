import pygame
from MyPlayer import MyPlayer
from MyBots import MyBots

pygame.init()
pygame.display.set_caption('Prison Escape')
screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()
player = MyPlayer(400, 300, 50, 50, 255, 0, 0, screen_rect)
bot1 = MyBots(300, 300, 25, 25, 0, 200, 0, screen_rect)
bot2 = MyBots(300, 300, 25, 25, 0, 150, 0, screen_rect)
bot3 = MyBots(300, 300, 25, 25, 0, 0, 200, screen_rect)
bot4 = MyBots(300, 300, 25, 25, 0, 0, 150, screen_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    player.move(key)
    bot1.move()
    bot2.move()
    bot3.move()
    bot4.move()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the Objects
    player.draw(screen)
    bot1.draw(screen)
    bot2.draw(screen)
    bot3.draw(screen)
    bot4.draw(screen)

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
