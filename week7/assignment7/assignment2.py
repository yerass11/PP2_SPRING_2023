import pygame as pg
import sys

pg.init()
WHITE = (255, 255, 255)
RED = (255, 0, 0)
clock = pg.time.Clock()

size = [800, 600]
x , y = 800 // 2 , 600//2
speed = 20
r = 25

screen = pg.display.set_mode(size)
pg.display.set_caption("Ball game")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    keys = pg.key.get_pressed()
    if keys[pg.K_UP] and y-r > 0:
        y-=speed
    if keys[pg.K_DOWN] and y+r < 600:
        y+=speed
    if keys[pg.K_LEFT] and x-r > 0:
        x-=speed
    if keys[pg.K_RIGHT] and x+r < 800:
        x+=speed

    screen.fill(WHITE)
    pg.draw.circle(screen, RED, (x, y), r)
    clock.tick(30)

    pg.display.update()
    pg.display.flip()