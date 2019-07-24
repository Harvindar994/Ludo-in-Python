import pygame
import sys
import random
import clipboard
import pymongo
from PIL import Image
pygame.init()


# Global color Class.
class Colors:
    white = (255, 255, 255)
    orange = (252, 82, 59)
    light_black = (43, 43, 43)
    light_gray = (166, 166, 166)
    light_green = (97, 227, 31)
    light_blue = (0, 133, 255)
    light_orange = (255, 61, 0)


# class for defining path and position of ballast.
class Ballast:
    def __init__(self, color_type):
        if color_type == 'green':
            self.Winner_name_pos = [559, 780, 668]
            self.Home_border = [531, 415, 801, 687]
            self.color = [2, 160, 73]
            self.Bet_block = [815, 491, 910, 588]
            self.win_box = [523, 315, 491, 377]
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
            self.Winner_name_pos = [142, 362, 668]
            self.color = [255, 222, 21]
            self.Home_border = [119, 415, 390, 687]
            self.Bet_block = [10, 492, 106, 588]
            self.win_box = [429, 376, 491, 409]
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
            self.Winner_name_pos = [142, 362, 8]
            self.color = [235, 28, 34]
            self.Home_border = [118, 5, 390, 275]
            self.Bet_block = [9, 61, 105, 158]
            self.win_box = [396, 319, 432, 375]
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
            self.Winner_name_pos = [559, 780, 8]
            self.color = [33, 159, 235]
            self.Home_border = [531, 4, 801, 275]
            self.Bet_block = [814, 62, 912, 158]
            self.win_box = [429, 282, 491, 314]
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

        self.Win_status = False
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

    def is_stop_location(self, moves):
        if len(self.Path)-1 >= moves:
            for e in self.stop_positions:
                if e == self.Path[moves]:
                    return True
                    return True
            else:
                return False
        else:
            return False

    def validate_moves(self, moves, mover_ballast):
        home = 'home'
        win = 'win'
        if mover_ballast == 1:
            if moves == 6 and self.Movers_pos_1 == home:
                return True
            elif self.Movers_pos_1 != home and self.Movers_pos_1 != win and len(self.Path) >= self.Movers_pos_1 + moves:
                if not self.is_stop_location(self.Movers_pos_1 + moves):
                    if not((self.Movers_pos_1 + moves == self.Movers_pos_2)
                           or (self.Movers_pos_1 + moves == self.Movers_pos_3)
                           or (self.Movers_pos_1 + moves == self.Movers_pos_4)):
                        return True
                    else:
                        return False
                else:
                    return True
            return False
        elif mover_ballast == 2:
            if moves == 6 and self.Movers_pos_2 == home:
                return True
            elif self.Movers_pos_2 != home and self.Movers_pos_2 != win and len(self.Path) >= self.Movers_pos_2 + moves:
                if not self.is_stop_location(self.Movers_pos_2 + moves):
                    if not((self.Movers_pos_2 + moves == self.Movers_pos_1)
                           or (self.Movers_pos_2 + moves == self.Movers_pos_3)
                           or (self.Movers_pos_2 + moves == self.Movers_pos_4)):
                        return True
                    else:
                        return False
                else:
                    return True
            return False
        elif mover_ballast == 3:
            if moves == 6 and self.Movers_pos_3 == home:
                return True
            elif self.Movers_pos_3 != home and self.Movers_pos_3 != win and len(self.Path) >= self.Movers_pos_3 + moves:
                if not self.is_stop_location(self.Movers_pos_3 + moves):
                    if not ((self.Movers_pos_3 + moves == self.Movers_pos_1)
                            or (self.Movers_pos_3 + moves == self.Movers_pos_2)
                            or (self.Movers_pos_3 + moves == self.Movers_pos_4)):
                        return True
                    else:
                        return False
                else:
                    return True
            return False
        elif mover_ballast == 4:
            if moves == 6 and self.Movers_pos_4 == home:
                return True
            elif self.Movers_pos_4 != home and self.Movers_pos_4 != win and len(self.Path) >= self.Movers_pos_4 + moves:
                if not self.is_stop_location(self.Movers_pos_4 + moves):
                    if not ((self.Movers_pos_4 + moves == self.Movers_pos_1)
                            or (self.Movers_pos_4 + moves == self.Movers_pos_3)
                            or (self.Movers_pos_4 + moves == self.Movers_pos_2)):
                        return True
                    else:
                        return False
                else:
                    return True
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
        global Last_bet_number
        color = tuple(self.ballast_highlight_color)
        if self.Movers_pos_1 != 'home' and self.validate_moves(Last_bet_number, 1):
            x, y, x1, y1 = self.Path[self.Movers_pos_1]
            pygame.draw.rect(Game_Window, color, [x, y, x1-x, y1-y])
        if self.Movers_pos_2 != 'home' and self.validate_moves(Last_bet_number, 2):
            x, y, x1, y1 = self.Path[self.Movers_pos_2]
            pygame.draw.rect(Game_Window, color, [x, y, x1 - x, y1 - y])
        if self.Movers_pos_3 != 'home' and self.validate_moves(Last_bet_number, 3):
            x, y, x1, y1 = self.Path[self.Movers_pos_3]
            pygame.draw.rect(Game_Window, color, [x, y, x1 - x, y1 - y])
        if self.Movers_pos_4 != 'home' and self.validate_moves(Last_bet_number, 4):
            x, y, x1, y1 = self.Path[self.Movers_pos_4]
            pygame.draw.rect(Game_Window, color, [x, y, x1 - x, y1 - y])

    def get_position(self):
        pos_list = []
        home = 'home'
        win = 'win'
        if self.Movers_pos_1 != home and self.Movers_pos_1 != win:
            pos_list.append(self.Path[self.Movers_pos_1])
        else:
            pos_list.append(0)
        if self.Movers_pos_2 != home and self.Movers_pos_2 != win:
            pos_list.append(self.Path[self.Movers_pos_2])
        else:
            pos_list.append(0)
        if self.Movers_pos_3 != home and self.Movers_pos_3 != win:
            pos_list.append(self.Path[self.Movers_pos_3])
        else:
            pos_list.append(0)
        if self.Movers_pos_4 != home and self.Movers_pos_4 != win:
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
        win = 'win'
        if type(self.Movers_pos_1) == str and self.Movers_pos_1 == home:
            self.put_ballast(self.Home_pos_1)
        elif type(self.Movers_pos_1) == str and self.Movers_pos_1 == win:
            self.put_ballast(self.win_box)
        elif type(self.Movers_pos_1) == int:
            self.put_ballast(self.Path[self.Movers_pos_1])

        if type(self.Movers_pos_2) == str and self.Movers_pos_2 == home:
            self.put_ballast(self.Home_pos_2)
        elif type(self.Movers_pos_2) == str and self.Movers_pos_2 == win:
            self.put_ballast(self.win_box)
        elif type(self.Movers_pos_2) == int:
            self.put_ballast(self.Path[self.Movers_pos_2])

        if type(self.Movers_pos_3) == str and self.Movers_pos_3 == home:
            self.put_ballast(self.Home_pos_3)
        elif type(self.Movers_pos_3) == str and self.Movers_pos_3 == win:
            self.put_ballast(self.win_box)
        elif type(self.Movers_pos_3) == int:
            self.put_ballast(self.Path[self.Movers_pos_3])

        if type(self.Movers_pos_4) == str and self.Movers_pos_4 == home:
            self.put_ballast(self.Home_pos_4)
        elif type(self.Movers_pos_4) == str and self.Movers_pos_4 == win:
            self.put_ballast(self.win_box)
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
                    if Last_six_counter > 1:
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
            pygame.time.Clock().tick(100)
            count += 1
            random.randint(1, 6)
            yield count
        return

