import pygame
import random

pygame.init()

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

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
#set game tic rate
FPS = 30

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pic = pygame.image.load("background.jpg")

pygame.display.set_caption('Clicky Bicky Game')
clock = pygame.time.Clock()
clock.tick(FPS)

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Clicky Bicky Game', True, (0,255,0), (0,0,255))
textRect = text.get_rect()
textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200)

# fruit object
class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super(Fruit, self).__init__()
        self.surf = pygame.image.load("Strawberry.png").convert()
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
                self.posY = random.randint(60, SCREEN_HEIGHT - self.rect.height)
        

fruit = Fruit()

running = True
while running:    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    print(pygame.mouse.get_pos())

    #if the mouse is clicked
    if event.type == MOUSEBUTTONDOWN:
        (x,y) = pygame.mouse.get_pos()
        fruit.is_clicked(x,y)
    
    screen.blit(pygame.transform.scale(pic, (1000, 500)), (0, 0))
    screen.blit(text, textRect)
    screen.blit(fruit.surf, (fruit.posX, fruit.posY))
    pygame.display.flip()
    

pygame.quit()
