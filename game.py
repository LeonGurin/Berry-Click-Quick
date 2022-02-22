from tkinter.tix import MAIN
import pygame
import random
import os
import sys
import time

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,    
    RLEACCEL,
)

pygame.init()

# fixed python 32-bit bug 
# add score bar and timer
# add sound
# add game over
# add high score
# add pause

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 30

# init screen and clock
pygame.display.set_caption('Clicky Bicky Game')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
clock.tick(FPS)

# init background
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.dirname(__file__) + "\\sky2.jpg").convert()
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.y2 = self.rect.height

    def update(self):
        self.y -= 0.05
        self.y2 -= 0.05
        if self.y <= -self.rect.height:
            self.y = self.rect.height
        if self.y2 <= -self.rect.height:
            self.y2 = self.rect.height

    def render(self):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.image, (self.x, self.y2))

# init text
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Clicky Bicky Game', True, (0,255,0), (0,0,255))
textRect = text.get_rect()
textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200)

# fruit object
class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super(Fruit, self).__init__()
        self.surf = pygame.image.load(os.path.dirname(__file__) + "\\Strawberry.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.posX = SCREEN_WIDTH / 2
        self.posY = SCREEN_HEIGHT / 2

    def is_clicked(self,x,y):
        if x > self.posX and x < self.posX + self.rect.width:
            if y > self.posY and y < self.posY + self.rect.height:
                # self.surf.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                self.posX = random.randint(0, SCREEN_WIDTH - self.rect.width)
                self.posY = random.randint(100, SCREEN_HEIGHT - self.rect.height)
        
# init objects
bg = Background()
fruit = Fruit()

# game loop
running = True
while running:    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    #print(pygame.mouse.get_pos())

    #if the mouse is clicked
    if event.type == MOUSEBUTTONDOWN:
        (x,y) = pygame.mouse.get_pos()
        fruit.is_clicked(x,y)
    
    bg.render()
    bg.update()
    screen.blit(text, textRect)
    screen.blit(fruit.surf, (fruit.posX, fruit.posY))
    pygame.display.flip()
    

pygame.quit()
sys.exit()
