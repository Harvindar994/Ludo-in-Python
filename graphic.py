import pygame
pygame.init()

class Colors:
    white = (255, 255, 255)
    orange = (252, 82, 59)
    light_black = (43, 43, 43)
    light_gray = (166, 166, 166)
    light_green = (97, 227, 31)
    light_blue = (0, 133, 255)
    light_orange = (255, 61, 0)



# Loading Image.
List_menu_background = pygame.image.load('Media/Image/List_menu/light_blue.png')
List_menu_selector = pygame.image.load('Media/Image/List_menu/selector.png')
hover_selector = pygame.image.load('Media/Image/List_menu/hover_selector.png')
main_background = pygame.image.load("Media/Image/main_background.png")


# Creating Game screen.
Game_Window = pygame.display.set_mode((920, 689), 0, 0)
pygame.display.set_caption('Ludo')

# Global Variables
colors_rb = Colors()


class Button:
    def __init__(self, surface, image, hover_img, x, y, caption_text = '', press_effact = False, button_text = None,
                 button_text_size = 28, button_text_color = (255, 255, 255), text_file = 'Media/Font/Kollektif.ttf',
                 list_menu=None, command = None):
        self.linked_list = list_menu
        self.surface = surface
        self.command = command
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

    def place(self, events=None):
        global Mouse_x
        global Mouse_y
        global event
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        if type(self.linked_list) == List_menu:
            if events != None:
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            mouse_x, mouse_y = event.pos
                            if self.collide(mouse_x, mouse_y):
                                if self.linked_list.list_state:
                                    self.linked_list.list_state = False
                                else:
                                    self.linked_list.list_state = True
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


class List_menu:
    def __init__(self, surface, x, y, bg_image, selector, hover_selector = None, buttons = [], button_distance = 5,
                 top_padding = 5, text_size = 14, text_color = colors_rb.white, hover_text_color = colors_rb.white,
                 text_file = 'Media/Font/Raleway-Medium.ttf'):
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
        self.button_actions = buttons
        self.top_padding = top_padding
        self.button_distance = button_distance
        self.list_width = self.background.get_width()
        self.list_height = self.background.get_height()
        self.buttons_y = self.y+self.top_padding
        self.buttons_x = (self.x + self.list_width/2) - (self.selector.get_width()/2)
        self.buttons_end_y = self.buttons_y
        start_point_y = self.buttons_y
        step_value = self.selector.get_height()+self.button_distance
        for button_dict in buttons:
            self.buttons_end_y = start_point_y+self.selector.get_height()
            self.buttons.append(Button(self.surface, self.selector, self.hover_selector, self.buttons_x, start_point_y,
                                       button_text=button_dict['name'], button_text_size=text_size, button_text_color=text_color,
                                       text_file=text_file, command=button_dict['command'] if 'command' in button_dict else None))
            start_point_y += step_value
            if start_point_y+self.top_padding >= (self.y + self.list_height):
                break

        self.list_state = False
        if self.list_height - (self.buttons_end_y - self.y) > self.top_padding:
            #crop_Image('Media/Image/List_menu/background.png', 'Media/Image/List_menu/temp_background.png', 0, 0, self.list_width, self.buttons_end_y - self.y+self.top_padding)
            self.background = pygame.transform.scale(bg_image, (self.selector.get_width()+10, self.buttons_end_y - self.y+self.top_padding)).convert_alpha()
            #self.background = pygame.image.load('Media/Image/List_menu/temp_background.png')

    def place(self, events=None):
        if self.list_state:
            self.surface.blit(self.background, [self.x, self.y])
            for button in self.buttons:
                button.place()
            if events != None:
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            mouse_x, mouse_y = event.pos
                            for button in self.buttons:
                                if button.command != None and button.collide(mouse_x, mouse_y):
                                    button.command()


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


file_menu = List_menu(Game_Window, 20, 53, List_menu_background, List_menu_selector, hover_selector,
                      [{'name': 'Store', 'command': lambda a=0: open_url('https://www.instamojo.com/Brightgoal')},
                       {'name': 'Brightgoal', 'command': lambda a=0: open_url('https://www.brightgoal.in/')},
                       {'name': 'Twitter', 'command': lambda a=0: open_url('https://twitter.com/brightgoal_in')},
                       {'name': 'Facebook', 'command': lambda  a=0: open_url('https://www.facebook.com/brightgoal.in.Education')},
                       {'name': 'Instagram', 'command': lambda a=0: open_url('https://www.instagram.com/brightgoal.in/')},
                       {'name': 'Facebook Self', 'command': lambda a=0: open_url('https://www.facebook.com/harvindar.brightgoal')},
                       {'name': 'YouTube', 'command': lambda a=0: open_url('https://www.youtube.com/channel/UCCEBsUxSW7PyyCYLw8cyhvA')},
                       {'name': 'Close game', 'command': lambda a=0: exit(0)}])

menu_button = Button(Game_Window, 'Media/Image/Icon/menu blue.png', 'Media/Image/Icon/menu white.png', 20, 20, list_menu=file_menu)

event_list = []
while True:
    for event in pygame.event.get():
        event_list.append(event)
        if event.type == pygame.QUIT:
            exit(0)

    Game_Window.blit(main_background, [0, 0])
    menu_button.place(event_list)
    file_menu.place(event_list)
    event_list = []
    pygame.display.update()
