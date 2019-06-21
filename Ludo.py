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
    light_green = (97, 227, 31)
    light_blue = (0, 133, 255)


# class for defining path and position of ballast.
class Ballast:
    def __init__(self, color_type):
        if color_type == 'green':
            self.Home_border = [530, 416, 801, 686]
            self.color = [2, 160, 73]
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
            self.color = [255, 222, 21]
            self.Home_border = [119, 415, 390, 687]
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
            self.color = [235, 28, 34]
            self.Home_border = [118, 5, 390, 275]
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
            self.color = [33, 159, 235]
            self.Home_border = [531, 4, 801, 275]
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

        self.Home_border_width = 25
        self.Movers_pos_1 = 'home'
        self.Movers_pos_2 = 'home'
        self.Movers_pos_3 = 'home'
        self.Movers_pos_4 = 'home'
        self.color_type = color_type
        self.bet_status = True
        self.bet_flag = False
        self.bet_itration = None
        self.last_bet_number = None
        self.ballast_highlight_color = [0, 247, 238]
        self.home_highlighter_color = [0, 229, 255]
        self.home_highlighter_counter = 1
        self.stop_positions = ([714, 369, 759, 412], [483, 553, 526, 598], [393, 599, 437, 645], [208, 368, 254, 413],
                               [161, 279, 207, 322], [394, 94, 437, 139], [484, 46, 527, 92], [667, 279, 712, 324])

    def validate_moves(self, moves, mover_ballast):
        if mover_ballast == 1:
            if len(self.Path)-1 < self.Movers_pos_1 + moves:
                return True
            else:
                return False
        elif mover_ballast == 2:
            if len(self.Path)-1 < self.Movers_pos_2 + moves:
                return True
            else:
                return False
        elif mover_ballast == 3:
            if len(self.Path)-1 < self.Movers_pos_3 + moves:
                return True
            else:
                return False
        elif mover_ballast == 4:
            if len(self.Path)-1 < self.Movers_pos_4 + moves:
                return True
            else:
                return False

    @staticmethod
    def get_med_position(rect):
        x, y, x1, y1 = rect
        width = x1 - x
        height = y1 - y
        return [int(x+(width/2)), int(y+(height/2))]

    def home_highlight_rect(self):
        global Game_Window
        x, y, x1, y1 = self.Home_border
        pygame.draw.rect(Game_background, tuple(self.color), [x, y, x1-x, y1-y], self.Home_border_width)

    def ballast_highlight(self):
        global Game_Window
        color = tuple(self.ballast_highlight_color)
        if self.Movers_pos_1 != 'home':
            x, y, x1, y1 = self.Path[self.Movers_pos_1]
            pygame.draw.rect(Game_Window, color, [x, y, x1-x, y1-y])
        if self.Movers_pos_2 != 'home':
            x, y, x1, y1 = self.Path[self.Movers_pos_2]
            pygame.draw.rect(Game_Window, color, [x, y, x1 - x, y1 - y])
        if self.Movers_pos_3 != 'home':
            x, y, x1, y1 = self.Path[self.Movers_pos_3]
            pygame.draw.rect(Game_Window, color, [x, y, x1 - x, y1 - y])
        if self.Movers_pos_4 != 'home':
            x, y, x1, y1 = self.Path[self.Movers_pos_4]
            pygame.draw.rect(Game_Window, color, [x, y, x1 - x, y1 - y])

    def get_position(self):
        pos_list = []
        home = 'home'
        if self.Movers_pos_1 != home:
            pos_list.append(self.Path[self.Movers_pos_1])
        else:
            pos_list.append(0)
        if self.Movers_pos_2 != home:
            pos_list.append(self.Path[self.Movers_pos_2])
        else:
            pos_list.append(0)
        if self.Movers_pos_3 != home:
            pos_list.append(self.Path[self.Movers_pos_3])
        else:
            pos_list.append(0)
        if self.Movers_pos_4 != home:
            pos_list.append(self.Path[self.Movers_pos_4])
        else:
            pos_list.append(0)
        return pos_list

    def put_ballast(self, rect, players=None):
        global Game_Window
        x, y, x1, y1 = rect
        if y == 0:
            c_x = (x + ((x1 - x) / 2)) - 18
            c_y = y - 1
            Game_Window.blit(self.Movers_ballast, [c_x, c_y])
        else:
            c_y = (y+((y1-y)/2))-40
            c_x = (x+((x1-x)/2))-18
            Game_Window.blit(self.Movers_ballast, [c_x, c_y])


    def print_movers_ballast(self):
        global Game_Window
        home = 'home'
        if type(self.Movers_pos_1) == str and self.Movers_pos_1 == home:
            self.put_ballast(self.Home_pos_1)
        elif type(self.Movers_pos_1) == int:
            self.put_ballast(self.Path[self.Movers_pos_1])

        if type(self.Movers_pos_2) == str and self.Movers_pos_2 == home:
            self.put_ballast(self.Home_pos_2)
        elif type(self.Movers_pos_2) == int:
            self.put_ballast(self.Path[self.Movers_pos_2])

        if type(self.Movers_pos_3) == str and self.Movers_pos_3 == home:
            self.put_ballast(self.Home_pos_3)
        elif type(self.Movers_pos_3) == int:
            self.put_ballast(self.Path[self.Movers_pos_3])

        if type(self.Movers_pos_4) == str and self.Movers_pos_4 == home:
            self.put_ballast(self.Home_pos_4)
        elif type(self.Movers_pos_4) == int:
            self.put_ballast(self.Path[self.Movers_pos_4])

    @staticmethod
    def collide(mouse_x, mouse_y, rect):
        x, y, x1, y1 = rect
        if (mouse_x > x) and (mouse_x < x1) and (mouse_y > y) and (mouse_y < y1):
            return True
        else:
            return False

    def move_ballast(self, events, moves):
        home = 'home'
        if self.Movers_pos_4 == home and self.Movers_pos_3 == home and self.Movers_pos_2 == home\
                and self.Movers_pos_1 == home and moves != 6:
            return True
        if events.type == pygame.MOUSEBUTTONDOWN:
            if events.button == 1:
                mouse_x, mouse_y = event.pos
                if self.Movers_pos_1 != home and self.collide(mouse_x, mouse_y, self.Path[self.Movers_pos_1]):
                    self.Movers_pos_1 += moves
                    return True
                elif self.Movers_pos_2 != home and self.collide(mouse_x, mouse_y, self.Path[self.Movers_pos_2]):
                    self.Movers_pos_2 += moves
                    return True
                elif self.Movers_pos_3 != home and self.collide(mouse_x, mouse_y, self.Path[self.Movers_pos_3]):
                    self.Movers_pos_3 += moves
                    return True
                elif self.Movers_pos_4 != home and self.collide(mouse_x, mouse_y, self.Path[self.Movers_pos_4]):
                    self.Movers_pos_4 += moves
                    return True
                elif moves == 6:
                    if self.collide(mouse_x, mouse_y, self.Home_pos_1) and self.Movers_pos_1 == home:
                        self.Movers_pos_1 = 0
                        return True
                    elif self.collide(mouse_x, mouse_y, self.Home_pos_2) and self.Movers_pos_2 == home:
                        self.Movers_pos_2 = 0
                        return True
                    elif self.collide(mouse_x, mouse_y, self.Home_pos_3) and self.Movers_pos_3 == home:
                        self.Movers_pos_3 = 0
                        return True
                    elif self.collide(mouse_x, mouse_y, self.Home_pos_4) and self.Movers_pos_4 == home:
                        self.Movers_pos_4 = 0
                        return True
        return False

    def bet_manage(self, events):
        global Last_bet_number
        global Game_Window
        global Last_six_counter
        x, y, x1, y1 = self.Bet_block
        if events.type == pygame.MOUSEBUTTONDOWN:
            if events.button == 1:
                mouse_x, mouse_y = events.pos
                if self.collide(mouse_x, mouse_y, self.Bet_block) and self.bet_status:
                    self.bet_status = False
                    self.bet_flag = True
                    self.bet_itration = self.bet_now()

        if self.bet_flag:
            try:
                next(self.bet_itration)
            except StopIteration:
                self.bet_flag = False
                Last_bet_number = random.randint(1, 6)
                if Last_bet_number == 6:
                    Last_six_counter += 1
                    if Last_six_counter > 2:
                        while Last_bet_number != 6:
                            Last_bet_number = random.randint(1, 6)
                        Last_six_counter = 0
                else:
                    Last_six_counter = 0
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
            pygame.time.Clock().tick(70)
            count += 1
            random.randint(1, 6)
            yield count
        return

