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
    def __init__(self, color_type):
        if color_type == 'green':
            self.Bet_block = [815, 491, 910, 588]
        elif color_type == 'yellow':
            self.Bet_block = [10, 492, 106, 588]
        elif color_type == 'red':
            self.Bet_block = [9, 61, 105, 158]
        elif color_type == 'blue':
            self.Bet_block = [814, 62, 912, 158]
        self.Bet_status = True
        self.Bet_flag = False
        self.Bet_itration = None
        self.last_bet_number = None

    @staticmethod
    def collide(mouse_x, mouse_y, rect):
        x, y, x1, y1 = rect
        if (mouse_x > x) and (mouse_x < x1) and (mouse_y > y) and (mouse_y < y1):
            return True
        else:
            return False

    def bet_manage(self, events):
        global Game_Window
        if events.type == pygame.MOUSEBUTTONDOWN:
            if events.button == 1:
                mouse_x, mouse_y = events.pos
                if self.collide(mouse_x, mouse_y, self.Bet_block) and self.Bet_status:
                    self.Bet_status = True
                    self.Bet_flag = True
                    self.Bet_itration = self.bet_now()

        if self.Bet_flag:
            try:
                next(self.Bet_itration)
            except StopIteration:
                self.Bet_flag = False
        else:
            Game_Window.blit(Ballast_img[0], [829, 506])

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


# Global variables.
Mouse_x = 0
Mouse_y = 0
event = None
colors_rb = Colors()


def close_game():
    pygame.quit()
    sys.exit()


# Main menu Creation.

b1 = Ballast('green')
event_list = []
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
    pygame.display.update()
