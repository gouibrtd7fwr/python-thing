import pygame
from random import *

# colors/palette
navy = (42, 0, 78)
red = (198, 35, 0)
orange = (241, 74, 0)

# initialize
clock = pygame.time.Clock()
pygame.init()
window = pygame.display.set_mode((500,500))
window.fill(navy)
running = True

# questions and answers
questions = ['Who was the 192th president of the United States?', 'What year is it?', 'What is the name of this programming language?']
answers = ['Nobody, since there are less then 192 presidents!', 'It is 45^2 right now.', 'Obviously not not Python.']

# font
main_font = pygame.font.Font(None, 70)

# shaping class
class TextArea():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = color
    def set_text(self,text,fsize=14,text_color=orange):
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(text, True, text_color)
    def draw(self,shift_x=0,shift_y=0):
        pygame.draw.rect(window,self.fill_color,self.rect)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

# drawing
question = TextArea(100,50,300,100,red)
answer = TextArea(100,350,300,100,red)
question.set_text('Question', 70, orange)
answer.set_text('Answer', 70, orange)
question.draw(25, 15)
answer.draw(25, 15)

while running:
    # x button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                rand_number_ques = randint(0, (len(questions) - 1))
                selected_question = questions[rand_number_ques]
                question.set_text(selected_question, 45, orange)
                question.draw(25, 15)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                rand_number_ans = randint(0, (len(answers) - 1))
                selected_answer = answers[rand_number_ans]
                answer.set_text(selected_answer, 45, orange)
                answer.draw(25, 15)
    pygame.display.update()
    clock.tick(40)
pygame.quit()