# Defining class for buttons.


class Button:
    def __init__(self, surface, image, hover_img, x, y):
        self.surface = surface
        self.image = pygame.image.load(image)
        self.hover_img = pygame.image.load(hover_img)
        self.x = x
        self.y = y
        self.x1 = x+self.image.get_width()
        self.y1 = y+self.image.get_height()

    def put(self):
        self.surface.blit(self.image, [self.x, self.y])

    def collide(self, x, y):
        if (x > self.x) and (x < self.x1) and (y > self.y) and (y < self.y1):
            return True
        else:
            return False

    def config(self, config_dict):
        if type(config_dict) != dict:
            return
        if 'position' in config_dict:
            pos = config_dict['position']
            if type(pos) == list and len(pos) == 2:
                self.x, self.y = pos
            else:
                return

    def place(self):
        global Mouse_x
        global Mouse_y
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        if self.collide(Mouse_x, Mouse_y):
            self.surface.blit(self.hover_img, [self.x, self.y])
        else:
            self.surface.blit(self.image, [self.x, self.y])


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

main_menu_img = pygame.image.load('Media/Image/menu_img/Menu.png')
visit_on_website = Button(Game_Window, 'Media/Image/menu_img/Visit_button_black.png',
                          'Media/Image/menu_img/Visit_button_green.png', 120, 595)

