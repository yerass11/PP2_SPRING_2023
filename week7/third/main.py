import pygame
pygame.init()

# cons
SIZE = WIDTH, HIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (253, 16, 59)
BLUE = (79, 236, 97)
GREEN = (147, 224, 83)
FPS = 60
RADIUS = 25
x = WIDTH // 2
y = HIGHT // 2
speed = 5

screen = pygame.display.set_mode(SIZE)
done = False
clock = pygame.time.Clock()

# quit

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
# move
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - RADIUS - speed >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + RADIUS + speed <= WIDTH:
        x += speed
    if keys[pygame.K_UP] and y - RADIUS - speed >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + RADIUS + speed <= HIGHT:
        y += speed


    screen.fill(WHITE)
    circle = pygame.draw.circle(screen, RED, (x, y), RADIUS)
    pygame.display.update()
    clock.tick(FPS)