import pygame
import random
import os
import sys
import time
from pygame.locals import (
    QUIT,
    MOUSEBUTTONDOWN,    
    RLEACCEL,
)
# fixed python 32-bit bug ✔
# add start screen ✔
# fix berry bug ✔
# add score bar and timer ✔
# add sound ✔
# add game over ✔
# add high score ✔
# add pause ✔

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 90
MAX_BERRIES = 8

# init screen and clock
pygame.display.set_caption('Clicky Bicky Game')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

berries = pygame.sprite.Group()

# init background
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.dirname(__file__) + '\\background\\backgroundClouds.png').convert()
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.y2 = self.rect.height+1
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
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\startFrames\\start-frame-0.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\startFrames\\start-frame-1.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\startFrames\\start-frame-2.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\startFrames\\start-frame-3.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\startFrames\\start-frame-4.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\startFrames\\start-frame-5.png").convert_alpha())
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
                pygame.mixer.Sound(os.path.dirname(__file__) + "\\sounds\\startBlip.wav").play()
                return True
        return False

    def hover(self,x,y):
        if x > self.posX+100 and x < self.posX + 300:
            if y > self.posY+150 and y < self.posY + 225:
                self.is_animating = False
                self.current_sprite = 0
                self.image = pygame.image.load(os.path.dirname(__file__) + "\\pressed\\startButtonPressed.png").convert_alpha()
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
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\quitFrames\\quit-frame-0.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\quitFrames\\quit-frame-1.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\quitFrames\\quit-frame-2.png").convert_alpha())
        # self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\quitFrames\\quit-frame-3.png").convert_alpha())
        # self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\quitFrames\\quit-frame-4.png").convert_alpha())
        # self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\quitFrames\\quit-frame-5.png").convert_alpha())
        # self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\quitFrames\\quit-frame-6.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\quitFrames\\quit-frame-7.png").convert_alpha())
        # self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\quitFrames\\quit-frame-8.png").convert_alpha())
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
            self.image = pygame.image.load(os.path.dirname(__file__) + "\\pressed\\quitButtonClicked.png").convert_alpha()
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
        # pygame.draw.rect(screen, (0,0,0), (self.posX+100, self.posY+150+175, self.w1, self.h1), 2)

class Title(pygame.sprite.Sprite):
    def __init__(self):
        super(Title, self).__init__()
        self.image = pygame.image.load(os.path.dirname(__file__) + "\\title\\gameT.png").convert_alpha()
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
        self.surf = pygame.image.load(os.path.dirname(__file__) + "\\ui\\uiBar.png").convert_alpha()
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
                self.image = pygame.image.load(os.path.dirname(__file__) + "\\ui\\uiMenu.png").convert_alpha()
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
                self.image = pygame.image.load(os.path.dirname(__file__) + "\\ui\\uiClose.png").convert_alpha()
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
        
        self.vel = 1
        self.acc = 1.05

        self.color = (3, 169, 244)
        self.text = self.font.render("0:10", True, self.color)
        # self.text = self.font.render(str(self.m) + ':' + str(self.s), True, (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT // 2 - 195)
    
    def resetClock(self):
        self.current_time = time.time()
        self.s = 10
        self.m = 0
        self.vel = 1
        self.acc = 1.05
        self.text = self.font.render("0:10", True, self.color)

    def gameOver(self):
        if self.s <= 0:
            return True
        return False

    def addTime(self):
        self.s += 1
    
    def update(self):
        if time.time() - self.current_time >= 1:
            self.current_time = time.time()
            self.vel = -(self.vel * (-self.acc))
            self.s = self.s - self.vel
            #print(self.s)
            self.s = round(self.s)
        # self.text = self.font.render(str(int(self.m)) + ':' + str(self.s), True, self.color)

    def render(self):
        if self.s < 10:
            self.text = self.font.render(str(self.m) + ':0' + str(int(self.s)), True, self.color)
        else:
            self.text = self.font.render(str(self.m) + ':' + str(int(self.s)), True, self.color)
        screen.blit(self.text, self.rect)

