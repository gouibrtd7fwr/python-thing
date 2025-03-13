import pygame

# colors/palette
blue = (106, 128, 185)
orange = (246, 199, 148)
yellow = (255, 246, 179)
black = (0,0,0)
green = (183, 255, 203)
red = (255, 100, 100)

enemy_assets = ['assets/enemy_lvl_1.png','assets/enemy_lvl_2.png','assets/enemy_lvl_3.png','assets/enemy_lvl_4.png','assets/enemy_lvl_5.png','assets/enemy_lvl_6.png','assets/enemy_lvl_7.png','assets/enemy_lvl_8.png']
level_dicts = [
    {
        'level': 1,
        'proportion': [100,0,0,0,0,0,0,0]
    },
    {
        'level': 2,
        'proportion': [40,50,10,0,0,0,0,0]
    },
    {
        'level': 3,
        'proportion': [25,35,35,5,0,0,0,0]
    },
    {
        'level': 4,
        'proportion': [5,20,30,35,7,3,0,0]
    },
    {
        'level': 5,
        'proportion': [0,10,15,20,35,8,2,0]
    },
    {
        'level': 6,
        'proportion': [0,2,5,10,25,40,10,8]
    },
    {
        'level': 7,
        'proportion': [0,0,1,4,10,15,50,25]
    },
    {
        'level': 8,
        'proportion': [0,0,0,0,2,8,15,75]
    },
]
# initialize
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((500,500))
window.fill(yellow)
running = True

# variables
fps = 60
count = 9
rows = 2

platform_x = 220
platform_y = 400

ball_x = 3
ball_y = 3

m_x = 5
m_y = 5

number = 0
# bool values
move_up = False
move_down = False
move_right = False
move_left = False

# others
monsters = []

# classes
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = yellow
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(window,self.fill_color,self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def colliderect(self, rect):
        return self.rect.collidepoint()
class Image(Area):
    def __init__(self, file_name, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(file_name)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Label(Area):
    def set_text(self,text,fsize=14,text_color=(0,0,0)):
        self.image = pygame.font.SysFont('Verdana', fsize).render(text, True, text_color)

    def draw(self,shift_x=0,shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

class Enemy(Image):
    def __init__(self, enemy_assets, x=0, y=0, width=10, height=10, level=0):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(enemy_assets[level])
        self.level = level
        self.level_cap = len(enemy_assets) - 1

    def hit_or_delete(self):
        if self.level == 0:
            return False
        else:
            self.level -= 1
            self.image = pygame.image.load(enemy_assets[self.level])
            return True

# monster function
for i in range(rows):
    y = m_y + (55*i)
    x = m_x + (27.5*i)
    for j in range(count):
        monster = Enemy(enemy_assets, x, y, 50, 50, 2)
        monsters.append(monster)
        x += 55
    count -= 1
# waiting screen
def waiting_screen():
    window.fill(blue)
    # loop
    waiting = True
    name = Label(50,100,400,50,green)
    name.set_text('Welcome to Arkanoid!', 35, black)
    name.draw(10, 10)

    how_to = Label(50,175,300,100,blue)
    how_to.set_text('Kill all the monsters!', 25, black)
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

def waiting_level(level, time_allowed):
    window.fill(yellow)
    waiting = True
    levels = Label(50,100,400,50,green)
    levels.set_text('You are in Level ' + str(level), 35, black)
    levels.draw(10, 10)

    info = Label(50,200,400,50,green)
    info.set_text('Time: '+ str(time_allowed),20,black)
    info.draw(10,10)

    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False
                window.fill(yellow)
        pygame.display.update()
        clock.tick(fps)

# runs waiting screen
waiting_screen()
window.fill(yellow)
running = True

for level in range(len(level_dicts)):
    # images/assets
    ball = Image('assets/ball.png', 200, 200, 50, 50)
    platform = Image('assets/platform.png', platform_x, platform_y, 60, 10)

    # main loop
    while running:
        window.fill(yellow)
        ball.fill()
        platform.fill()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    move_left = True
                if event.key == pygame.K_d:
                    move_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    move_left = False
                if event.key == pygame.K_d:
                    move_right = False
        # movement of the platform
        if move_left:
            platform.rect.x -= 5
        if move_right:
            platform.rect.x += 5

        # border
        if platform.rect.x > 400:
            platform.rect.x = 400
        if platform.rect.x < 0:
            platform.rect.x = 0
        
        # ball moving
        ball.rect.x += ball_x
        ball.rect.y += ball_y

        # ball bounce
        if ball.rect.y < 0:
            ball_y *= -1
        if ball.rect.x <= 0:
            ball_x *= -1
            ball.rect.x += 2
        if ball.rect.x >= 450:
            ball_x *= -1
            ball.rect.x -= 2
        if ball.rect.colliderect(platform.rect):
            ball_y *= -1
            ball.rect.x -= 3
            
        for m in monsters:
            m.draw()
            if m.rect.colliderect(ball.rect):
                if not m.hit_or_delete():
                    monsters.remove(m)
                m.fill()
                ball_y *= -1
                number += 1
        
        if ball.rect.y > 450:
            lose = Label(0,0,500,500,red)
            lose.set_text('YOU LOST!', 30, black)
            lose.draw(150,150)
            run = False

        if len(monsters) == 0:
            win = Label(0,0,500,500,green)
            win.set_text('You win!', 30, black)
            win.draw(150, 150)
            run = False

        ball.draw()
        platform.draw()
        pygame.display.update()
        clock.tick(fps)