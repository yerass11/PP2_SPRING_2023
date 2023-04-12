import pygame as pg
import time, sys, random

pg.init()
pg.mixer.init()
clock = pg.time.Clock()
WIDTH = 800
HEIGHT = 800
screen = pg.display.set_mode([WIDTH, HEIGHT])
icon = pg.image.load("./images/mysnake.png")
pg.display.set_caption('Snake game 2.0')
fps = 6
clock = pg.time.Clock()

background = pg.image.load('./images/1.png')
background = pg.transform.scale(background, (800, 800))
gameover = pg.image.load('./images/gameover.jpg')
gamover = pg.transform.scale(gameover, (800, 800))
score = pg.font.SysFont('Game Over Regular', 70)
score2 = pg.font.SysFont('Game Over Regular', 100)


pg.display.set_icon(icon)
speed = 40
level = 0
timing = False
timing2 = False
running = True
lose = False
eat = False
eat2 = False
counter = 5

class Food:
    def __init__(self):
        self.x = random.randrange(40, 760, speed)
        self.y = random.randrange(40, 760, speed)
        self.bx = random.randrange(40, 760, speed)
        self.by = random.randrange(40, 760, speed)
        self.food = random.randint(1, 7)
        self.s = random.randint(1, 3)
        self.badfood = random.randint(1, 2)
        self.image = pg.image.load(f'./images/food{self.food}.png')
        self.badimage = pg.image.load(f'./images/badfood{self.badfood}.png')
        self.rect2 = self.image.get_rect()
        self.rect2.center = (self.bx, self.by)

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self):
        screen.blit(self.image, self.rect.center)
        screen.blit(self.badimage, self.rect2.center)

    def seconddraw(self):
        self.x = random.randrange(40, 760, speed)
        self.y = random.randrange(40, 760, speed)
        self.food = random.randint(1, 7)
        self.image = pg.image.load(f'./images/food{self.food}.png')
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        screen.blit(self.image, (self.rect.center))

    def seconddrawforbad(self):
        self.bx = random.randrange(40, 760, speed)
        self.by = random.randrange(40, 760, speed)
        self.badfood = random.randint(1, 2)
        self.badimage = pg.image.load(f'./images/badfood{self.badfood}.png')
        self.rect2 = self.image.get_rect()
        self.rect2.center = (self.bx, self.by)
        screen.blit(self.badimage, (self.rect2.center))

class Snake:
    def __init__(self):
        self.speed = speed
        self.body = [[360, 360]]
        self.dx = 0
        self.dy = 0
        self.color = 'green'
        self.score = 0
        self.score2 = 0
    def move(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and self.dy == 0:
                    self.dx = 0
                    self.dy = -self.speed
                if event.key == pg.K_DOWN and self.dy == 0:
                    self.dx = 0
                    self.dy = self.speed
                if event.key == pg.K_LEFT and self.dx == 0:
                    self.dx = -self.speed
                    self.dy = 0
                if event.key == pg.K_RIGHT and self.dx == 0:
                    self.dx = self.speed
                    self.dy = 0
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]
        self.body[0][0] += self.dx  
        self.body[0][1] += self.dy 
        print(self.body)
    def draw(self):
        for block in self.body:
            pg.draw.rect(screen, self.color, (block[0], block[1], speed, speed), 5)

    def eat_food(self):
        global eat
        global eat2
        if self.body[0][0] == f.x and self.body[0][1] == f.y:   
            eat = True
            self.score +=1
            self.score2 +=1
            global timing
            timing = True
            pg.mixer.Sound('./music/eat.mp3').play()
            self.body.append([1000, 1000])
        if self.body[0][0] == f.bx and self.body[0][1] == f.by:
            pg.mixer.Sound('./music/eat.mp3').play()
            eat2 = True
            global timing2
            timing2 = True
            if len(self.body) > 1:
                self.body.pop(0)
            self.score -=1
        
    

    def collision(self):
        global lose
        if self.body[0] in self.body[1:]:
            pg.mixer.Sound('./music/gameover.wav').play()
            lose = True
    
    def newfood(self):
        if [f.x, f.y] == self.body:
            f.seconddraw()
        elif [f.bx, f.by] == self.body:
            f.seconddrawforbad()
        # elif f.x == f.bx and f.y == f.by:
        #     f.seconddrawforbad()

class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pg.image.load('./images/wall.png')

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

def disappear(t):
    pg.time.set_timer(pg.USEREVENT, t)

f = Food()   
s = Snake()     
disappear(6000)
# pg.mixer.Sound('./music/snake.mp3').play()
while running:
    clock.tick(fps)
  
    screen.blit(background, (0, 0))
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.USEREVENT and timing == False:
            f.seconddraw()
        if event.type == pg.USEREVENT and timing2 == False:
            f.seconddrawforbad()

    my_walls = open(f'wall{level}.txt', 'r').readlines()
    walls = []
    for i , line in enumerate(my_walls):
        for j , each in enumerate(line):
            if each == '+':
                walls.append(Wall(j*speed, i*speed))

    f.draw()
    s.draw()
    s.move(events)
    s.eat_food()
    s.collision()
    
    # s.newfood()
    if s.score == -1:
        cnt1 = score2.render(f'You are lose', True, 'black')
        cnt2 = score2.render(f'You should not eat this apple!', True, 'red')
        screen.blit(cnt1 , (50, 50))
        screen.blit(cnt2,   (50, 85))
    else:
        cnt = score.render(f'Your score: {s.score}', True, 'red')
        screen.blit(cnt, (50, 50))
        lvl = score.render(f'Level: {level}', True, 'red')
        screen.blit(lvl, (50, 80) )


    if s.score < 0:
        pg.mixer.Sound('./music/gameover.wav').play()
        lose = True
    # if s.score == 0 and f.bx == s.body[0][0] and f.by == s.body[0][1] an:
    #     lose = True

    # if f.x == s.body[0][0] and f.y == s.body[0][1]:
    #     s.newfood()
    if f.bx == s.body[0][0] and f.by == s.body[0][1]:
        s.newfood()
    for wall in walls:
        wall.draw()
        if f.x == wall.x and f.y == wall.y:
            f.seconddraw()
        if f.bx == wall.x and f.by == wall.y:
            f.seconddrawforbad()
        if s.body[0][0] == wall.x and s.body[0][1] == wall.y:
            pg.mixer.Sound('./music/gameover.wav').play()
            lose = True
    if eat:
        f.seconddraw()
        eat = False
    if eat2:
        f.seconddrawforbad()
        eat2 = False
    if timing:
        timmer = 6000
        disappear(timmer)
        # f.seconddraw()
        timing = False
    if timing2:
        timmer = 6000
        disappear(timmer)
        timing2 = False
    if s.score > counter:
        level +=1
        level %= 4
        counter +=5
        fps+=2
    while lose:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                lose = False
                pg.quit()
                sys.exit()
        screen.blit(gameover, (310, 350))
        count = s.score
        if s.score == -1:
            count = 0
        loosing2 = score.render(f'Result: {count}', True , 'red')
        screen.blit(loosing2, (343, 430))

        pg.display.update()
        pg.display.flip()
        
    pg.display.update()
    pg.display.flip()
