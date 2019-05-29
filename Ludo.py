import pygame
import sys
import pymongo
pygame.init()


# Global color Class.
class Colors:
    white = (255, 255, 255)
    orange = (252, 82, 59)
    light_black = (43, 43, 43)
    light_gray = (166, 166, 166)


# class for defining path and position of ballast.
class Ballast:
    def __int__(self, color):
        pass

    def create_path(self):
        pass

    def move(self):
        pass

    def check_location(self):
        pass


class Elements:
    def __int__(self):
        pass


# Creating Game screen.
Game_Window = pygame.display.set_mode((920, 689))
pygame.display.set_caption('Ludo')

# Image Loading
Game_background = pygame.image.load('Media/Image/background.png')


# Global variables.
Mouse_x = 0
Mouse_y = 0
event = None
colors_rb = Colors()


def close_game():
    pygame.quit()
    sys.exit()

# Temp Function to define screen objects.


def selecter(x, y, mouse_x, mouse_y, color=colors_rb.white):
    pygame.draw.rect(Game_Window, color, [x, y, mouse_x-x, mouse_y-y], 1)


def drow_circule(x, y, redouis, color=colors_rb.light_black):
    pygame.draw.circle(Game_Window, color, [x, y], redouis)


def define_pos(image):
    global colors_rb
    global event
    global Mouse_y, Mouse_x
    flag = False
    rect = True
    circle = False
    file_name = input("Enter File Name : ")
    file = open(file_name, 'a')
    position = ''
    x = 0
    y = 0
    Mouse_x = 0
    Mouse_y = 0
    while True:
        for event in pygame.event.get():
            Mouse_x, Mouse_y = pygame.mouse.get_pos()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_c:
                    circle = True
                    rect = False
                if event.key == pygame.K_r:
                    circle = False
                    rect = True
                if event.key == pygame.K_s:
                    file.write('\n'+position)
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if flag:
                    print("Mouse X : ", Mouse_x)
                    print("Mouse Y : ", Mouse_y)
                    position = '['+str(x)+','+str(y)+','+str(Mouse_x)+','+str(Mouse_y)+']'
                    flag = False
                else:
                    position = ''
                    flag = True
                    print("POS X : ", x)
                    print("POS Y : ", y)

        Game_Window.blit(image, [0, 0])
        if flag and rect:
            selecter(x, y, Mouse_x, Mouse_y, colors_rb.light_black)
        if flag and circle:
            drow_circule(Mouse_x, Mouse_y, 10)
        pygame.display.update()

# Main menu Creation.


while True:
    for event in pygame.event.get():
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            close_game()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse X : ", Mouse_x)
            print("Mouse Y : ", Mouse_y)

    define_pos(Game_background)
    Game_Window.fill(colors_rb.white)
    Game_Window.blit(Game_background, [0, 0])
    pygame.draw.rect(Game_Window, colors_rb.light_gray, (0, 0, 690, 689), 1)
    pygame.display.update()