# fruit object
class Fruit(pygame.sprite.Sprite):
    def __init__(self, tf = None, x = None, y = None):
        super(Fruit, self).__init__()
        if tf == None:
            self.transform_factor = random.randint(50,100)
        else:
            self.transform_factor = tf
        if x == None:
            self.posX = random.randint(self.transform_factor + 200, SCREEN_WIDTH - self.transform_factor)
        else:
            self.posX = x
        if y == None:
            self.posY = random.randint(self.transform_factor + 200, SCREEN_HEIGHT - self.transform_factor)
        else:
            self.posY = y
        
        self.sprites = []
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\berryFrames\\berry-frame-0.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\berryFrames\\berry-frame-1.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\berryFrames\\berry-frame-2.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\berryFrames\\berry-frame-3.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\berryFrames\\berry-frame-4.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\berryFrames\\berry-frame-5.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\berryFrames\\berry-frame-6.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\berryFrames\\berry-frame-7.png").convert_alpha())
        self.sprites.append(pygame.image.load(os.path.dirname(__file__) + "\\berryFrames\\berry-frame-8.png").convert_alpha())
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (self.transform_factor, self.transform_factor))
        self.rect = self.image.get_rect()
        self.tempX = self.posX
        self.tempY = self.posY
        self.click_status = False
        self.is_animating = False

    def is_clicked(self,x,y):
        if self.posX < x < self.posX + self.rect.width:
            if self.posY < y < self.posY + self.rect.height:
                pygame.mixer.Sound(os.path.dirname(__file__) + "\\sounds\\berryClick.wav").play()
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

    # def scale(self):
    #     if self.transform_factor >= 50:
    #         self.transform_factor -= 15
    #         self.image = pygame.transform.scale(self.image, (self.transform_factor, self.transform_factor))
    #         self.rect = self.image.get_rect()
    
    def render(self):
        #draw a border around the fruit
        pygame.draw.rect(screen, (255, 255, 255), (self.posX, self.posY, self.rect.width, self.rect.height), 1)
        screen.blit(self.image, (self.posX, self.posY))