# Defining class for buttons.


class Button:
    def __init__(self, surface, image, hover_img, x, y, caption_text = '', press_effact = False, button_text = None, button_text_size = 28, button_text_color = (255, 255, 255), text_file = 'Media/Font/Kollektif.ttf'):
        self.surface = surface
        self.caption = caption_text
        self.press_effact = press_effact
        if type(image) != str:
            self.image = image
        else:
            self.image = pygame.image.load(image)
        if type(hover_img) != str:
            self.hover_img = hover_img
        else:
            self.hover_img = pygame.image.load(hover_img)
        self.button_text = button_text
        self.button_text_size = button_text_size
        self.x = x
        self.y = y
        self.x1 = x+self.image.get_width()
        self.y1 = y+self.image.get_height()
        if press_effact:
            img = pygame.transform.scale(self.hover_img, ((self.hover_img.get_width()-2), (self.hover_img.get_height()-2))).convert_alpha()
            self.hover_img = img
        if button_text != None and type(button_text) == str:
            self.button_text_img = out_text_file(surface, button_text, button_text_size, 0, 0, button_text_color, text_file, True)
            self.button_text_x = (self.x+(self.image.get_width()/2))-(self.button_text_img.get_width()/2)
            self.button_text_y = (self.y+(self.image.get_height()/2))-(self.button_text_img.get_height()/2)
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
            if self.press_effact:
                self.surface.blit(self.hover_img, [self.x+1, self.y+1])
            else:
                self.surface.blit(self.hover_img, [self.x, self.y])
            if len(self.caption) != 0:
                caption(self.caption, self.x1+2, self.y-16)
        else:
            self.surface.blit(self.image, [self.x, self.y])
        if self.button_text != None and type(self.button_text) == str:
            self.surface.blit(self.button_text_img, [self.button_text_x, self.button_text_y])

class Line_effact:
    def __init__(self, surface, image = 'Media/Image/Effact/line-blue.png', starting_point = -765):
        self.surface = surface
        self.image = pygame.image.load(image)
        self.x = starting_point
        self.y = 0
        self.start_point_x = -800
        self.end_point_x = 885
        self.direction = 'right'

    def show_effact(self):
        if self.direction == 'right':
            if self.x < self.end_point_x:
                self.x += 4
            else:
                self.direction = 'left'
        if self.direction == 'left':
            if self.x > self.start_point_x:
                self.x -= 4
            else:
                self.direction = 'right'
        self.surface.blit(self.image, [self.x, self.y])

# Creating Game screen.
Game_Window = pygame.display.set_mode((920, 689), 0, 0)
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

msg_box_img = pygame.image.load('Media/Image/MsgBox/MsgBox.png')
main_menu_img = pygame.image.load('Media/Image/menu_img/Menu.png')
visit_on_website = Button(Game_Window, 'Media/Image/menu_img/Visit_button_black.png',
                          'Media/Image/menu_img/Visit_button_green.png', 120, 595)
setting_background = pygame.image.load('Media/Image/setting/background.png')
setting_background_logo = pygame.image.load('Media/Image/setting/background logo.png')
Highlighter = pygame.image.load("Media/Image/Highlighter.png")
main_background = pygame.image.load("Media/Image/main_background.png")
profile_img = pygame.image.load('Media/Image/profile/Profile.png')

# More Product Images
List_menu_background = pygame.image.load('Media/Image/List_menu/background.png')
List_menu_selector = pygame.image.load('Media/Image/List_menu/selector.png')
hover_selector = pygame.image.load('Media/Image/List_menu/hover_selector.png')

# Global variables.
Mouse_x = 0
Mouse_y = 0
event = None
colors_rb = Colors()
Last_bet_number = 2
Last_six_counter = 0
LineEffact = Line_effact(Game_Window)
LineEffact_2 = Line_effact(Game_Window, image='Media/Image/Effact/line-green.png',starting_point=875)
Database_connection = pymongo.MongoClient('localhost',27017)
Database = Database_connection['Ludo_Brightgoal']
Collection = Database['Setting']
back_button = Button(Game_Window, "Media/Image/Icon/back_blue.png", "Media/Image/Icon/back_white.png", 20, 20,
                         'Back To Menu')
facebook_button = Button(Game_Window, 'Media/Image/Icon/facebook.png', 'Media/Image/Icon/facebook.png', 339, 510, press_effact=True, caption_text='facebook.com/brightgoal.in.Education/')
brightgoal_button = Button(Game_Window, 'Media/Image/Icon/brightgoal.png', 'Media/Image/Icon/brightgoal.png', 381, 510, press_effact=True, caption_text='brightgoal.in')
youtube_button = Button(Game_Window, 'Media/Image/Icon/youtube.png', 'Media/Image/Icon/youtube.png', 423, 510, press_effact=True, caption_text='youtube.com/brightgoal')
twitter_button = Button(Game_Window, 'Media/Image/Icon/twitter.png', 'Media/Image/Icon/twitter.png', 465, 510, press_effact=True, caption_text='twitter.com/brightgoal_in')
insta_button = Button(Game_Window, 'Media/Image/Icon/insta.png', 'Media/Image/Icon/insta.png', 507, 510,
                        press_effact=True, caption_text='instagram.com/brightgoal.in')
whatsapp_button = Button(Game_Window, 'Media/Image/Icon/whatsapp.png', 'Media/Image/Icon/whatsapp.png', 549, 510,
                        press_effact=True, caption_text='9140417112')
more_product = Button(Game_Window, 'Media/Image/setting/more_product_black.png', 'Media/Image/setting/more_product_green.png', 375, 570, caption_text='https://www.instamojo.com/Brightgoal')

#Global Setting Variable

Sound_volume = 100
Music_volume = 100

# Setting related Function.

def check_Setting():
    global Database
    global Collection
    global Music_volume
    global Sound_volume

    collection_list = Database.list_collection_names()
    if 'Setting' not in collection_list:
        print('Setting not in Data Base')
        change_collection('Setting')
        try:
            Collection.insert_one({'_id':12345, 'Music volume':100, 'Sound volume':100})
        except:
            pass

    data = Collection.find_one({'_id' : 12345})
    Music_volume = data['Music volume']
    Sound_volume = data['Sound volume']

def update_setting(collection_name, s_key, s_value, update_data = {}):
    global Database
    global Collection
    global Music_volume
    global Sound_volume
    if type(collection_name) == str and len(collection_name) != 0:
        change_collection(collection_name)
    else:
        return False
    if type(update_data) ==  dict and len(update_data) != 0:
        Collection.update_many({s_key:s_value}, {'$set':update_data})

# DataBase releted function.

def change_collection(collection_name):
    global Collection
    global Database
    if type(collection_name) == str and len(collection_name)!=0:
        Collection = Database[collection_name]
        return False
    return False

def chnage_Database(database_name, collection_name):
    global Collection
    global Database_connection
    global Database
    if type(database_name) == str and type(collection_name) == str and len(database_name) != 0 \
            and len(collection_name) != 0:
        Database = Database_connection[database_name]
        Collection = Database[Collection]
        return True
    return False


# temp function to define positions


