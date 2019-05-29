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
Ballast_img = [pygame.image.load('Media/Image/ballast/B1.png'), pygame.image.load('Media/Image/ballast/B2.png'), pygame.image.load('Media/Image/ballast/B3.png'), pygame.image.load('Media/Image/ballast/B4.png'), pygame.image.load('Media/Image/ballast/B5.png'), pygame.image.load('Media/Image/ballast/B6.png'), pygame.image.load('Media/Image/ballast/B7.png'), pygame.image.load('Media/Image/ballast/B8.png')]


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

def verify_position():
    global colors_rb
    fp = open('position.txt', 'r')
    data = ''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    data = fp.readline()
                    if data == '':
                        return
                    data = data[1:len(data)-2]
                    data = data.split(',')
                    print(data)
                    data = [int(e) for e in data]
                    x, y, x1, y1 = data
            if event.type == pygame.QUIT:
                close_game()

        Game_Window.blit(Game_background, [0, 0])
        if data != '':
            pygame.draw.rect(Game_Window, colors_rb.light_black, [x, y, x1-x, y1-y])
        pygame.display.update()

def insert_location(file_name, location):
    fp = open(file_name, 'a')
    fp.write(location)
    fp.close()


def define_pos(image):
    global colors_rb
    global event
    global Mouse_y, Mouse_x
    flag = False
    rect = True
    circle = False
    file_name = input("Enter File Name : ")
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
                if event.key == pygame.K_s and position != '':
                    insert_location(file_name, '\n'+position)
                    position = ''

            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if flag:
                    print("Mouse X : ", Mouse_x)
                    print("Mouse Y : ", Mouse_y)
                    position = '['+str(x)+','+str(y)+','+str(Mouse_x)+','+str(Mouse_y)+']'
                    flag = False
                else:
                    x, y = pygame.mouse.get_pos()
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


def do_bet_1(x, y):
    value = 7
    count = 0
    while count <= value:
        Game_Window.blit(Ballast_img[count], [x, y])
        pygame.time.Clock().tick(30)
        count += 1
        yield count


def do_bet():
    global Game_Window
    global Game_background
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    count = 0
        Game_Window.blit(Game_background, [0, 0])
        if count < 8:
            Game_Window.blit(Ballast_img[count], [25, 508])
            pygame.time.Clock().tick(30)
            count += 1
        else:
            Game_Window.blit(Ballast_img[0], [25, 508])

        pygame.display.update()

# Main menu Creation.

flag = False
while True:
    for event in pygame.event.get():
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            close_game()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse X : ", Mouse_x)
            print("Mouse Y : ", Mouse_y)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                bet_itr = do_bet_1(25, 508)
                flag = True

    Game_Window.fill(colors_rb.white)
    Game_Window.blit(Game_background, [0, 0])
    if flag:
        try:
            next(bet_itr)
        except:
            flag = False
    else:
        Game_Window.blit(Ballast_img[0], [25, 508])
    pygame.display.update()
