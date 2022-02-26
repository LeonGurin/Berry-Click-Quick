from turtle import update
import pygame
import random
import os
import sys
import time

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,    
    RLEACCEL,
)

pygame.init()

# fixed python 32-bit bug ✔
# add start screen ✔
# fix berry bug ✔
# add score bar and timer ✔
# add sound
# add game over
# add high score
# add pause

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 60

# init screen and clock
pygame.display.set_caption('Clicky Bicky Game')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

berries = pygame.sprite.Group()

# init background
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.dirname(__file__) + "\\backgroundClouds.png").convert()
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.y2 = self.rect.height
    def update(self):
        self.y -= 2
        self.y2 -= 2
        if self.y <= -self.rect.height:
            self.y = self.rect.height
        if self.y2 <= -self.rect.height:
            self.y2 = self.rect.height
    def render(self):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.image, (self.x, self.y2))

# create a start button
class StartButton(pygame.sprite.Sprite):
    def __init__(self):
        super(StartButton, self).__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\start-frame-0.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\start-frame-1.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\start-frame-2.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\start-frame-3.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\start-frame-4.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\start-frame-5.png").convert_alpha())
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH-100, SCREEN_HEIGHT-100))
        # self.image = pygame.Surface((100, 100))
        self.rect = self.image.get_rect()
        self.posX = SCREEN_WIDTH / 2 - self.rect.width / 2
        self.posY = SCREEN_HEIGHT / 2 - self.rect.height / 2 + 30
        self.is_animating = True

        self.h1 = 75
        self.w1 = 200

    def is_clicked(self,x,y):
        if x > self.posX and x < self.posX + self.rect.width:
            if y > self.posY and y < self.posY + self.rect.height:
                return True
        return False

    def hover(self,x,y):
        if x > self.posX+100 and x < self.posX + 300:
            if y > self.posY+150 and y < self.posY + 225:
                self.is_animating = False
                self.current_sprite = 0
                self.image = pygame.image.load(os.path.dirname(__file__) + "\\startButtonPressed.png").convert_alpha()
                self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH-100, SCREEN_HEIGHT-100))
            self.rect = self.image.get_rect()
        else:
            self.is_animating = True

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.1
            
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            
            self.image = self.sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH-100, SCREEN_HEIGHT-100))
            self.rect = self.image.get_rect()

    def render(self):
        screen.blit(self.image, (self.posX, self.posY))
        #draw a border around the button
        # pygame.draw.rect(screen, (0,0,0), (self.posX+100, self.posY+150, self.w1, self.h1), 2)

class QuitButton(pygame.sprite.Sprite):
    def __init__(self):
        super(QuitButton, self).__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\quit-frame-0.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\quit-frame-1.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\quit-frame-2.png").convert_alpha())
        # self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\quit-frame-3.png").convert_alpha())
        # self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\quit-frame-4.png").convert_alpha())
        # self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\quit-frame-5.png").convert_alpha())
        # self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\quit-frame-6.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\quit-frame-7.png").convert_alpha())
        # self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\quit-frame-8.png").convert_alpha())
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH-200, SCREEN_HEIGHT-200))
        # self.image = pygame.Surface((100, 100))
        self.rect = self.image.get_rect()
        self.posX = SCREEN_WIDTH / 2 - self.rect.width / 2 + 100
        self.posY = SCREEN_HEIGHT / 2 - self.rect.height / 2
        self.is_animating = True

        self.h1 = 75
        self.w1 = 200

    def is_clicked(self,x,y):
        if x > self.posX+100 and x < self.posX + 250:
            if y > self.posY+150+175 and y < self.posY + 225+200:
                return True
        return False

    def hover(self,x,y):
        if x > self.posX+100 and x < self.posX + 250:
            if y > self.posY+150+175 and y < self.posY + 225+200:
                self.is_animating = False
                self.current_sprite = 0
            self.image = pygame.image.load(os.path.dirname(__file__) + "\\quitButtonClicked.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH-100, SCREEN_HEIGHT-100))
            self.rect = self.image.get_rect()
        else:
            self.is_animating = True

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.05
            
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            
            self.image = self.sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH-100, SCREEN_HEIGHT-100))
            self.rect = self.image.get_rect()

    def render(self):
        screen.blit(self.image, (self.posX, self.posY))
        #draw a border around the button
        pygame.draw.rect(screen, (0,0,0), (self.posX+100, self.posY+150+175, self.w1, self.h1), 2)