def caption(text, x, y, window_width = 920, window_height = 690, bk_color = (255, 255, 255), border_color = (43, 43, 43), text_color = colors_rb.light_black):
    global colors_rb
    difrence_between_m_y = 0
    difrence_between_m_x = 0
    text_img = out_text_file(Game_Window, text, 12, 0, 0, text_color, "Media\Font\DroidSansMono.ttf", True)
    rect_width = text_img.get_width()+6
    rect_height = text_img.get_height()+4
    rect_x = x+difrence_between_m_x
    rect_y = y+difrence_between_m_y
    if (rect_y+rect_height > window_height) and (rect_x+rect_width > window_width):
        rect_x = x-rect_width
        rect_y = y-rect_height
    if rect_x+rect_width > window_width:
        rect_x = rect_x-rect_width
    if rect_y+rect_height > window_height:
        rect_x = x
        rect_y = y-rect_height

    pygame.draw.rect(Game_Window, bk_color,[rect_x, rect_y, rect_width, rect_height])
    pygame.draw.rect(Game_Window, border_color, [rect_x, rect_y, rect_width, rect_height], 1)
    Game_Window.blit(text_img, [rect_x+3, rect_y+2]) #10, 5

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
            selecter(x, y, Mouse_x, Mouse_y, colors_rb.white)
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
    global Database_connection
    Database_connection.close()
    pygame.quit()
    sys.exit()

def define_player(players=0):
    player = []
    if players < 2:
        return False
    elif players == 2:
        player = [Ballast('green'), Ballast('red')]
        return player
    elif players == 3:
        player = [Ballast('green'), Ballast('yellow'), Ballast('red')]
        return player
    elif players == 4:
        player = [Ballast('green'), Ballast('yellow'), Ballast('red'), Ballast('blue')]
        return player
    else:
        return False

def play_game(players=0):
    global Mouse_x, Mouse_y
    global event
    global Last_six_counter
    global Last_bet_number
    global Game_Window
    global back_button
    global main_background
    global Highlighter, LineEffact_2, LineEffact
    player = define_player(players)
    if not player:
        return False
    total_player = len(player)
    bet_turn = 0
    move_ballast = False
    temp_last_bet_number = 0
    move_ballast_1 = False
    move_ballast_2 = False
    move_ballast_3 = False
    move_ballast_4 = False
    reverse_move = False
    win_flag = False
    reverse_move_ballast = None
    home = 'home'
    win = 'win'
    ballast_highlighter_color_change = 1
    cut_flag = False
    while True:
        for event in pygame.event.get():
            Mouse_x, Mouse_y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                if msg_box('Are you sure,Do yo want to close,this game?', [{'name':'Yes', 'caption':'yes'},{'name':'No','caption':'No'}]) == 'Yes':
                    close_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if msg_box('Are you sure,Do yo want to go back,to main menu?',[{'name':'Yes', 'caption':'yes'},{'name':'No','caption':'No'}]) == 'Yes':
                        return 'Game Menu'
            if event.type == pygame.MOUSEBUTTONDOWN:
                Mouse_x, Mouse_y = event.pos
                if event.button == 1:
                    if back_button.collide(Mouse_x, Mouse_y):
                        if msg_box('Are you sure,Do yo want to go back,to main menu?',
                                   [{'name': 'Yes', 'caption': 'yes'}, {'name': 'No', 'caption': 'No'}]) == 'Yes':
                            return 'Game Menu'
        temp_count = 0
        for e in player:
            if e.Win_status:
                temp_count += 1
        if temp_count == (len(player)-1):
            if msg_box('Game Completed',[{'name':'Replay', 'caption':'Replay Game'},
                                         {'name':'Game Menu','caption':'Go To Main Menu'}]) == 'Replay':
                return 'Replay'
            else:
                return 'Game Menu'

        #Game_Window.fill((255, 255, 255))
        Game_Window.blit(main_background, [0, 0])
        LineEffact.show_effact()
        LineEffact_2.show_effact()
        x, y, x1, y1 = player[bet_turn].Home_border
        #pygame.draw.rect(Game_Window, player[bet_turn].home_highlighter_color, [x, y, x1-x, y1-y])
        Game_Window.blit(Highlighter, [x, y])
        '''if player[bet_turn].home_highlighter_counter <= 200:
            player[bet_turn].home_highlighter_color[0] += 20
            player[bet_turn].home_highlighter_counter += 20
        elif player[bet_turn].home_highlighter_counter <= 400:
            player[bet_turn].home_highlighter_color[0] -= 20
            player[bet_turn].home_highlighter_counter += 20
        elif player[bet_turn].home_highlighter_counter > 400:
            player[bet_turn].home_highlighter_counter = 1
            player[bet_turn].home_highlighter_color = [0, 229, 255]'''

        Game_Window.blit(Game_background, [0, 0])
        back_button.place()
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
                elif (player[bet_turn].Movers_pos_1 != home or player[bet_turn].Movers_pos_2 != home\
                        or player[bet_turn].Movers_pos_3 != home or player[bet_turn].Movers_pos_4 != home):
                    if not (player[bet_turn].validate_moves(Last_bet_number, 1) or\
                            player[bet_turn].validate_moves(Last_bet_number, 2) or\
                            player[bet_turn].validate_moves(Last_bet_number, 3) or\
                            player[bet_turn].validate_moves(Last_bet_number, 4)):
                        move_ballast = False
                        player[bet_turn].bet_status = True
                        bet_turn += 1
                        if bet_turn > total_player - 1:
                            bet_turn = 0
                        Last_six_counter = 0


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_x, mouse_y = event.pos
                        if type(player[bet_turn].Movers_pos_1) != str and player[bet_turn].collide(mouse_x, mouse_y, player[bet_turn].Path[player[bet_turn].Movers_pos_1]):
                            if player[bet_turn].validate_moves(Last_bet_number, 1):
                                move_ballast_1 = True
                        elif type(player[bet_turn].Movers_pos_2) != str and player[bet_turn].collide(mouse_x, mouse_y, player[bet_turn].Path[player[bet_turn].Movers_pos_2]):
                            if player[bet_turn].validate_moves(Last_bet_number, 2):
                                move_ballast_2 = True
                        elif type(player[bet_turn].Movers_pos_3) != str and player[bet_turn].collide(mouse_x, mouse_y, player[bet_turn].Path[player[bet_turn].Movers_pos_3]):
                            if player[bet_turn].validate_moves(Last_bet_number, 3):
                                move_ballast_3 = True
                        elif type(player[bet_turn].Movers_pos_4) != str and player[bet_turn].collide(mouse_x, mouse_y, player[bet_turn].Path[player[bet_turn].Movers_pos_4]):
                            if player[bet_turn].validate_moves(Last_bet_number, 4):
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
                        player[bet_turn].Movers_pos_1 += 1
                        if len(player[bet_turn].Path) == player[bet_turn].Movers_pos_1:
                            player[bet_turn].Movers_pos_1 = win
                            win_flag = True
                        pygame.time.Clock().tick(18)
                    elif move_ballast_2:
                        temp_last_bet_number -= 1
                        player[bet_turn].Movers_pos_2 += 1
                        if len(player[bet_turn].Path) == player[bet_turn].Movers_pos_2:
                            player[bet_turn].Movers_pos_2 = win
                            win_flag = True
                        pygame.time.Clock().tick(18)
                    elif move_ballast_3:
                        temp_last_bet_number -= 1
                        player[bet_turn].Movers_pos_3 += 1
                        if len(player[bet_turn].Path) == player[bet_turn].Movers_pos_3:
                            player[bet_turn].Movers_pos_3 = win
                            win_flag = True
                        pygame.time.Clock().tick(18)
                    elif move_ballast_4:
                        temp_last_bet_number -= 1
                        player[bet_turn].Movers_pos_4 += 1
                        if len(player[bet_turn].Path) == player[bet_turn].Movers_pos_4:
                            player[bet_turn].Movers_pos_4 = win
                            win_flag = True
                        pygame.time.Clock().tick(18)

                    if temp_last_bet_number == 0:
                        if move_ballast_1 and player[bet_turn].Movers_pos_1 != win:
                            for element in player[bet_turn].stop_positions:
                                if element == player[bet_turn].Path[player[bet_turn].Movers_pos_1]:
                                    break
                            else:
                                cut_flag = True
                        elif move_ballast_2 and player[bet_turn].Movers_pos_2 != win:
                            for element in player[bet_turn].stop_positions:
                                if element == player[bet_turn].Path[player[bet_turn].Movers_pos_2]:
                                    break
                            else:
                                cut_flag = True
                        elif move_ballast_3 and player[bet_turn].Movers_pos_3 != win:
                            for element in player[bet_turn].stop_positions:
                                if element == player[bet_turn].Path[player[bet_turn].Movers_pos_3]:
                                    break
                            else:
                                cut_flag = True
                        elif move_ballast_4 and player[bet_turn].Movers_pos_4 != win:
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
                                if Last_bet_number != 6 and not win_flag:
                                    player[bet_turn].bet_status = True
                                    bet_turn += 1
                                    if bet_turn > total_player - 1:
                                        bet_turn = 0
                                    Last_six_counter = 0
                                else:
                                    win_flag = False
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
                            if Last_bet_number != 6 and not win_flag:
                                player[bet_turn].bet_status = True
                                bet_turn += 1
                                if bet_turn > total_player - 1:
                                    bet_turn = 0
                                Last_six_counter = 0
                            else:
                                win_flag = False
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

        for element in player:
            if element.Win_status:
                x, x1, y = element.Winner_name_pos
                custom_out_text(Game_Window, 'You Win', x, x1, y, colors_rb.white, 18, 'Media/Font/Kollektif.ttf')

        if player[bet_turn].Movers_pos_1 == win and player[bet_turn].Movers_pos_2 == win and \
            player[bet_turn].Movers_pos_3 == win and player[bet_turn].Movers_pos_4 == win:
            player[bet_turn].Win_status = True
        while player[bet_turn].Win_status:
            move_ballast_1 = False
            move_ballast_2 = False
            move_ballast_3 = False
            move_ballast_4 = False
            move_ballast = False
            player[bet_turn].bet_status = True
            bet_turn += 1
            if bet_turn > total_player - 1:
                bet_turn = 0
            Last_six_counter = 0
            if player[bet_turn].Movers_pos_1 == win and player[bet_turn].Movers_pos_2 == win and \
                    player[bet_turn].Movers_pos_3 == win and player[bet_turn].Movers_pos_4 == win:
                player[bet_turn].Win_status = True

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
        x, x1, y = player[bet_turn].Winner_name_pos
        if not player[bet_turn].Win_status:
            custom_out_text(Game_Window, 'Your Turn', x, x1, y, colors_rb.white, 18, 'Media/Font/Kollektif.ttf')
        pygame.display.update()



