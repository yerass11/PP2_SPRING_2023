import pygame , sys , random , time , os
from pygame.locals import *
pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
Green = (0, 255, 0)
size = [400, 600]
cnt = 0
e_library_of_images = {}

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Racer game")

# icon = pygame.image.load("images/vehicle.png") 
# pygame.display.set_icon(icon)

background = pygame.image.load("assignment1/images/streen.png")

FPS = 60
FramePerSec = pygame.time.Clock()

running = True

coinFont = pygame.font.SysFont("childer", 40)
# screen.fill(WHITE)

def get_images(name):
    global e_library_of_images
    path = os.path.join(os.getcwd(), 'images', 'Enemy', name)
    image = e_library_of_images.get(path)
    if image == None:
        image = pygame.image.load(path)
        e_library_of_images[path] = image
        return image
    

class Player(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("assignment1/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 550) 
        self.speed = 15
    def move(self): 
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 400:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(self.speed, 0)
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -self.speed)
        if self.rect.bottom < 600:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, self.speed)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()
        self.rand = random.randint(1, 6)
        # self.image = pygame.image.load('images/Enemy' + f'/{str(self.rand)}.png')
        # self.image = get_images(f'{self.rand}.png')
        self.image = pygame.image.load('assignment1/images/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, 400 - 40), 0)
        self.speed2 = 15
    
    def move(self):
        self.rect.move_ip(0, self.speed2) 
        self.speed2 +=0.001
        if (self.rect.bottom > 600): 
            self.rect.top = 0 
            self.rect.center = (random.randint(20, 360), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coins(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assignment1/images/tyre.png") 
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(10, 390), 25) 
    
    def move(self):
        self.rect.move_ip(0, 5) 
        if self.rect.bottom > 600: 
            self.rect.top = 0 
            self.rect.center = (random.randint(20, 360), 25)
    

P1 = Player()
E1 = Enemy()
C1 = Coins()

enemies = pygame.sprite.Group() 
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
     

    score = coinFont.render(str(cnt), True, Green)
    screen.blit(background, (0, 0))
    screen.blit(score, (350, 25))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
        if pygame.sprite.spritecollideany(P1, enemies):
            # pygame.mixer.Sound('crash.mp3').play()
            time.sleep(0.1)
            photo = pygame.image.load("assignment1/images/game_over.png")   
            screen.blit(photo, (30, 60))
            print("You lose dumb!")
            print(f"Your score is: {cnt}")

            pygame.display.update()
            for entity in all_sprites:
                    entity.kill()
            time.sleep(1)
            pygame.quit()
            sys.exit()
            
        if pygame.sprite.spritecollideany(P1, coins ):
            # pygame.mixer.Sound('coin.mp3').play()
            cnt+=1
            C1.rect.top = 600
                  
    pygame.display.update()
    pygame.display.flip()
    FramePerSec.tick(FPS)