class Score:
    def __init__(self):
        self.font = pygame.font.Font(os.path.dirname(__file__) + "\\Quinquefive.ttf", 24)
        self.cur_time = time.time()
        self.color = (0, 0, 0)
        self.text = self.font.render("0", True, self.color)
        self.counter = 0
        self.scr = 0

        self.rect = self.text.get_rect()
        self.rect.center = (SCREEN_WIDTH//2 - 138, SCREEN_HEIGHT // 2 - 195)
    
    def resetScore(self):
        self.scr = 0
        self.counter = 0

    def displayScore(self):
        self.font = pygame.font.Font(os.path.dirname(__file__) + "\\Quinquefive.ttf", 40)
        self.text = self.font.render(str(self.scr), True, self.color)
        self.rect = self.text.get_rect()
        self.rect.center = (SCREEN_WIDTH/2 + 80, SCREEN_HEIGHT /2 + 9)
        screen.blit(self.text, self.rect)

    def update(self):
        if self.counter == 5:
            self.counter = 0
        else:
            self.counter += 1
        self.scr += 1
    
    def render(self):
        if self.scr < 10:
            self.font = pygame.font.Font(os.path.dirname(__file__) + "\\Quinquefive.ttf", 32)
            self.rect = self.text.get_rect()
            self.rect.center = (SCREEN_WIDTH//2 - 121, SCREEN_HEIGHT // 2 - 195)
            self.text = self.font.render(str(self.scr), True, self.color)
        if self.scr >= 10 and self.scr < 100:
            self.font = pygame.font.Font(os.path.dirname(__file__) + "\\Quinquefive.ttf", 22)
            self.rect = self.text.get_rect()
            self.rect.center = (SCREEN_WIDTH//2 - 126, SCREEN_HEIGHT // 2 - 195)
            self.text = self.font.render(str(self.scr), True, self.color)
        if self.scr >= 100:
            self.font = pygame.font.Font(os.path.dirname(__file__) + "\\Quinquefive.ttf", 16)
            self.rect = self.text.get_rect()
            self.rect.center = (SCREEN_WIDTH//2 - 126, SCREEN_HEIGHT // 2 - 195)
            self.text = self.font.render(str(self.scr), True, self.color)
        screen.blit(self.text, self.rect)

class Menu(pygame.sprite.Sprite):
    def __init__(self, pause_or_gameover):
        super(Menu, self).__init__()
        if pause_or_gameover == "pause":
            self.text = pygame.image.load(os.path.dirname(__file__) + "\\menu\\pausedText.png").convert_alpha()
            self.text_rect = self.text.get_rect()
        elif pause_or_gameover == "gameover":
            self.text = pygame.image.load(os.path.dirname(__file__) + "\\menu\\gameOver.png").convert_alpha()
            self.text_rect = self.text.get_rect()
        
        self.scoreScreen = pygame.image.load(os.path.dirname(__file__) + "\\menu\\scoreScreen.png").convert_alpha()
        self.scoreScreen_rect = self.scoreScreen.get_rect()
        self.retryButton = pygame.image.load(os.path.dirname(__file__) + "\\menu\\retryButton.png").convert_alpha()
        self.retryButton_rect = self.retryButton.get_rect()
        self.quitButton = pygame.image.load(os.path.dirname(__file__) + "\\menu\\exitButton.png").convert_alpha()
        self.quitButton_rect = self.quitButton.get_rect()

        self.quitX = SCREEN_WIDTH / 2 - 45
        self.quitY = SCREEN_HEIGHT / 2 + 165
        self.quit_h = 80
        self.quit_w = 95

        self.retryX = SCREEN_WIDTH / 2 - 45
        self.retryY = SCREEN_HEIGHT / 2 + 80
        self.retry_h = 80
        self.retry_w = 95

    # def is_clicked(self,x,y):
    #     if self.pause_rect.left < x < self.pause_rect.right:
    #         if self.pause_rect.top < y < self.pause_rect.bottom:
    #             self.exit_status = 1
    #             return True
    #     return False
    
    def quitHover(self,x,y):
        if self.quitX < x <  self.quitX + self.quit_w:
            if self.quitY < y < self.quitY + self.quit_h:
                self.quitButton = pygame.image.load(os.path.dirname(__file__) + "\\menu\\exitButtonHover.png").convert_alpha()
                self.quitButton_rect = self.quitButton.get_rect()
        else:
            self.quitButton = pygame.image.load(os.path.dirname(__file__) + "\\menu\\exitButton.png").convert_alpha()
            self.quitButton_rect = self.quitButton.get_rect()
    
    def quitClicked(self,x,y):
        if self.quitX < x < self.quitX + self.quit_w:
            if self.quitY < y < self.quitY + self.quit_h:
                return True
        return False

    def retryHover(self,x,y):
        if self.retryX < x < self.retryX + self.retry_w:
            if self.retryY < y < self.retryY + self.retry_h:
                self.retryButton = pygame.image.load(os.path.dirname(__file__) + "\\menu\\retryButtonHover.png").convert_alpha()
                self.retryButton_rect = self.retryButton.get_rect()
        else:
            self.retryButton = pygame.image.load(os.path.dirname(__file__) + "\\menu\\retryButton.png").convert_alpha()
            self.retryButton_rect = self.retryButton.get_rect()

    def retryClicked(self,x,y):
        if self.retryX < x < self.retryX + self.retry_w:
            if self.retryY < y < self.retryY + self.retry_h:
                return True
        return False

    def render(self):
        # pygame.draw.rect(screen, (255,0,255), (self.quitX, self.quitY, self.quit_w, self.quit_h), 2)
        pygame.draw.rect(screen, (255,0,255), (self.retryX, self.retryY, self.retry_w, self.retry_h), 2)
        screen.blit(self.text, self.text_rect)
        screen.blit(self.scoreScreen, self.scoreScreen_rect)
        screen.blit(self.retryButton, self.retryButton_rect)
        screen.blit(self.quitButton, self.quitButton_rect)

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
running2 = True

#delay
pygame.time.delay(100)

(x,y) = pygame.mouse.get_pos()
# start menu
while startGame == False:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    (x,y) = pygame.mouse.get_pos()
    if qt.is_clicked(x,y) and event.type == MOUSEBUTTONDOWN:
        pygame.mixer.Sound(os.path.dirname(__file__) + "\\sounds\\quitClick.wav").play()
        time.sleep(0.4)
        pygame.quit()
        sys.exit()
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

del st
del qt
del tt

# delay
time.sleep(.1)
# game loop
# fr = Fruit(100, SCREEN_HEIGHT / 2 - 100 / 2, SCREEN_WIDTH / 2 - 100 / 2)
cl = ClockText()
ui_bar = UI()
uim = UI_menuButton()
uic = UI_closeButton()
sc = Score()

# berries.add(fr)

# ADDBERRY = pygame.USEREVENT + 1
# event_time = 3000
# pygame.time.set_timer(ADDBERRY, event_time)

fr = Fruit(100, SCREEN_HEIGHT / 2 - 100 / 2, SCREEN_WIDTH / 2 - 100 / 2)
berries.add(fr)
ADDBERRY = pygame.USEREVENT + 1
event_time = 3000
pygame.time.set_timer(ADDBERRY, event_time)

while running2:
    while running:
        (x,y) = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == ADDBERRY:
                if len(berries) < MAX_BERRIES:
                    new_fr = Fruit()
                    berries.add(new_fr)
                if event_time >= 1000:
                    event_time = event_time - 100
                    pygame.time.set_timer(ADDBERRY, event_time)
                    
            if event.type == MOUSEBUTTONDOWN:
                if uic.is_clicked(x,y):
                    pygame.mixer.Sound(os.path.dirname(__file__) + "\\sounds\\gameOver.wav").play()
                    time.sleep(.3)
                    pygame.quit()
                    sys.exit()
                if uim.is_clicked(x,y):
                    pygame.mixer.Sound(os.path.dirname(__file__) + "\\sounds\\menuClick.wav").play()
                    men = Menu("pause")
                    running = False
                for fruit in berries:
                    fruit.is_clicked(x,y)                        
                    # fruit.scale()
        if cl.gameOver():
            pygame.mixer.Sound(os.path.dirname(__file__) + "\\sounds\\gameOver.wav").play()
            men = Menu("gameover")
            berries.empty()
            event_time = 3000
            pygame.time.set_timer(ADDBERRY, event_time)
            running = False

        bg.update()
        bg.render()

        for fruit in berries:
            if fruit.update() == True:
                sc.update()
                cl.addTime()
                if sc.counter == 0:
                    berries.remove(fruit)
                    del fruit
                    continue
            fruit.render()        
        
        ui_bar.render()
        uim.hover(x,y)
        uic.hover(x,y)
        cl.update()
        cl.render()
        
        sc.render()
        pygame.display.update()
        clock.tick(FPS)

    ###############################################################################
    # menu loop
    ###############################################################################

    if running == False:
        (x,y) = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        if event.type == MOUSEBUTTONDOWN:
            if men.quitClicked(x,y):
                pygame.mixer.Sound(os.path.dirname(__file__) + "\\sounds\\gameOver.wav").play()
                time.sleep(.3)
                pygame.quit()
                sys.exit()
            if men.retryClicked(x,y):
                pygame.mixer.Sound(os.path.dirname(__file__) + "\\sounds\\retryClick.wav").play()
                berries.empty()
                fr = Fruit(100, SCREEN_HEIGHT / 2 - 100 / 2, SCREEN_WIDTH / 2 - 100 / 2)
                berries.add(fr)
                ADDBERRY = pygame.USEREVENT + 1
                event_time = 3000
                pygame.time.set_timer(ADDBERRY, event_time)
                cl.resetClock()
                sc.resetScore()
                running = True

        bg.update()
        bg.render()
        men.quitHover(x,y)
        men.retryHover(x,y)
        men.render()
        sc.displayScore()

        pygame.display.update()
        clock.tick(FPS)