def profile():
    global profile_img
    global Line_effact, LineEffact_2
    global Game_Window
    global Mouse_x, Mouse_y
    global setting_background
    global event
    global back_button

    facebook = Button(Game_Window, 'Media/Image/Icon/facebook_white.png', 'Media/Image/Icon/facebook_white.png', 338, 642,
                             press_effact=True, caption_text='facebook.com/brightgoal.in.Education/')
    brightgoal = Button(Game_Window, 'Media/Image/Icon/brightgoal_white.png', 'Media/Image/Icon/brightgoal_white.png', 382,
                        642, press_effact=True, caption_text='brightgoal.in')
    youtube = Button(Game_Window, 'Media/Image/Icon/youtube_white.png', 'Media/Image/Icon/youtube_white.png', 426, 642,
                            press_effact=True, caption_text='youtube.com/brightgoal')
    twitter = Button(Game_Window, 'Media/Image/Icon/twitter_white.png', 'Media/Image/Icon/twitter_white.png', 470, 642,
                            press_effact=True, caption_text='twitter.com/brightgoal_in')
    instagram = Button(Game_Window, 'Media/Image/Icon/instagram_white.png', 'Media/Image/Icon/instagram_white.png', 514, 642,
                          press_effact=True, caption_text='instagram.com/brightgoal.in')
    whatsapp = Button(Game_Window, 'Media/Image/Icon/whatsapp_white.png', 'Media/Image/Icon/whatsapp_white.png', 558, 642,
                             press_effact=True, caption_text='9140417112')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Mouse_x, Mouse_y = event.pos
                    if back_button.collide(Mouse_x, Mouse_y):
                        return
                    if facebook.collide(Mouse_x, Mouse_y):
                        open_url('https://www.facebook.com/brightgoal.in.Education/')
                    if brightgoal.collide(Mouse_x, Mouse_y):
                        open_url('https://www.brightgoal.in/')
                    if instagram.collide(Mouse_x, Mouse_y):
                        open_url('https://www.instagram.com/brightgoal.in/')
                    if twitter.collide(Mouse_x, Mouse_y):
                        open_url('https://twitter.com/brightgoal_in')
                    if youtube.collide(Mouse_x, Mouse_y):
                        open_url('https://youtube.com/brightgoal')
                    if whatsapp.collide(Mouse_x, Mouse_y):
                        open_url('https://wa.me/919140417112')

        Game_Window.blit(setting_background, [0, 0])
        LineEffact.show_effact()
        LineEffact_2.show_effact()
        Game_Window.blit(profile_img, [0, 0])
        back_button.place()
        whatsapp.place()
        instagram.place()
        twitter.place()
        youtube.place()
        brightgoal.place()
        facebook.place()
        pygame.display.update()

class List_menu:
    def __init__(self, surface, x, y, bg_image, selector, hover_selector = None, buttons = [], button_distance = 5, top_padding = 5, text_size = 14, text_color = colors_rb.white, hover_text_color = colors_rb.white, text_file = 'Media/Font/Kollektif.ttf'):
        self.background = bg_image
        self.selector = selector
        if hover_selector != None:
            self.hover_selector = hover_selector
        else:
            self.hover_selector = self.selector
        self.surface = surface
        self.x = x
        self.y = y
        self.buttons = []
        self.top_padding = top_padding
        self.button_distance = button_distance
        self.list_width = self.background.get_width()
        self.list_height = self.background.get_height()
        self.buttons_y = self.x+self.top_padding
        self.buttons_x = (self.x + self.list_width/2) - (self.selector.get_width()/2)
        self.buttons_end_y = self.buttons_y
        start_point_y = self.buttons_y
        step_value = self.selector.get_height()+self.button_distance
        for button_name in buttons:
            self.buttons_end_y = start_point_y+self.selector.get_height()
            self.buttons.append(Button(self.surface, self.selector, self.hover_selector, self.buttons_x, start_point_y,
                                       button_text=button_name, button_text_size=text_size, button_text_color=text_color,
                                       text_file=text_file))
            start_point_y += step_value
            if start_point_y+self.top_padding >= (self.y + self.list_height):
                break

        self.list_state = False
        if self.list_height - (self.buttons_end_y - self.y) > self.top_padding:
            crop_Image('Media/Image/List_menu/background.png', 'Media/Image/List_menu/temp_background.png', 0, 0, self.list_width, self.buttons_end_y - self.y+self.top_padding)
            self.background = pygame.image.load('Media/Image/List_menu/temp_background.png')

    def place(self):
        if self.list_state:
            self.surface.blit(self.background, [self.x, self.y])
            for button in self.buttons:
                button.place()


