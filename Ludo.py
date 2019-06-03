import pygame
import sys
import random
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
    def __init__(self, color_type):
        if color_type == 'green':
            self.Bet_block = [815, 491, 910, 588]
            self.Movers_ballast = pygame.image.load('Media/Image/Movers_ballast/Green.png')
            self.Home_pos_1 = [596, 482, 652, 536]
            self.Home_pos_2 = [685, 480, 743, 537]
            self.Home_pos_3 = [597, 574, 652, 630]
            self.Home_pos_4 = [686, 573, 743, 631]
            self.Path = ([714, 369, 759, 412], [667, 369, 712, 412], [620, 369, 666, 412], [574, 369, 619, 412],
                         [528, 369, 573, 412],
                         [483, 413, 526, 458], [483, 459, 526, 504], [483, 505, 526, 551], [483, 553, 526, 598],
                         [483, 599, 526, 645], [483, 646, 526, 688],
                         [439, 646, 482, 688],
                         [393, 646, 437, 688], [393, 599, 437, 645], [393, 553, 437, 598], [393, 505, 437, 551],
                         [393, 459, 437, 504], [393, 413, 437, 458],
                         [348, 368, 393, 413], [302, 368, 347, 413], [255, 368, 300, 413], [208, 368, 254, 413],
                         [161, 368, 207, 413], [117, 368, 160, 413],
                         [117, 324, 160, 367],
                         [117, 279, 160, 322], [161, 279, 207, 322], [208, 279, 254, 322], [255, 279, 300, 322],
                         [302, 279, 347, 322], [348, 279, 393, 322],
                         [394, 233, 437, 279], [394, 187, 437, 232], [394, 140, 437, 186], [394, 94, 437, 139],
                         [394, 46, 437, 92], [394, 0, 437, 45],
                         [439, 0, 482, 45],
                         [484, 0, 527, 45], [484, 46, 527, 92], [484, 94, 527, 139], [484, 140, 527, 186],
                         [484, 187, 527, 232], [484, 233, 527, 279],
                         [528, 279, 573, 324], [574, 279, 619, 324], [620, 279, 666, 324], [667, 279, 712, 324],
                         [714, 279, 759, 324], [760, 279, 803, 324],
                         [760, 325, 803, 368], [714, 325, 759, 368], [667, 325, 712, 368], [620, 325, 666, 368],
                         [574, 325, 619, 368], [528, 325, 573, 368])

        elif color_type == 'yellow':
            self.Bet_block = [10, 492, 106, 588]
            self.Movers_ballast = pygame.image.load('Media/Image/Movers_ballast/Yellow.png')
            self.Home_pos_1 = [181, 479, 239, 535]
            self.Home_pos_2 = [268, 479, 326, 535]
            self.Home_pos_3 = [178, 572, 236, 629]
            self.Home_pos_4 = [268, 572, 326, 629]
            self.Path = ([393, 599, 437, 645], [393, 553, 437, 598], [393, 505, 437, 551], [393, 459, 437, 504],
                         [393, 413, 437, 458],
                         [348, 368, 393, 413], [302, 368, 347, 413], [255, 368, 300, 413], [208, 368, 254, 413],
                         [161, 368, 207, 413], [117, 368, 160, 413],
                         [117, 324, 160, 367],
                         [117, 279, 160, 322], [161, 279, 207, 322], [208, 279, 254, 322], [255, 279, 300, 322],
                         [302, 279, 347, 322], [348, 279, 393, 322],
                         [394, 233, 437, 279], [394, 187, 437, 232], [394, 140, 437, 186], [394, 94, 437, 139],
                         [394, 46, 437, 92], [394, 0, 437, 45],
                         [439, 0, 482, 45],
                         [484, 0, 527, 45], [484, 46, 527, 92], [484, 94, 527, 139], [484, 140, 527, 186],
                         [484, 187, 527, 232], [484, 233, 527,  279],
                         [528, 279, 573, 324], [574, 279, 619, 324], [620, 279, 666, 324],  [667, 279, 712, 324],
                         [714, 279, 759, 324], [760, 279, 803, 324],
                         [760, 325, 803, 368],
                         [760, 369, 803, 412], [714, 369, 759, 412], [667, 369, 712, 412], [620, 369, 666, 412],
                         [574, 369, 619, 412], [528, 369, 573, 412],
                         [483, 413, 526, 458], [483, 459, 526, 504], [483, 505, 526, 551], [483, 553, 526, 598],
                         [483, 599, 526, 645], [483, 646, 526, 688],
                         [439, 646, 482, 688], [439, 599, 482, 645], [439, 553, 482, 598], [439, 505, 482, 551],
                         [439, 459, 482, 504], [439, 413, 482, 458])

        elif color_type == 'red':
            self.Bet_block = [9, 61, 105, 158]
            self.Movers_ballast = pygame.image.load('Media/Image/Movers_ballast/Red.png')
            self.Home_pos_1 = [181, 68, 239, 123]
            self.Home_pos_2 = [271, 67, 328, 123]
            self.Home_pos_3 = [182, 160, 238, 216]
            self.Home_pos_4 = [271, 161, 328, 216]
            self.Path = ([161, 279, 207, 322], [208, 279, 254, 322], [255, 279, 300, 322], [302, 279, 347, 322],
                         [348, 279, 393, 322],
                         [394, 233, 437, 279], [394, 187, 437, 232], [394, 140, 437, 186], [394, 94, 437, 139],
                         [394, 46, 437, 92], [394, 0, 437, 45],
                         [439, 0, 482, 45],
                         [484, 0, 527, 45], [484, 46, 527, 92], [484, 94, 527, 139], [484, 140, 527, 186],
                         [484, 187, 527, 232], [484, 233, 527, 279],
                         [528, 279, 573, 324], [574, 279, 619, 324], [620, 279, 666, 324], [667, 279, 712, 324],
                         [714, 279, 759, 324], [760, 279, 803, 324],
                         [760, 325, 803, 368],
                         [760, 369, 803, 412], [714, 369, 759, 412], [667, 369, 712, 412], [620, 369, 666, 412],
                         [574, 369, 619, 412], [528, 369, 573, 412],
                         [483, 413, 526, 458], [483, 459, 526, 504], [483, 505, 526, 551], [483, 553, 526, 598],
                         [483, 599, 526, 645], [483, 646, 526, 688],
                         [439, 646, 482, 688],
                         [393, 646, 437, 688], [393, 599, 437, 645], [393, 553, 437, 598], [393, 505, 437, 551],
                         [393, 459, 437, 504], [393, 413, 437, 458],
                         [348,  368, 393, 413], [302, 368, 347, 413], [255, 368, 300, 413], [208, 368, 254, 413],
                         [161, 368, 207, 413], [117, 368, 160, 413],
                         [117, 324, 160, 367], [161, 324, 207, 367], [208, 324, 254, 367], [255, 324, 300, 367],
                         [302, 324, 347, 367], [348, 324, 393, 367])

        elif color_type == 'blue':
            self.Bet_block = [814, 62, 912, 158]
            self.Movers_ballast = pygame.image.load('Media/Image/Movers_ballast/Blue.png')
            self.Home_pos_1 = [594, 66, 652, 123]
            self.Home_pos_2 = [685, 68, 740, 122]
            self.Home_pos_3 = [594, 161, 650, 217]
            self.Home_pos_4 = [690, 162, 744, 217]
            self.Path = ([484, 46, 527, 92], [484, 94, 527, 139], [484, 140, 527, 186], [484, 187, 527, 232],
                         [484, 233, 527, 279],
                         [528, 279, 573, 324], [574, 279, 619, 324], [620, 279, 666, 324], [667, 279, 712, 324],
                         [714, 279, 759, 324], [760,  279, 803, 324],
                         [760, 325, 803, 368],
                         [760, 369, 803, 412], [714, 369, 759, 412], [667, 369, 712, 412], [620, 369, 666, 412],
                         [574, 369, 619, 412], [528, 369, 573, 412],
                         [483, 413, 526, 458], [483, 459, 526, 504], [483, 505, 526, 551], [483, 553, 526, 598],
                         [483, 599, 526, 645], [483, 646, 526, 688],
                         [439, 646, 482, 688],
                         [393, 646, 437, 688], [393, 599, 437, 645], [393, 553, 437, 598], [393, 505, 437, 551],
                         [393, 459, 437, 504], [393, 413, 437, 458],
                         [348, 368, 393, 413], [302, 368, 347, 413], [255, 368, 300, 413], [208, 368, 254, 413],
                         [161, 368, 207, 413], [117, 368, 160, 413],
                         [117, 324, 160, 367],
                         [117, 279, 160, 322], [161, 279, 207, 322], [208, 279, 254, 322], [255, 279, 300, 322],
                         [302, 279, 347, 322], [348, 279, 393, 322],
                         [394, 233, 437, 279], [394, 187, 437, 232], [394, 140, 437, 186], [394, 94, 437, 139],
                         [394, 46, 437, 92], [394, 0, 437, 45],
                         [439, 0, 482, 45], [439, 46, 482, 92], [439, 94, 482, 139], [439, 140, 482, 186],
                         [439, 187, 482, 232], [439, 233, 482, 279])

        self.Movers_pos_1 = 'home'
        self.Movers_pos_2 = 'home'
        self.Movers_pos_3 = 'home'
        self.Movers_pos_4 = 'home'
        self.color_type = color_type
        self.Bet_status = True
        self.Bet_flag = False
        self.Bet_itration = None
        self.last_bet_number = None

    @staticmethod
    def get_med_position(rect):
        x, y, x1, y1 = rect
        width = x1 - x
        height = y1 - y
        return [int(x+(width/2)), int(y+(height/2))]

    def print_movers_ballast(self):
        global Game_Window
        home = 'home'
        if type(self.Movers_pos_1) == str and self.Movers_pos_1 == home:
            x, y, x1, y1 = self.Home_pos_1
            Game_Window.blit(self.Movers_ballast, [x, y])
        elif type(self.Movers_pos_1) == int:
            x, y, x1, y1 = self.Path[self.Movers_pos_1 - 1]
            Game_Window.blit(self.Movers_ballast, [x, y])

        if type(self.Movers_pos_2) == str and self.Movers_pos_2 == home:
            x, y, x1, y1 = self.Home_pos_2
            Game_Window.blit(self.Movers_ballast, [x, y])
        elif type(self.Movers_pos_2) == int:
            x, y, x1, y1 = self.Path[self.Movers_pos_2 - 1]
            Game_Window.blit(self.Movers_ballast, [x, y])

        if type(self.Movers_pos_3) == str and self.Movers_pos_3 == home:
            x, y, x1, y1 = self.Home_pos_3
            Game_Window.blit(self.Movers_ballast, [x, y])
        elif type(self.Movers_pos_3) == int:
            x, y, x1, y1 = self.Path[self.Movers_pos_3 - 1]
            Game_Window.blit(self.Movers_ballast, [x, y])

        if type(self.Movers_pos_4) == str and self.Movers_pos_4 == home:
            x, y, x1, y1 = self.Home_pos_4
            Game_Window.blit(self.Movers_ballast, [x, y])
        elif type(self.Movers_pos_4) == int:
            x, y, x1, y1 = self.Path[self.Movers_pos_4 - 1]
            Game_Window.blit(self.Movers_ballast, [x, y])

    @staticmethod
    def collide(mouse_x, mouse_y, rect):
        x, y, x1, y1 = rect
        if (mouse_x > x) and (mouse_x < x1) and (mouse_y > y) and (mouse_y < y1):
            return True
        else:
            return False

    def bet_manage(self, events):
        global Last_bet_number
        global Game_Window
        x, y, x1, y1 = self.Bet_block
        if events.type == pygame.MOUSEBUTTONDOWN:
            if events.button == 1:
                mouse_x, mouse_y = events.pos
                if self.collide(mouse_x, mouse_y, self.Bet_block) and self.Bet_status:
                    self.Bet_status = False
                    self.Bet_flag = True
                    self.Bet_itration = self.bet_now()

        if self.Bet_flag:
            try:
                next(self.Bet_itration)
            except StopIteration:
                self.Bet_flag = False
                Last_bet_number = random.randint(1, 6)
        else:
            Game_Window.blit(Ballast_number_img[Last_bet_number-1], [x+14, y+15])  # 14, 15

    def bet_now(self):
        global Game_Window
        x, y, x1, y1 = self.Bet_block
        center_point_x = int(x + ((x1 - x) / 2))
        center_point_y = int(y + ((y1 - y) / 2))
        value = 7
        count = 0
        while count <= value:
            image = Ballast_img[count]
            point_x = center_point_x - (image.get_width() / 2)
            point_y = center_point_y - (image.get_height() / 2)
            Game_Window.blit(image, [point_x, point_y])
            pygame.time.Clock().tick(30)
            count += 1
            random.randint(1, 6)
            yield count
        return

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
Ballast_img = [pygame.image.load('Media/Image/ballast/B1.png'), pygame.image.load('Media/Image/ballast/B2.png'),
               pygame.image.load('Media/Image/ballast/B3.png'), pygame.image.load('Media/Image/ballast/B4.png'),
               pygame.image.load('Media/Image/ballast/B5.png'), pygame.image.load('Media/Image/ballast/B6.png'),
               pygame.image.load('Media/Image/ballast/B7.png'), pygame.image.load('Media/Image/ballast/B8.png')]

Ballast_number_img = [pygame.image.load('Media/Image/ballast/BN1.png'),
                      pygame.image.load('Media/Image/ballast/BN2.png'),
                      pygame.image.load('Media/Image/ballast/BN3.png'),
                      pygame.image.load('Media/Image/ballast/BN4.png'),
                      pygame.image.load('Media/Image/ballast/BN5.png'),
                      pygame.image.load('Media/Image/ballast/BN6.png')]

# Global variables.
Mouse_x = 0
Mouse_y = 0
event = None
colors_rb = Colors()
Last_bet_number = 2


def close_game():
    pygame.quit()
    sys.exit()


# Main menu Creation.

b1 = Ballast('green')

while True:
    for event in pygame.event.get():
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            close_game()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.button)
            print("Mouse X : ", Mouse_x)
            print("Mouse Y : ", Mouse_y)

    Game_Window.blit(Game_background, [0, 0])
    b1.bet_manage(event)
    b1.print_movers_ballast()
    pygame.display.update()
