import pygame
import sys
import datetime

COLOR_BACK = (250, 255, 255)
size = [830, 780]

screen = pygame.display.set_mode(size)
mickey = pygame.image.load("images/main-clock.png")
left_hand = pygame.image.load('images/left-hand.png')
right_hand = pygame.image.load('images/right-hand.png')
pygame.display.set_caption("Mickey Clock")

def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surf.blit(rotated_image, new_rect)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exist")
            pygame.quit()
            sys.exit()
    screen.fill(COLOR_BACK)
    screen.blit(mickey, (0, 0))
    time = datetime.datetime.now()
    minute = time.minute
    second = time.second
    

    blitRotateCenter(screen, left_hand, (180, 320), ((second % 60) / 60) * -360)
    blitRotateCenter(screen, right_hand, (160, 310), ((minute % 60) / 60) * -(360 - 40))
    
    pygame.display.flip()
    clock.tick(60)
    
    #FINAL IS THIS
    