class List_menu1:
    def __init__(self, surface, x, y, width, height, bk_color, border_color, state = False):
        self.x = x
        self.y = y
        self.surface = surface
        self.x1 = x+width
        self.y1 = y+height
        self.bk_color = bk_color
        self.border_color = border_color
        self.state = state
        self.height = height
        if self.state:
            self.width = width
        else:
            self.width = 0
        self.speed_value = 25
    def place(self):
        if self.state:
            if self.width < self.x1-self.x:
                self.width += self.speed_value
            pygame.draw.rect(self.surface, self.bk_color, [self.x, self.y, self.width, self.height])
            pygame.draw.rect(self.surface, self.border_color, [self.x, self.y, self.width, self.height], 1)
        else:
            if self.width > 0:
                self.width -= self.speed_value
            if self.width > 0:
                pygame.draw.rect(self.surface, self.bk_color, [self.x, self.y, self.width, self.height])
                pygame.draw.rect(self.surface, self.border_color, [self.x, self.y, self.width, self.height], 1)

def crop_Image(image, output_file_name, x, y, x1, y1):
    img = Image.open(image)
    img = img.crop((x, y, x1, y1))
    img.save(output_file_name)



def more_products():
    global profile_img
    global Line_effact, LineEffact_2
    global Game_Window
    global Mouse_x, Mouse_y
    global setting_background
    global event
    global back_button
    global List_menu_background
    global List_menu_selector
    global hover_selector
    Menu = List_menu(Game_Window, 20, 20, List_menu_background, List_menu_selector, hover_selector,
                     ['Button 1', 'Button 2', 'Button 3', 'Button 4', 'Button 5', 'Button 6', 'Button 7', 'Button 8',
                      'Button 9', 'Button 10', 'Button 11', 'Button 12', 'Button 13', 'Button 14', 'Button 15'], text_size=14,
                     text_file='Media/Font/Raleway-Medium.ttf')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Mouse_x, Mouse_y = event.pos
                    if Menu.list_state:
                        for button in Menu.buttons:
                            if button.collide(Mouse_x, Mouse_y):
                                print(button.button_text)
                    if back_button.collide(Mouse_x,  Mouse_y):
                        if Menu.list_state:
                            Menu.list_state = False
                        else:
                            Menu.list_state = True
        Game_Window.blit(setting_background, [0, 0])
        LineEffact.show_effact()
        LineEffact_2.show_effact()
        Game_Window.blit(setting_background_logo, [0, 0])
        Menu.place()
        back_button.place()
        pygame.display.update()


def choose_player():
    global setting_background
    global setting_background_logo
    global back_button
    global Game_Window
    global LineEffact, LineEffact_2
    global event
    global brightgoal_button
    global facebook_button, twitter_button, insta_button, whatsapp_button, youtube_button
    global more_product
    button_2 = Button(Game_Window, 'Media/Image/c_players/button.png', 'Media/Image/c_players/shadow_button.png',
                      295, 250, button_text='2')
    button_3 = Button(Game_Window, 'Media/Image/c_players/button.png', 'Media/Image/c_players/shadow_button.png',
                      410, 250, button_text='3')
    button_4 = Button(Game_Window, 'Media/Image/c_players/button.png', 'Media/Image/c_players/shadow_button.png',
                      525, 250, button_text='4')
    last_players = None
    ads_txt = Message(Game_Window, [280, 400, 640, 500], 'If you want to download more Project,of python then click on,More Product', 22, font_file='Media/Font/adventpro-bold.ttf')
    note_text = Message(Game_Window, [280, 120, 640, 220], 'How many Players wants to Play,Choose number of players', 22, font_file='Media/Font/adventpro-bold.ttf')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if more_product.collide(mouse_x, mouse_y):
                        open_url('https://www.instamojo.com/Brightgoal')
                    if facebook_button.collide(mouse_x, mouse_y):
                        re_value = msg_box('Facebook Page:,https://www.facebook.com/,brightgoal.in.Education/',
                                           [{'name': 'Open in browser'}, {'name': 'Copy to clipboard'}])
                        if re_value == 'Copy to clipboard':
                            clipboard.copy('https://www.facebook.com/brightgoal.in.Education/')
                        elif re_value == 'Open in browser':
                            open_url('https://www.facebook.com/brightgoal.in.Education/')
                    if brightgoal_button.collide(mouse_x, mouse_y):
                        re_value = msg_box('Website Link:,https://www.brightgoal.in/',
                                           [{'name': 'Open in browser'}, {'name': 'Copy to clipboard'}])
                        if re_value == 'Copy to clipboard':
                            clipboard.copy('https://www.brightgoal.in/')
                        elif re_value == 'Open in browser':
                            open_url('https://www.brightgoal.in/')
                    if insta_button.collide(mouse_x, mouse_y):
                        re_value = msg_box('Instagram link:,https://www.instagram.com,/brightgoal.in/',
                                           [{'name': 'Open in browser'}, {'name': 'Copy to clipboard'}])
                        if re_value == 'Copy to clipboard':
                            clipboard.copy('https://www.instagram.com/brightgoal.in/')
                        elif re_value == 'Open in browser':
                            open_url('https://www.instagram.com/brightgoal.in/')
                    if twitter_button.collide(mouse_x, mouse_y):
                        re_value = msg_box('Twitter Link:,https://twitter.com/brightgoal_in',
                                           [{'name': 'Open in browser'}, {'name': 'Copy to clipboard'}])
                        if re_value == 'Copy to clipboard':
                            clipboard.copy('https://twitter.com/brightgoal_in')
                        elif re_value == 'Open in browser':
                            open_url('https://twitter.com/brightgoal_in')
                    if youtube_button.collide(mouse_x, mouse_y):
                        re_value = msg_box('Youtube Link:,https://youtube.com/brightgoal',
                                           [{'name': 'Open in browser'}, {'name': 'Copy to clipboard'}])
                        if re_value == 'Copy to clipboard':
                            clipboard.copy('https://youtube.com/brightgoal')
                        elif re_value == 'Open in browser':
                            open_url('https://youtube.com/brightgoal')
                    if whatsapp_button.collide(mouse_x, mouse_y):
                        if msg_box('WhatsApp Number,9140417112',
                                   [{'name': 'Copy to clipboard'}]) == 'Copy to clipboard':
                            clipboard.copy('9140417112')
                    if back_button.collide(mouse_x, mouse_y):
                        return
                    if button_2.collide(mouse_x, mouse_y):
                        last_players = 2
                    if button_3.collide(mouse_x, mouse_y):
                        last_players = 3
                    if button_4.collide(mouse_x, mouse_y):
                        last_players = 4
                    if last_players != None:
                        while True:
                            return_value = play_game(last_players)
                            if return_value == 'Game Menu':
                                return True
        Game_Window.blit(setting_background, [0, 0])
        LineEffact.show_effact()
        LineEffact_2.show_effact()
        Game_Window.blit(setting_background_logo, [0, 0])
        custom_out_text(Game_Window, 'Players', 0, 920, 90, colors_rb.white, 28, 'Media/Font/adventpro-bold.ttf')
        ads_txt.plase()
        note_text.plase()
        back_button.place()
        button_2.place()
        button_3.place()
        button_4.place()
        whatsapp_button.place()
        insta_button.place()
        twitter_button.place()
        youtube_button.place()
        brightgoal_button.place()
        facebook_button.place()
        more_product.place()
        pygame.display.update()