# Global variables.
Mouse_x = 0
Mouse_y = 0
event = None
colors_rb = Colors()
Last_bet_number = 2
Last_six_counter = 0

# temp function to define positions


def selecter(x, y, mouse_x, mouse_y, color=colors_rb.light_black):
    pygame.draw.rect(Game_Window, color, [x, y, mouse_x-x, mouse_y-y], 1)


def drow_circule(x, y, redouis, color=colors_rb.light_black):
    pygame.draw.circle(Game_Window, color, [x, y], redouis)


def verify_position():
    global colors_rb
    global event
    fp = open('position.txt', 'r')
    data = ''
    x, y, x1, y1 = [0, 0, 0, 0]
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


def collide(mouse_x, mouse_y, rect):
    x, y, x1, y1 = rect
    if (mouse_x > x) and (mouse_x < x1) and (mouse_y > y) and (mouse_y < y1):
        return True
    else:
        return False


def close_game():
    pygame.quit()
    sys.exit()


def play_game(players=0):
    global Mouse_x, Mouse_y
    global event
    global Last_six_counter
    global Last_bet_number
    player = [Ballast('green'), Ballast('yellow'), Ballast('red'), Ballast('blue')]

    total_player = len(player)+players
    bet_turn = 0
    move_ballast = False
    temp_last_bet_number = 0
    move_ballast_1 = False
    move_ballast_2 = False
    move_ballast_3 = False
    move_ballast_4 = False
    reverse_move = False
    reverse_move_ballast = None
    home = 'home'
    ballast_highlighter_color_change = 1
    cut_flag = False
    while True:
        for event in pygame.event.get():
            Mouse_x, Mouse_y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                close_game()
        Game_Window.fill((255, 255, 255))
        x, y, x1, y1 = player[bet_turn].Home_border
        pygame.draw.rect(Game_Window, player[bet_turn].home_highlighter_color, [x, y, x1-x, y1-y])
        if player[bet_turn].home_highlighter_counter <= 200:
            player[bet_turn].home_highlighter_color[0] += 20
            player[bet_turn].home_highlighter_counter += 20
        elif player[bet_turn].home_highlighter_counter <= 400:
            player[bet_turn].home_highlighter_color[0] -= 20
            player[bet_turn].home_highlighter_counter += 20
        elif player[bet_turn].home_highlighter_counter > 400:
            player[bet_turn].home_highlighter_counter = 1
            player[bet_turn].home_highlighter_color = [0, 229, 255]

        Game_Window.blit(Game_background, [0, 0])
        if bet_turn == 0:
            if total_player >= 1:
                player[0].bet_manage(event)
                if not player[0].bet_status and not player[0].bet_flag and not move_ballast:
                    temp_last_bet_number = Last_bet_number
                    move_ballast = True
        if bet_turn == 1:
            if total_player >= 2:
                player[1].bet_manage(event)
                if not player[1].bet_status and not player[1].bet_flag and not move_ballast:
                    temp_last_bet_number = Last_bet_number
                    move_ballast = True
        if bet_turn == 2:
            if total_player >= 3:
                player[2].bet_manage(event)
                if not player[2].bet_status and not player[2].bet_flag and not move_ballast:
                    temp_last_bet_number = Last_bet_number
                    move_ballast = True

        if bet_turn == 3:
            if total_player >= 4:
                player[3].bet_manage(event)
                if not player[3].bet_status and not player[3].bet_flag and not move_ballast:
                    temp_last_bet_number = Last_bet_number
                    move_ballast = True

        if move_ballast:
            if not reverse_move and not move_ballast_1 and not move_ballast_2 and not move_ballast_3 and not move_ballast_4:
                if player[bet_turn].Movers_pos_4 == home and player[bet_turn].Movers_pos_3 == home \
                        and player[bet_turn].Movers_pos_2 == home and player[bet_turn].Movers_pos_1 == home and Last_bet_number != 6:
                    move_ballast = False
                    if Last_bet_number != 6:
                        player[bet_turn].bet_status = True
                        bet_turn += 1
                        if bet_turn > total_player - 1:
                            bet_turn = 0
                        Last_six_counter = 0
                    else:
                        player[bet_turn].bet_status = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_x, mouse_y = event.pos
                        if player[bet_turn].Movers_pos_1 != home and player[bet_turn].collide(mouse_x, mouse_y, player[bet_turn].Path[player[bet_turn].Movers_pos_1]):
                            move_ballast_1 = True
                        elif player[bet_turn].Movers_pos_2 != home and player[bet_turn].collide(mouse_x, mouse_y, player[bet_turn].Path[player[bet_turn].Movers_pos_2]):
                            move_ballast_2 = True
                        elif player[bet_turn].Movers_pos_3 != home and player[bet_turn].collide(mouse_x, mouse_y, player[bet_turn].Path[player[bet_turn].Movers_pos_3]):
                            move_ballast_3 = True
                        elif player[bet_turn].Movers_pos_4 != home and player[bet_turn].collide(mouse_x, mouse_y, player[bet_turn].Path[player[bet_turn].Movers_pos_4]):
                            move_ballast_4 = True
                        elif Last_bet_number == 6:
                            if player[bet_turn].collide(mouse_x, mouse_y, player[bet_turn].Home_pos_1) \
                                    and player[bet_turn].Movers_pos_1 == home:
                                player[bet_turn].Movers_pos_1 = 0
                                move_ballast_1 = False
                                move_ballast_2 = False
                                move_ballast_3 = False
                                move_ballast_4 = False
                                move_ballast = False
                                if Last_bet_number != 6:
                                    player[bet_turn].bet_status = True
                                    bet_turn += 1
                                    if bet_turn > total_player - 1:
                                        bet_turn = 0
                                    Last_six_counter = 0
                                else:
                                    player[bet_turn].bet_status = True
                            elif player[bet_turn].collide(mouse_x, mouse_y, player[bet_turn].Home_pos_2) \
                                    and player[bet_turn].Movers_pos_2 == home:
                                player[bet_turn].Movers_pos_2 = 0
                                move_ballast_1 = False
                                move_ballast_2 = False
                                move_ballast_3 = False
                                move_ballast_4 = False
                                move_ballast = False
                                if Last_bet_number != 6:
                                    player[bet_turn].bet_status = True
                                    bet_turn += 1
                                    if bet_turn > total_player - 1:
                                        bet_turn = 0
                                    Last_six_counter = 0
                                else:
                                    player[bet_turn].bet_status = True
                            elif player[bet_turn].collide(mouse_x, mouse_y, player[bet_turn].Home_pos_3) \
                                    and player[bet_turn].Movers_pos_3 == home:
                                player[bet_turn].Movers_pos_3 = 0
                                move_ballast_1 = False
                                move_ballast_2 = False
                                move_ballast_3 = False
                                move_ballast_4 = False
                                move_ballast = False
                                if Last_bet_number != 6:
                                    player[bet_turn].bet_status = True
                                    bet_turn += 1
                                    if bet_turn > total_player - 1:
                                        bet_turn = 0
                                    Last_six_counter = 0
                                else:
                                    player[bet_turn].bet_status = True
                            elif player[bet_turn].collide(mouse_x, mouse_y, player[bet_turn].Home_pos_4) \
                                    and player[bet_turn].Movers_pos_4 == home:
                                player[bet_turn].Movers_pos_4 = 0
                                move_ballast_1 = False
                                move_ballast_2 = False
                                move_ballast_3 = False
                                move_ballast_4 = False
                                move_ballast = False
                                if Last_bet_number != 6:
                                    player[bet_turn].bet_status = True
                                    bet_turn += 1
                                    if bet_turn > total_player - 1:
                                        bet_turn = 0
                                    Last_six_counter = 0
                                else:
                                    player[bet_turn].bet_status = True
            else:
                if reverse_move_ballast == None and not reverse_move and not cut_flag:
                    if move_ballast_1:
                        temp_last_bet_number -= 1
                        pygame.time.Clock().tick(10)
                        player[bet_turn].Movers_pos_1 += 1
                    elif move_ballast_2:
                        temp_last_bet_number -= 1
                        player[bet_turn].Movers_pos_2 += 1
                        pygame.time.Clock().tick(10)
                    elif move_ballast_3:
                        temp_last_bet_number -= 1
                        player[bet_turn].Movers_pos_3 += 1
                        pygame.time.Clock().tick(10)
                    elif move_ballast_4:
                        temp_last_bet_number -= 1
                        player[bet_turn].Movers_pos_4 += 1
                        pygame.time.Clock().tick(10)

                    if temp_last_bet_number == 0:
                        if move_ballast_1:
                            for element in player[bet_turn].stop_positions:
                                if element == player[bet_turn].Path[player[bet_turn].Movers_pos_1]:
                                    break
                            else:
                                cut_flag = True
                        elif move_ballast_2:
                            for element in player[bet_turn].stop_positions:
                                if element == player[bet_turn].Path[player[bet_turn].Movers_pos_2]:
                                    break
                            else:
                                cut_flag = True
                        elif move_ballast_3:
                            for element in player[bet_turn].stop_positions:
                                if element == player[bet_turn].Path[player[bet_turn].Movers_pos_3]:
                                    break
                            else:
                                cut_flag = True
                        elif move_ballast_4:
                            for element in player[bet_turn].stop_positions:
                                if element == player[bet_turn].Path[player[bet_turn].Movers_pos_4]:
                                    break
                            else:
                                cut_flag = True
                        if cut_flag:
                            count = 0
                            for element in player:
                                if count != bet_turn:
                                    b1, b2, b3, b4 = element.get_position()
                                    if move_ballast_1:
                                        if b1 == player[bet_turn].Path[player[bet_turn].Movers_pos_1]:
                                            move_ballast_1 = False
                                            reverse_move_ballast = element
                                            reverse_move = True
                                            move_ballast_1 = True
                                            #element.Movers_pos_1 = 'home'
                                            break
                                        elif b2 == player[bet_turn].Path[player[bet_turn].Movers_pos_1]:
                                            move_ballast_1 = False
                                            reverse_move_ballast = element
                                            reverse_move = True
                                            move_ballast_2 = True
                                            #element.Movers_pos_2 = 'home'
                                            break
                                        elif b3 == player[bet_turn].Path[player[bet_turn].Movers_pos_1]:
                                            move_ballast_1 = False
                                            reverse_move_ballast = element
                                            reverse_move = True
                                            move_ballast_3 = True
                                            #element.Movers_pos_3 = 'home'
                                            break
                                        elif b4 == player[bet_turn].Path[player[bet_turn].Movers_pos_1]:
                                            move_ballast_1 = False
                                            reverse_move_ballast = element
                                            reverse_move = True
                                            move_ballast_4 = True
                                            #element.Movers_pos_4 = 'home'
                                            break
                                    elif move_ballast_2:
                                        if b1 == player[bet_turn].Path[player[bet_turn].Movers_pos_2]:
                                            move_ballast_2 = False
                                            reverse_move_ballast = element
                                            reverse_move = True
                                            move_ballast_1 = True
                                            #element.Movers_pos_1 = 'home'
                                            break
                                        elif b2 == player[bet_turn].Path[player[bet_turn].Movers_pos_2]:
                                            move_ballast_2 = False
                                            reverse_move_ballast = element
                                            reverse_move = True
                                            move_ballast_2 = True
                                            #element.Movers_pos_2 = 'home'
                                            break
                                        elif b3 == player[bet_turn].Path[player[bet_turn].Movers_pos_2]:
                                            move_ballast_2 = False
                                            reverse_move_ballast = element
                                            reverse_move = True
                                            move_ballast_3 = True
                                            #element.Movers_pos_3 = 'home'
                                            break
                                        elif b4 == player[bet_turn].Path[player[bet_turn].Movers_pos_2]:
                                            move_ballast_2 = False
                                            reverse_move_ballast = element
                                            reverse_move = True
                                            move_ballast_4 = True
                                            #element.Movers_pos_4 = 'home'
                                            break
                                    elif move_ballast_3:
                                        if b1 == player[bet_turn].Path[player[bet_turn].Movers_pos_3]:
                                            move_ballast_3 = False
                                            reverse_move_ballast = element
                                            reverse_move = True
                                            move_ballast_1 = True
                                            #element.Movers_pos_1 = 'home'
                                            break
                                        elif b2 == player[bet_turn].Path[player[bet_turn].Movers_pos_3]:
                                            move_ballast_3 = False
                                            reverse_move_ballast = element
                                            reverse_move = True
                                            move_ballast_2 = True
                                            #element.Movers_pos_2 = 'home'
                                            break
                                        elif b3 == player[bet_turn].Path[player[bet_turn].Movers_pos_3]:
                                            move_ballast_3 = False
                                            reverse_move_ballast = element
                                            reverse_move = True
                                            move_ballast_3 = True
                                            #element.Movers_pos_3 = 'home'
                                            break
                                        elif b4 == player[bet_turn].Path[player[bet_turn].Movers_pos_3]:
                                            move_ballast_3 = False
                                            reverse_move_ballast = element
                                            reverse_move = True
                                            move_ballast_4 = True
                                            #element.Movers_pos_4 = 'home'
                                            break
                                    elif move_ballast_4:
                                        if b1 == player[bet_turn].Path[player[bet_turn].Movers_pos_4]:
                                            move_ballast_4 = False
                                            reverse_move_ballast = element
                                            reverse_move = True
                                            move_ballast_1 = True
                                            #element.Movers_pos_1 = 'home'
                                            break
                                        elif b2 == player[bet_turn].Path[player[bet_turn].Movers_pos_4]:
                                            move_ballast_4 = False
                                            reverse_move_ballast = element
                                            reverse_move = True
                                            move_ballast_2 = True
                                            #element.Movers_pos_2 = 'home'
                                            break
                                        elif b3 == player[bet_turn].Path[player[bet_turn].Movers_pos_4]:
                                            move_ballast_4 = False
                                            reverse_move_ballast = element
                                            reverse_move = True
                                            move_ballast_3 = True
                                            #element.Movers_pos_3 = 'home'
                                            break
                                        elif b4 == player[bet_turn].Path[player[bet_turn].Movers_pos_4]:
                                            move_ballast_4 = False
                                            reverse_move_ballast = element
                                            reverse_move = True
                                            move_ballast_4 = True
                                            #element.Movers_pos_4 = 'home'
                                            break
                                count += 1
                            else:
                                reverse_move_ballast = None
                                reverse_move = False
                                cut_flag = False
                                move_ballast = False
                                move_ballast_1 = False
                                move_ballast_2 = False
                                move_ballast_3 = False
                                move_ballast_4 = False
                                if Last_bet_number != 6:
                                    player[bet_turn].bet_status = True
                                    bet_turn += 1
                                    if bet_turn > total_player - 1:
                                        bet_turn = 0
                                    Last_six_counter = 0
                                else:
                                    player[bet_turn].bet_status = True
                        else:
                            reverse_move_ballast = None
                            reverse_move = False
                            cut_flag = False
                            move_ballast = False
                            move_ballast_1 = False
                            move_ballast_2 = False
                            move_ballast_3 = False
                            move_ballast_4 = False
                            if Last_bet_number != 6:
                                player[bet_turn].bet_status = True
                                bet_turn += 1
                                if bet_turn > total_player - 1:
                                    bet_turn = 0
                                Last_six_counter = 0
                            else:
                                player[bet_turn].bet_status = True
                else:
                    if cut_flag:
                        if move_ballast_1:
                            if reverse_move_ballast.Movers_pos_1 != 0:
                                reverse_move_ballast.Movers_pos_1 -= 1
                            else:
                                reverse_move_ballast.Movers_pos_1 = 'home'
                                cut_flag = False
                        elif move_ballast_2:
                            if reverse_move_ballast.Movers_pos_2 != 0:
                                reverse_move_ballast.Movers_pos_2 -= 1
                            else:
                                reverse_move_ballast.Movers_pos_2 = 'home'
                                cut_flag = False
                        elif move_ballast_3:
                            if reverse_move_ballast.Movers_pos_3 != 0:
                                reverse_move_ballast.Movers_pos_3 -= 1
                            else:
                                reverse_move_ballast.Movers_pos_3 = 'home'
                                cut_flag = False
                        elif move_ballast_4:
                            if reverse_move_ballast.Movers_pos_4 != 0:
                                reverse_move_ballast.Movers_pos_4 -= 1
                            else:
                                reverse_move_ballast.Movers_pos_4 = 'home'
                                cut_flag = False
                        pygame.time.Clock().tick(30)
                    else:
                        reverse_move_ballast = None
                        reverse_move = False
                        cut_flag = False
                        move_ballast = False
                        move_ballast_1 = False
                        move_ballast_2 = False
                        move_ballast_3 = False
                        move_ballast_4 = False
                        player[bet_turn].bet_status = True



        if move_ballast and not move_ballast_1 and not move_ballast_2 and not move_ballast_3 and not move_ballast_4:
            player[bet_turn].ballast_highlight()
            if ballast_highlighter_color_change <= 240:
                player[bet_turn].ballast_highlight_color[0] += 10
                #player[bet_turn].ballast_highlight_color[1] += 5
                #player[bet_turn].ballast_highlight_color[2] +=
                ballast_highlighter_color_change += 10
            elif ballast_highlighter_color_change <= 480:
                player[bet_turn].ballast_highlight_color[0] -= 10
                #player[bet_turn].ballast_highlight_color[1] -= 5
                #player[bet_turn].ballast_highlight_color[2] -= 5
                ballast_highlighter_color_change += 10
            elif ballast_highlighter_color_change > 480:
                ballast_highlighter_color_change = 1
                player[bet_turn].ballast_highlight_color = [0, 247, 238]
        else:
            ballast_highlighter_color_change = 1
            player[bet_turn].ballast_highlight_color = [0, 247, 238]

        if total_player >= 1:
            player[0].print_movers_ballast()
        if total_player >= 2:
            player[1].print_movers_ballast()
        if total_player >= 3:
            player[2].print_movers_ballast()
        if total_player >= 4:
            player[3].print_movers_ballast()
        player[bet_turn].print_movers_ballast()
        if cut_flag and reverse_move_ballast != None:
            reverse_move_ballast.print_movers_ballast()
        pygame.display.update()


