import pygame
from time import *
from random import *

# colors/palette
blue = (21, 94, 149)
cyan = (106, 128, 185)
orange = (246, 199, 148)
yellow = (255, 246, 179)
black = (0,0,0)

# initialize
clock = pygame.time.Clock()
pygame.init()
window = pygame.display.set_mode((500,500))
window.fill(yellow)
running = True

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
class Label(Area):
    def set_text(self,text,fsize=14,text_color=(0,0,0)):
        self.image = pygame.font.SysFont('Verdana', fsize).render(text, True, text_color)
    def draw(self,shift_x=0,shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

# cards
cards = []
num_cards = 4
x = 50

for i in range(num_cards):
    new_card = Label(x, 170, 70, 100, cyan)
    new_card.set_text('CLICK', 24, black)
    new_card.outline(orange, 10)
    cards.append(new_card)
    x = x + 100

while running:
    # x button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for card in cards:
        card.draw(10, 30)
    pygame.display.update()
    clock.tick(40)
pygame.quit()