def main_menu():
    global Game_Window
    global Mouse_x, Mouse_y
    global event
    global main_menu_img
    global visit_on_website
    global setting_background
    global LineEffact_2
    global LineEffact
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
                if event.key == pygame.K_RETURN:
                    if option_rect == 0:
                        choose_player()
                    elif option_rect == 1:
                        setting()
                    elif option_rect == 2:
                        profile()
                    elif option_rect == 3:
                        more_products()
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
                    choose_player()
                elif collide(Mouse_x, Mouse_y, options_rect_positions[1]):
                    setting()
                elif collide(Mouse_x, Mouse_y, options_rect_positions[2]):
                    profile()
                elif collide(Mouse_x, Mouse_y, options_rect_positions[3]):
                    more_products()

        if collide(Mouse_x, Mouse_y, options_rect_positions[0]):
            option_rect = 0
        if collide(Mouse_x, Mouse_y, options_rect_positions[1]):
            option_rect = 1
        if collide(Mouse_x, Mouse_y, options_rect_positions[2]):
            option_rect = 2
        if collide(Mouse_x, Mouse_y, options_rect_positions[3]):
            option_rect = 3
        Game_Window.blit(setting_background, [0, 0])
        LineEffact_2.show_effact()
        LineEffact.show_effact()
        Game_Window.blit(main_menu_img, [0, 0])
        visit_on_website.place()
        x, y, x1, y1 = options_rect_positions[option_rect]
        if option_rect_color_flag:
            pygame.draw.rect(Game_Window, colors_rb.light_blue, [x, y, x1 - x, y1 - y], 4)
        else:
            pygame.draw.rect(Game_Window, colors_rb.light_green, [x, y, x1-x, y1-y], 4)
        pygame.display.update()

def out_text(text, size, x, y, color, font_style=None, bk_color=None):
    global GameWindow
    font = pygame.font.SysFont(font_style, size)
    text_img = font.render(text, True, color, bk_color)
    GameWindow.blit(text_img, [x, y])


def out_text_file(surface, text, size, x, y, color, font_file, return_img = False, bk_color=None):
    try:
        font = pygame.font.Font(font_file, size)
    except OSError:
        font = pygame.font.SysFont(None, size)
    text_img = font.render(text, True, color, bk_color)
    if return_img:
        return text_img
    surface.blit(text_img, [x, y])


