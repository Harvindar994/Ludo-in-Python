import pygame
import sys
pygame.init()

# Creating Game screen.
Game_Window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Ludo')

# Image Loading
Game_background = pygame.image.load('Media/Image/background.png')

# Global variables.
Mouse_x = 0
Mouse_y = 0


def close_game():
    pygame.quit()
    sys.exit()

# Main menu Creation.


while True:
    for event in pygame.event.get():
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            close_game()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse X : ", Mouse_x)
            print("Mouse Y : ", Mouse_y)

    Game_Window.blit(Game_background, [0, 0])
    pygame.display.update()