class Title(pygame.sprite.Sprite):
    def __init__(self):
        super(Title, self).__init__()
        self.image = pygame.image.load(os.path.dirname(__file__) + "\\gameT.png").convert_alpha()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect()
        self.posX = SCREEN_WIDTH / 2 - self.rect.width / 2
        self.posY = SCREEN_HEIGHT / 2 - self.rect.height / 2 - 75
    def render(self):
        screen.blit(self.image, (self.posX, self.posY))

class UI(pygame.sprite.Sprite):
    def __init__(self):
        super(UI, self).__init__()
        self.surf = pygame.image.load(os.path.dirname(__file__) + "\\ui.png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (SCREEN_WIDTH+36, 600))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
    
    def render(self):
        screen.blit(self.surf, (-15, 0))

class UI_menuButton(pygame.sprite.Sprite):
    def __init__(self):
        super(UI_menuButton, self).__init__()
        # self.image = pygame.image.load(os.path.dirname(__file__) + "\\uiMenu.png").convert_alpha()
        # self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH+36, 600))
        # self.rect = self.image.get_rect()
        self.posX = 338 + 80
        self.posY = 18
        self.h1 = 78
        self.w1 = 78

    def is_clicked(self,x,y):
        if x > self.posX and x < self.posX + self.w1:
            if y > self.posY and y < self.posY + self.h1:
                return True
        return False

    def hover(self,x,y):
        if x > self.posX and x < self.posX + self.w1:
            if y > self.posY and y < self.posY + self.h1:
                self.image = pygame.image.load(os.path.dirname(__file__) + "\\uiMenu.png").convert_alpha()
                self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH+36, 600))
                screen.blit(self.image, (-15, 0))

    # def render(self):
    #     #draw a border around the button
    #     pygame.draw.rect(screen, (0,0,0), (self.posX, self.posY, self.w1, self.h1), 2)

class UI_closeButton(pygame.sprite.Sprite):
    def __init__(self):
        super(UI_closeButton, self).__init__()
        # self.image = pygame.image.load(os.path.dirname(__file__) + "\\uiMenu.png").convert_alpha()
        # self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH+36, 600))
        # self.rect = self.image.get_rect()
        self.posX = 338
        self.posY = 18
        self.h1 = 78
        self.w1 = 78

    def is_clicked(self,x,y):
        if x > self.posX and x < self.posX + self.w1:
            if y > self.posY and y < self.posY + self.h1:
                return True
        return False

    def hover(self,x,y):
        if x > self.posX and x < self.posX + self.w1:
            if y > self.posY and y < self.posY + self.h1:
                self.image = pygame.image.load(os.path.dirname(__file__) + "\\uiClose.png").convert_alpha()
                self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH+36, 600))
                screen.blit(self.image, (-15, 0))

    # def render(self):
    #     #draw a border around the button
    #     pygame.draw.rect(screen, (0,0,0), (self.posX, self.posY, self.w1, self.h1), 2)

class ClockText:
    def __init__(self):
        self.font = pygame.font.Font(os.path.dirname(__file__) + "\\Quinquefive.ttf", 34)
        self.current_time = time.time()
        self.s = 10
        self.m = 0
        self.color = (3, 169, 244)
        self.text = self.font.render("0:10", True, self.color)
        # self.text = self.font.render(str(self.m) + ':' + str(self.s), True, (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT // 2 - 195)
    def update(self):
        if time.time() - self.current_time >= 1:
            self.current_time = time.time()
            self.s -= 1
        self.text = self.font.render(str(self.m) + ':' + str(self.s), True, self.color)

    def render(self):
        if self.s < 10:
            self.text = self.font.render(str(self.m) + ':0' + str(self.s), True, self.color)
        else:
            self.text = self.font.render(str(self.m) + ':' + str(self.s), True, self.color)
        screen.blit(self.text, self.rect)