def custom_out_text(surface, text, x, x1, y, color, size, f_file = "Media/Font/Kollektif.ttf"):
    text_img = out_text_file(surface, text, size, 0, 0, color, f_file, True)
    put_point_x = x + ((x1 - x) // 2)
    put_point_x = put_point_x - (text_img.get_width() // 2)
    surface.blit(text_img, [put_point_x, y])


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

class Message:
    def __init__(self, surface, rect, message='', text_size = 17, text_color = colors_rb.white, text_align = 'center', font_file = 'Media/Font/DroidSansMono.ttf'):
        global Game_Window
        self.message = message
        self.message_area = rect
        self.text_size = text_size
        self.color = text_color
        self.text_align = text_align
        self.message_status = False
        self.surface = surface
        self.message_list_img = []
        self.message_starting_y_point = 0
        if type(rect) == list or type(rect) == tuple:
            x, y, x1, y1 = rect
        else:
            return
        if len(message) == 0:
            return
        self.center_x = int(((x1 - x)/2) + x)
        message_list = message.split(',')
        rect_width = x1 - x
        rect_height = y1-y
        max_width_line = 0
        while True:
            for e in message_list:
                img = out_text_file(Game_Window, e,self.text_size, 0, 0, self.color, font_file, True)
                if img.get_width() > max_width_line:
                    max_width_line = img.get_width()
                self.message_list_img.append(img)
            if max_width_line > rect_width:
                max_width_line = 0
                self.text_size -= 1
                text_size -= 1
                self.message_list_img  = []
                if self.text_size < 8:
                    return
                continue
            total_height = self.message_list_img[0].get_height()+1
            total_height = total_height*len(self.message_list_img)
            if total_height > rect_height:
                text_size -= 1
                self.text_size -= 1
                self.message_list_img = []
                if self.text_size < 8:
                    return
                continue
            else:
                break
        message_list_lenth = len(self.message_list_img)
        center_y = y + ((y1 - y)/2)
        if message_list_lenth % 2 == 0:
            starting_pos = (center_y - 2)
            half_msg = int((message_list_lenth) / 2)
        else:
            starting_pos = center_y - int(self.message_list_img[0].get_height()/2)
            half_msg = int((message_list_lenth-1)/2)
        line_height = self.message_list_img[0].get_height()
        while half_msg != 0:
            starting_pos -= line_height
            half_msg -= 1
        self.message_status = True
        self.message_starting_y_point = starting_pos

    def config(self, surface=None, rect=None, message=None, text_size = None, text_color = None):
        if surface != None or rect != None or message != None or text_size != None or text_color != None:
            self.__init__(surface if surface!= None else self.surface, rect if rect!=None else self.message_area,
                          message if message!=None else self.message, text_size if text_size!=None else self.text_size,
                          text_color if text_color!=None else self.color)
            return True
        else:
            return False

    def plase(self):
        if self.text_align == 'left' or self.text_align == 'right':
            x, y, x1, y1 = self.message_area
            start_point_y = y+2
        else:
            start_point_y = self.message_starting_y_point
        if self.message_status:
            for e in self.message_list_img:
                if self.text_align == 'center':
                    x = self.center_x - (e.get_width()/2)
                elif self.text_align == 'left':
                    x, y, x1, y1 = self.message_area
                    x += 2
                elif self.text_align == 'right':
                    x, y, x1, y1 = self.message_area
                    x = x1 - (e.get_width()+2)
                self.surface.blit(e, [x, start_point_y])
                start_point_y += self.text_size+3

class Text_button:
    def __init__(self, surface, x, y, text, text_size, text_color, bk_color, border_color=None, hover_text_color=None, hover_bk_color=None, hover_border_color=None, caption=None):
        self.Text = text
        self.x = x
        self.y = y
        self.caption = caption
        self.font_file = 'Media/Font/Gidole-Regular.otf'
        self.Text_size = text_size
        self.surface = surface
        self.color = text_color
        if hover_text_color != None:
            self.hover_color = hover_text_color
        else:
            self.hover_color = text_color
        self.bk_color = bk_color
        if hover_bk_color != None:
            self.hover_bk_color = hover_bk_color
        else:
            self.hover_bk_color = bk_color
        self.border_color = border_color
        if hover_border_color != None:
            self.hover_border_color = hover_border_color
        else:
            self.hover_border_color = border_color
        self.text_img = out_text_file(self.surface, self.Text ,self.Text_size, 0, 0, self.color, self.font_file, True)
        if hover_text_color != None:
            self.hover_text_img = out_text_file(self.surface, self.Text, self.Text_size, 0, 0, self.hover_color,
                                          self.font_file, True)
        else:
            self.hover_text_img = self.text_img
        self.button_width = self.text_img.get_width()+10
        self.button_height = self.text_img.get_height()+4

    def collide(self, x, y):
        if (x >= self.x) and (x <= self.x+self.button_width) and (y >= self.y) and (y <= self.y+self.button_height):
            return True
        else:
            return False

    def config_pos(self, x, y):
        self.x = x
        self.y = y

    def place(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.collide(mouse_x, mouse_y):
            pygame.draw.rect(self.surface, self.hover_bk_color, [self.x, self.y, self.button_width, self.button_height])
        else:
            pygame.draw.rect(self.surface, self.bk_color, [self.x, self.y, self.button_width, self.button_height])
        if self.collide(mouse_x, mouse_y) and self.hover_border_color != None:
            pygame.draw.rect(self.surface, self.hover_border_color,
                             [self.x, self.y, self.button_width, self.button_height], 1)
        elif self.border_color != None:
            pygame.draw.rect(self.surface, self.border_color,
                             [self.x, self.y, self.button_width, self.button_height], 1)
        if self.collide(mouse_x, mouse_y):
            self.surface.blit(self.hover_text_img, [self.x + 5, self.y + 2])
        else:
            self.surface.blit(self.text_img, [self.x+5, self.y+2])
        if self.caption != None and len(self.caption) != 0:
            if self.collide(mouse_x, mouse_y):
                caption(self.caption, self.x + self.button_width, self.y - self.button_height, border_color=colors_rb.light_orange)

def msg_box(text, button=None, text_align='center'):
    global event
    global msg_box_img
    global Game_Window
    global Game_background
    global Mouse_y, Mouse_x
    value = lambda dict, key: dict[key] if key in dict else ''
    pygame.image.save(Game_Window, 'Temp.png')
    bg_image = pygame.image.load('Temp.png')
    close_button = Button(Game_Window, 'Media/Image/Icon/orange_close.png', 'Media/Image/Icon/white_close.png', 612, 275, 'Close')
    with_button_msg_area = [300, 272, 608, 400]
    without_button_msg_area = [300, 272, 608, 423]
    button_area = [300, 402, 608, 426]
    Buttons = []
    if button != None and type(button) == list:
        msg = Message(Game_Window, with_button_msg_area, text, text_align=text_align)
        button.reverse()
        for e in button:
            if len(Buttons) == 0:
                btn = Text_button(Game_Window, 0, 0, value(e, 'name'), 14, colors_rb.white, colors_rb.light_orange,
                                  hover_text_color = colors_rb.light_black, hover_bk_color= colors_rb.white,
                                  caption=value(e, 'caption'))
                btn.config_pos(608-btn.button_width, 402)
                Buttons.append(btn)
            else:
                btn = Text_button(Game_Window, 0, 0, value(e, 'name'), 14, colors_rb.white, colors_rb.light_orange,
                                  hover_text_color=colors_rb.light_black, hover_bk_color=colors_rb.white,
                                  caption=value(e, 'caption'))
                btn_x = Buttons[len(Buttons)-1].x - (btn.button_width+10)
                if btn_x < 300:
                    break
                btn.config_pos(btn_x, 402)
                Buttons.append(btn)
    else:
        msg = Message(Game_Window, without_button_msg_area, text, text_align=text_align)
    close_msg = False
    show_msg = False
    width = 0
    height = 0
    x = 460
    y = 344
    temp_msg_box = msg_box_img
    close_msg_box = msg_box_img
    return_text = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Mouse_x, Mouse_y = event.pos
                    if len(Buttons) != 0:
                        for e in Buttons:
                            if e.collide(Mouse_x, Mouse_y):
                                return_text = e.Text
                                close_msg = True
                    if close_button.collide(Mouse_x, Mouse_y):
                        close_msg = True

        Game_Window.blit(bg_image, [0, 0])
        if not show_msg and not close_msg:
            width += 92
            height += 69
            x -= 46
            y -= 34
            temp_msg_box = pygame.transform.scale(msg_box_img, (width, height)).convert_alpha()
            close_msg_box = temp_msg_box
            if x <= 0 or y <= 0:
                show_msg = True

        if close_msg:
            width -= 46
            height -= 34
            x += 23
            y += 17
            temp_msg_box = pygame.transform.scale(close_msg_box, (width, height)).convert_alpha()
            if width <= 0 or height <= 0:
                if return_text != None:
                    return return_text
                else:
                    return True

        if show_msg and not close_msg:
            Game_Window.blit(msg_box_img, [0, 0])
            close_button.place()
            msg.plase()
            if button != None:
                for e in Buttons:
                    e.place()
        else:
            Game_Window.blit(temp_msg_box, [x, y])
        pygame.display.update()

class Scroll_Button:
    def __init__(self,surface, x, x1, y, bar_thickness, pointer_img, pointer_hover_img = None, zero_value_pinter_img = None,
                 zero_value_pointer_hover_img = None, defult_value = None):
        self.surface = surface
        self.x = x
        self.x1 = x1
        self.y = y
        self.thickness = bar_thickness
        self.pointer_img = pointer_img
        self.pointer_hover_img = pointer_hover_img if pointer_hover_img!=None else self.pointer_img
        self.zero_value_pointer_img = zero_value_pinter_img if zero_value_pinter_img!=None else self.pointer_img
        self.zero_value_pointer_hover_img = zero_value_pointer_hover_img if zero_value_pinter_img!=None and zero_value_pointer_hover_img!=None else self.zero_value_pointer_img if zero_value_pinter_img!=None else self.pointer_hover_img
        self.pointer_img = pygame.image.load(self.pointer_img)
        self.pointer_hover_img = pygame.image.load(self.pointer_hover_img)
        self.zero_value_pointer_img = pygame.image.load(self.zero_value_pointer_img)
        self.zero_value_pointer_hover_img = pygame.image.load(self.zero_value_pointer_hover_img)
        self.value = float(0)
        self.pointer_width = self.pointer_img.get_width()
        self.pointer_height = self.pointer_img.get_height()
        self.step_value = 100/(((self.x1-self.x)+2)-self.pointer_width)
        self.pointer_x = self.x-1
        if defult_value != None:
            self.pointer_x = self.pointer_x+int(defult_value/self.step_value)
            self.value = defult_value
        self.pointer_y = (self.y + int(self.thickness/2))-int(self.pointer_height/2)
        self.move_pointer = False
        self.pointer_mouse_dis = 0
        self.font_size = self.thickness+12
        self.persentage_y = (self.y+(self.thickness/2))-(self.font_size/2)
    def config_value(self, persentage):
        self.pointer_x = (self.x-1) + (int(persentage / self.step_value))
        self.value = persentage
    def place(self, event_list = None):
        global colors_rb
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event_list != None:
            for events in event_list:

                if events.type == pygame.MOUSEBUTTONDOWN:
                    if events.button == 1:
                        mouse_x, mouse_y = events.pos
                        if collide(mouse_x, mouse_y, [self.pointer_x, self.pointer_y, self.pointer_x+self.pointer_width, self.pointer_y+self.pointer_height]):
                            self.pointer_mouse_dis = mouse_x - self.pointer_x
                            self.move_pointer = True
                if events.type == pygame.MOUSEBUTTONUP:
                    if events.button == 1:
                        self.move_pointer = False
        if self.move_pointer:
            if mouse_x-self.pointer_mouse_dis >= self.x and mouse_x-self.pointer_mouse_dis <= self.x1-self.pointer_width:
                self.pointer_x = mouse_x-self.pointer_mouse_dis
            if mouse_x-self.pointer_mouse_dis < self.x:
                self.pointer_x = self.x-1
            if mouse_x-self.pointer_mouse_dis > self.x1-self.pointer_width:
                self.pointer_x = self.x1-self.pointer_width+1
            self.value = (self.pointer_x - (self.x-1))*self.step_value
            custom_out_text(Game_Window, str(int(self.value))+'%', self.x1+15, self.x1+45, self.persentage_y, colors_rb.white, self.font_size, 'Media/Font/Kollektif.ttf')

        pygame.draw.rect(self.surface, colors_rb.white,
                         [self.x, self.y, self.x1 - self.x, self.thickness])
        pygame.draw.rect(self.surface, colors_rb.light_blue, [self.x, self.y, self.pointer_x-self.x+2, self.thickness])
        if self.value <= 0:
            if self.move_pointer or collide(mouse_x, mouse_y, [self.pointer_x, self.pointer_y, self.pointer_x+self.pointer_width, self.pointer_y+self.pointer_height]):
                self.surface.blit(self.zero_value_pointer_hover_img, [self.pointer_x, self.pointer_y])
            else:
                self.surface.blit(self.zero_value_pointer_img, [self.pointer_x, self.pointer_y])
        else:
            if self.move_pointer or collide(mouse_x, mouse_y, [self.pointer_x, self.pointer_y, self.pointer_x+self.pointer_width, self.pointer_y+self.pointer_height]):
                self.surface.blit(self.pointer_hover_img, [self.pointer_x, self.pointer_y])
            else:
                self.surface.blit(self.pointer_img, [self.pointer_x, self.pointer_y])

def open_url(url):
    import webbrowser
    try:
        webbrowser.get('chrome').open_new(url)
    except:
        try:
            webbrowser.get('firefox').open_new_tab(url)
        except:
            try:
                webbrowser.open(url, new=1)
            except:
                return False
    return True

def setting():
    global LineEffact, LineEffact_3, LineEffact_2
    global Mouse_x, Mouse_y
    global setting_background
    global event
    global colors_rb
    global Game_Window
    global Music_volume
    global Sound_volume
    global setting_background_logo
    global back_button
    global brightgoal_button
    global facebook_button, twitter_button, insta_button, whatsapp_button, youtube_button
    global more_product
    check_Setting()
    speker_blue = ('Media/Image/Icon/speaker-blue.png')
    sperker_darkblue = ('Media/Image/Icon/speaker-darkblue.png')
    mute_blue = ('Media/Image/Icon/mute-blue.png')
    mute_darkblue = ('Media/Image/Icon/mute-darkblue.png')
    music_button = Scroll_Button(Game_Window,314, 822, 218, 8, speker_blue, sperker_darkblue, mute_blue, mute_darkblue,
                                 defult_value=Music_volume)
    sound_button = Scroll_Button(Game_Window,314, 822, 299, 8, speker_blue, sperker_darkblue, mute_blue, mute_darkblue,
                                  defult_value=Sound_volume)
    save_setting_button = Button(Game_Window, 'Media/Image/setting/Save_setting_black.png',
                          'Media/Image/setting/Save_setting_green.png', 652, 370)
    reset_setting_button = Button(Game_Window, 'Media/Image/setting/Reset_setting_black.png', 'Media/Image/setting/Reset_setting_green.png', 452, 370)
    facebook_button = Button(Game_Window, 'Media/Image/Icon/facebook.png', 'Media/Image/Icon/facebook.png', 339, 510, press_effact=True, caption_text='facebook.com/brightgoal.in.Education/')
    brightgoal_button = Button(Game_Window, 'Media/Image/Icon/brightgoal.png', 'Media/Image/Icon/brightgoal.png', 381, 510, press_effact=True, caption_text='brightgoal.in')
    youtube_button = Button(Game_Window, 'Media/Image/Icon/youtube.png', 'Media/Image/Icon/youtube.png', 423, 510, press_effact=True, caption_text='youtube.com/brightgoal')
    twitter_button = Button(Game_Window, 'Media/Image/Icon/twitter.png', 'Media/Image/Icon/twitter.png', 465, 510, press_effact=True, caption_text='twitter.com/brightgoal_in')
    insta_button = Button(Game_Window, 'Media/Image/Icon/insta.png', 'Media/Image/Icon/insta.png', 507, 510,
                            press_effact=True, caption_text='instagram.com/brightgoal.in')
    whatsapp_button = Button(Game_Window, 'Media/Image/Icon/whatsapp.png', 'Media/Image/Icon/whatsapp.png', 549, 510,
                            press_effact=True, caption_text='9140417112')
    more_product = Button(Game_Window, 'Media/Image/setting/more_product_black.png', 'Media/Image/setting/more_product_green.png', 375, 570, caption_text='https://www.instamojo.com/Brightgoal')
    event_list = []
    while True:
        for event in pygame.event.get():
            event_list.append(event)
            if event.type == pygame.QUIT:
                close_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.posmouse_x, mouse_y = event.pos
                    if more_product.collide(mouse_x, mouse_y):
                        open_url('https://www.instamojo.com/Brightgoal')
                    if facebook_button.collide(mouse_x, mouse_y):
                        re_value = msg_box('Facebook Page:,https://www.facebook.com/,brightgoal.in.Education/',
                                           [{'name': 'Open in browser'}, {'name': 'Copy to clipboard'}])
                        if re_value == 'Copy to clipboard':
                            clipboard.copy('https://www.facebook.com/brightgoal.in.Education/')
                        elif re_value == 'Open in browser':
                            open_url('https://www.facebook.com/brightgoal.in.Education/')
                    if brightgoal_button.collide(mouse_x, mouse_y):
                        re_value = msg_box('Website Link:,https://www.brightgoal.in/',
                                           [{'name': 'Open in browser'}, {'name': 'Copy to clipboard'}])
                        if re_value == 'Copy to clipboard':
                            clipboard.copy('https://www.brightgoal.in/')
                        elif re_value == 'Open in browser':
                            open_url('https://www.brightgoal.in/')
                    if insta_button.collide(mouse_x, mouse_y):
                        re_value = msg_box('Instagram link:,https://www.instagram.com,/brightgoal.in/', [{'name':'Open in browser'},{'name':'Copy to clipboard'}])
                        if re_value == 'Copy to clipboard':
                            clipboard.copy('https://www.instagram.com/brightgoal.in/')
                        elif re_value == 'Open in browser':
                            open_url('https://www.instagram.com/brightgoal.in/')
                    if twitter_button.collide(mouse_x, mouse_y):
                        re_value = msg_box('Twitter Link:,https://twitter.com/brightgoal_in', [{'name':'Open in browser'},{'name':'Copy to clipboard'}])
                        if re_value == 'Copy to clipboard':
                            clipboard.copy('https://twitter.com/brightgoal_in')
                        elif re_value == 'Open in browser':
                            open_url('https://twitter.com/brightgoal_in')
                    if youtube_button.collide(mouse_x, mouse_y):
                        re_value = msg_box('Youtube Link:,https://youtube.com/brightgoal',
                                           [{'name': 'Open in browser'}, {'name': 'Copy to clipboard'}])
                        if re_value == 'Copy to clipboard':
                            clipboard.copy('https://youtube.com/brightgoal')
                        elif re_value == 'Open in browser':
                            open_url('https://youtube.com/brightgoal')
                    if whatsapp_button.collide(mouse_x, mouse_y):
                        if msg_box('WhatsApp Number,9140417112',[{'name':'Copy to clipboard'}]) == 'Copy to clipboard':
                            clipboard.copy('9140417112')
                    if save_setting_button.collide(mouse_x, mouse_y):
                        update_setting('Setting', '_id', 12345, {'Sound volume': sound_button.value,
                                                                 'Music volume':music_button.value})
                        check_Setting()
                    if reset_setting_button.collide(mouse_x, mouse_y):
                        update_setting('Setting', '_id', 12345, {'Sound volume': 100,
                                                                 'Music volume': 100})
                        check_Setting()
                        sound_button.config_value(Sound_volume)
                        music_button.config_value(Music_volume)
                    if back_button.collide(mouse_x, mouse_y):
                        return

        Game_Window.blit(setting_background, [0, 0])
        LineEffact.show_effact()
        LineEffact_2.show_effact()
        Game_Window.blit(setting_background_logo, [0, 0])
        back_button.place()
        custom_out_text(Game_Window, 'Setting', 0, 920, 90, colors_rb.white, 28, 'Media/Font/adventpro-bold.ttf')
        out_text_file(Game_Window, 'Background Music', 24, 80, 207, colors_rb.white, 'Media/Font/adventpro-bold.ttf')
        out_text_file(Game_Window, "Sound Effact's", 24, 80, 284, colors_rb.white, 'Media/Font/adventpro-bold.ttf')
        music_button.place(event_list)
        sound_button.place(event_list)
        save_setting_button.place()
        reset_setting_button.place()
        whatsapp_button.place()
        insta_button.place()
        twitter_button.place()
        youtube_button.place()
        brightgoal_button.place()
        facebook_button.place()
        more_product.place()
        event_list = []
        pygame.display.update()

main_menu()