def main_menu():
    global Game_Window
    global Mouse_x, Mouse_y
    global event
    global main_menu_img
    global visit_on_website
    options_rect_positions = ([448, 135, 844, 233], [448, 272, 844, 370], [448, 409, 844, 507], [448, 545, 844, 643])
    option_rect = 0
    option_rect_color_flag = False
    while True:
        for event in pygame.event.get():
            Mouse_x, Mouse_y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                close_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if option_rect == 3:
                        option_rect = 0
                    else:
                        option_rect += 1
                if event.key == pygame.K_UP:
                    if option_rect == 0:
                        option_rect = 3
                    else:
                        option_rect -= 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if collide(Mouse_x, Mouse_y, options_rect_positions[0]):
                    option_rect_color_flag = True
                if collide(Mouse_x, Mouse_y, options_rect_positions[1]):
                    option_rect_color_flag = True
                if collide(Mouse_x, Mouse_y, options_rect_positions[2]):
                    option_rect_color_flag = True
                if collide(Mouse_x, Mouse_y, options_rect_positions[3]):
                    option_rect_color_flag = True
            if event.type == pygame.MOUSEBUTTONUP:
                option_rect_color_flag = False
                if collide(Mouse_x, Mouse_y, options_rect_positions[0]):
                    play_game()
                if collide(Mouse_x, Mouse_y, options_rect_positions[1]):
                    pass
                if collide(Mouse_x, Mouse_y, options_rect_positions[2]):
                    pass
                if collide(Mouse_x, Mouse_y, options_rect_positions[3]):
                    pass

        if collide(Mouse_x, Mouse_y, options_rect_positions[0]):
            option_rect = 0
        if collide(Mouse_x, Mouse_y, options_rect_positions[1]):
            option_rect = 1
        if collide(Mouse_x, Mouse_y, options_rect_positions[2]):
            option_rect = 2
        if collide(Mouse_x, Mouse_y, options_rect_positions[3]):
            option_rect = 3
        Game_Window.blit(main_menu_img, [0, 0])
        visit_on_website.place()
        x, y, x1, y1 = options_rect_positions[option_rect]
        if option_rect_color_flag:
            pygame.draw.rect(Game_Window, colors_rb.light_blue, [x, y, x1 - x, y1 - y], 4)
        else:
            pygame.draw.rect(Game_Window, colors_rb.light_green, [x, y, x1-x, y1-y], 4)
        pygame.display.update()


def ballast_resizer(self, resize_value, ballast):
    width = ballast.get_width()
    height = ballast.get_height()


def test_for_resizer():
    ballast_image = pygame.image.load('Media/Image/Movers_ballast/Blue.png')
    temp_image = ballast_image
    width = temp_image.get_width()
    height = temp_image.get_height()
    global event
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    height += 1
                    width += 1
                if event.key == pygame.K_DOWN:
                    height -= 1
                    width -= 1
                if event.key == pygame.K_LEFT:
                    width -= 1
                    height -= 1
                if event.key == pygame.K_RIGHT:
                    width += 1
                    height += 1
                temp_image = pygame.transform.scale(ballast_image, (width, height)).convert_alpha()

        Game_Window.blit(Game_background, [0, 0])
        Game_Window.blit(temp_image, [604, 44])
        pygame.display.update()


play_game()