# fruit object
class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super(Fruit, self).__init__()
        self.transform_factor = 100
        self.sprites = []
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\berry-frame-0.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\berry-frame-1.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\berry-frame-2.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\berry-frame-3.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\berry-frame-4.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\berry-frame-5.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\berry-frame-6.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\berry-frame-7.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\berry-frame-8.png").convert_alpha())
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (self.transform_factor, self.transform_factor))
        self.rect = self.image.get_rect()
        self.posX = SCREEN_WIDTH / 2 - self.rect.width / 2
        self.posY = SCREEN_HEIGHT / 2 - self.rect.height / 2
        self.tempX = self.posX
        self.tempY = self.posY
        self.click_status = False
        self.is_animating = False
    def is_clicked(self,x,y):
        if self.posX < x < self.posX + self.rect.width:
            if self.posY < y < self.posY + self.rect.height:
                self.click_status = True
                self.animate()
            else:
                if self.click_status == True:
                    self.click_status = False
    
    def change_pos(self):
        while self.tempX >= self.posX and self.tempX <= self.posX + self.rect.width:
            self.tempX = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.tempY = random.randint(150, SCREEN_HEIGHT - self.rect.height)
        self.posX = self.tempX
        self.posY = self.tempY

    def animate(self):
        self.is_animating = True 

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.5
            
            if self.current_sprite == len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
                self.change_pos()
                self.image = self.sprites[int(self.current_sprite)]
                self.image = pygame.transform.scale(self.image, (self.transform_factor, self.transform_factor))
                self.rect = self.image.get_rect()
                return True
            
            self.image = self.sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image, (self.transform_factor, self.transform_factor))
            self.rect = self.image.get_rect()
        return False

    def scale(self):
        if self.transform_factor >= 50:
            self.transform_factor -= 15
            self.image = pygame.transform.scale(self.image, (self.transform_factor, self.transform_factor))
            self.rect = self.image.get_rect()
        else:
            self.kill()
    def render(self):
        #draw a border around the fruit
        pygame.draw.rect(screen, (255, 255, 255), (self.posX, self.posY, self.rect.width, self.rect.height), 1)
        screen.blit(self.image, (self.posX, self.posY))

class Score:
    def __init__(self):
        self.font = pygame.font.Font(os.path.dirname(__file__) + "\\Quinquefive.ttf", 34)
        self.cur_time = time.time()
        self.color = (0, 0, 0)
        self.text = self.font.render("0", True, self.color)
        self.counter = 0
        self.rect = self.text.get_rect()
        self.rect.center = (SCREEN_WIDTH//2 - 121, SCREEN_HEIGHT // 2 - 195)
    def update(self):
        if self.counter == 5:
            self.counter = 0
        else:
            self.counter += 1
    def render(self):
        self.text = self.font.render(str(self.counter), True, self.color)
        screen.blit(self.text, self.rect)

#-------------------#
#  code starts here
#-------------------#

# init objects
bg = Background()
st = StartButton()
qt = QuitButton()
tt = Title()

startGame = False
running = True

#delay
pygame.time.delay(100)

(x,y) = pygame.mouse.get_pos()
# start menu
while startGame == False:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    (x,y) = pygame.mouse.get_pos()
    if qt.is_clicked(x,y) and event.type == MOUSEBUTTONDOWN:
        print("ended")
        running = False    
    if event.type == MOUSEBUTTONDOWN:
        startGame = st.is_clicked(x,y)
    bg.render()
    bg.update()
    tt.render()
    st.hover(x,y)
    st.update()
    st.render()
    qt.hover(x,y)
    qt.update()
    qt.render()
    pygame.display.update()
    clock.tick(FPS)

# delay
time.sleep(.1)
# game loop
fr = Fruit()
cl = ClockText()
ui = UI()
uim = UI_menuButton()
uic = UI_closeButton()
sc = Score()


berries.add(fr)

ADDBERRY = pygame.USEREVENT + 1
event_time = 3000
pygame.time.set_timer(ADDBERRY, event_time)

while running:    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == ADDBERRY:
            new_fr = Fruit()
            berries.add(new_fr)
            if event_time >= 1000:
                event_time = event_time - 100
                pygame.time.set_timer(ADDBERRY, event_time)
            #print(event_time)

    (x,y) = pygame.mouse.get_pos()
    
    if uic.is_clicked(x,y) and event.type == MOUSEBUTTONDOWN:
        print("ended")
        running = False

    #if the mouse is clicked
    for fruit in berries:
        if event.type == MOUSEBUTTONDOWN:
            fruit.is_clicked(x,y)
            print(len(berries))

    bg.update()
    bg.render()

    for fruit in berries:
        if fruit.update() == True:
            sc.update()
            if sc.counter == 0:
                fruit.scale()
                berries.remove(fruit)
                del fruit
    for fruit in berries:
        fruit.render()
    
    ui.render()
    uim.hover(x,y)
    uic.hover(x,y)
    cl.update()
    cl.render()
    
    sc.render()
    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()
sys.exit()
