import pygame
from carRacer import Car
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
GREY = (119,136,153)
PURPLE = (255,0,255)

size = (400,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Car Racer")

all_sprites_list = pygame.sprite.Group()

playerCar = Car(RED,200,300)
playerCar.rect.x = 200
playerCar.rect.y = 300

all_sprites_list.add(playerCar)

carryOn = True
clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                carryOn=False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        playerCar.moveRight(5)
    if keys[pygame.K_DOWN]:
        playerCar.moveLeft(5)

    #Drawing on Screen
    screen.fill(GREEN)
    #Draw The Road
    pygame.draw.rect(screen, GREY, [40,0, 200,500])
    #Draw Line painting on the road
    pygame.draw.line(screen, WHITE, [140,0],[140,500],5)


    pygame.display.flip()
    clock.tick(60)



#Once we have exited the main program loop we can stop the game engine:
pygame.quit()