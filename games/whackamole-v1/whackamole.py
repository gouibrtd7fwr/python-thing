import pygame
from time import *
from random import *
from math import *

# colors/palette
blue = (106, 128, 185)
orange = (246, 199, 148)
yellow = (255, 246, 179)
black = (0,0,0)
green = (183, 255, 203)
red = (255, 100, 100)

# initialize
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((1000,1000))
window.fill(yellow)
running = True

# variables
interval = 1
losing_point = -5
all_time = 20

# font
main_font = pygame.font.Font(None, 70)

# shaping class
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(window,self.fill_color,self.rect)
    def outline(self, frame_color, thickness):
        pygame.draw.rect(window,frame_color,self.rect,thickness)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
class Label(Area):
    def set_text(self,text,fsize=14,text_color=(0,0,0)):
        self.image = pygame.font.SysFont('Verdana', fsize).render(text, True, text_color)
    def draw(self,shift_x=0,shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

# waiting screen (func)
def waiting_screen():
    window.fill(blue)
    # loop
    waiting = True
    name = Label(50,100,400,50,green)
    name.set_text('Welcome to Whack-a-mole Levels!', 35, black)
    name.draw(10, 10)

    how_to = Label(50,175,300,100,blue)
    how_to.set_text('Click when the tiles say CLICK! Reach 10 points!', 25, black)
    how_to.draw(10, 10)

    space = Label(50,300,400,50,green)
    space.set_text('Click SPACE to begin!', 25, black)
    space.draw(100, 15)

    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False
                window.fill(yellow)
        pygame.display.update()
        clock.tick(40)

def waiting_level(level, time_allowed, points_need):
    window.fill(yellow)
    waiting = True
    levels = Label(50,100,400,50,green)
    levels.set_text('You are in Level ' + str(level), 35, black)
    levels.draw(10, 10)

    info = Label(50,200,400,50,green)
    info.set_text('Time: '+ str(time_allowed) +'. Points: '+ str(points_need) +'.',20,black)
    info.draw(10,10)

    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False
                window.fill(yellow)
        pygame.display.update()
        clock.tick(40)
# runs waiting screen
waiting_screen()
window.fill(yellow)
# variables 2: electric boogaloo
level_num = 100
num_cards = 4
points_need = 10
level = 1

for i in range(level_num):
    start_time = time()
    cur_time = time()
    cards = []
    x = 50

    for i in range(num_cards):
        new_card = Label(x, 170, 70, 100, blue)
        new_card.set_text('CLICK', 26, black)
        new_card.outline(orange, 10)
        cards.append(new_card)
        x = x + 100

    points = 0
    point_label = Label(10, 10, 120, 30, orange)
    point_label.set_text('Points: ' + str(points), 20)
    point_label.draw(10, 10)

    time_left = 0
    timer_label = Label(10, 50, 150, 30, orange)
    timer_label.set_text('Time left: ' + str(time_left), 20)
    timer_label.draw(10, 10)

    level_label = Label(370, 10, 120, 30, orange)
    level_label.set_text('Level: ' + str(level), 20)
    level_label.draw(10, 10)

    passed_time = 0
    fps = 40
    mole = -1

    lost = False
    running = True
    # main loop
    while running:
        new_time = time()
        # calc time
        if int(new_time) - int(cur_time) >= interval:
            timer_label.set_text('Time left: ' + str(all_time - int(new_time - start_time)), 20, black)
            timer_label.draw(10, 10)
            cur_time = new_time
        passed_time = passed_time + 1/fps
        if passed_time >= interval:
            passed_time = 0
            mole = randint(0, num_cards-1)
            for i in range(num_cards):
                cards[i].color(blue)
                if i == mole:
                    cards[i].draw(10, 30)
                else:
                    cards[i].color(blue)
                    cards[i].fill()
        else:
            # x button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    for i in range(num_cards):
                        if cards[i].collidepoint(x,y):
                            if i == mole:
                                cards[i].color(green)
                                points += 1
                            else:
                                cards[i].color(red)
                                points -= 1
                            cards[i].fill()
                            point_label.set_text('Points: ' + str(points), 20, black)
                            point_label.draw(10, 10)

        if new_time - start_time >= all_time:
            time_left = new_time - start_time
            win = Label(0,0,500,500,blue)
            win.set_text('TIMES UP!!!\n' + 'Total score: ' + str(points), 35, red)
            win.draw(110,100)
            running = False

        if points >= points_need:
            time_left = new_time - start_time
            win = Label(0,0,500,500,green)
            win.set_text('YOU WON!\n' + 'Completed in: ' + str(int((all_time - time_left))) + 's', 35, orange)
            win.draw(110, 100)
            running = False
        
        if points <= losing_point:
            time_left = new_time - start_time
            win = Label(0,0,500,500,red)
            win.set_text('YOU LOST!\n' + 'Lost in: ' + str(int((all_time - time_left))) + 's', 35, blue)
            win.draw(110, 100)
            running = False
            lost = True

        pygame.display.update()
        clock.tick(fps)
    pygame.display.update()
    sleep(3)

    all_time = int(20*sqrt(level))
    points_need = int(10*sqrt(level)*1.2)
    interval = float(interval*(level**-0.3))
    level += 1

    if lost == True:
        break
    waiting_level(level, all_time, points_need)
pygame.quit()