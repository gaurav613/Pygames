import pygame
import time, random
pygame.init()

#basic window creation - width and height for dynamic reference
display_width =800
display_height = 600

#rgb color codes
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,200,0)
RED = (200,0,0)
LIGHT_RED = (255,0,0)
LIGHT_GREEN = (0,255,0)
GREY = (119,136,153)
PURPLE = (255,0,255)

#text sizes
smallText = pygame.font.Font('freesansbold.ttf', 20)
mediumText = pygame.font.Font('freesansbold.ttf', 30)
largeText = pygame.font.Font('freesansbold.ttf',60)
gameDisplay = pygame.display.set_mode((display_width,display_height)) #setting height and width of game window
pygame.display.set_caption("Car Racing") #title of game window

carImg = pygame.image.load("Images/car.png")
taxiImg = pygame.image.load("Images/frontal-taxi-cab.png")

clock = pygame.time.Clock() #timing for game

#method to draw a block which will act as an obstacle
def things(x,y,w,h):
    gameDisplay.blit(taxiImg,(x,y))

#draws the car(in this case, the image) at (x,y) position
def car(x,y):
    gameDisplay.blit(carImg, (x,y)) 

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

#display a message in the center of the screen
def message_display(message):
    largeText = pygame.font.Font('freesansbold.ttf',30)
    TextSurf, TextRect = text_objects(message, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash():
    message_display('YoU cRaShEd! GaMe OvEr')

#method to display button with clicking
def button(message, x, y, w, h, inactive, active, action = "None"):
    mouse = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()

    #highlight button when hovered over
    if (x+w > mouse[0] > x and y+h > mouse[1] > y):
        pygame.draw.rect(gameDisplay,active,(x,y,w,h))

        if clicked[0] == 1 and action!="None":#left click
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()


    else:
        pygame.draw.rect(gameDisplay,inactive,(x,y,w,h))

    #add text over button    
    TextSurf, TextRect = text_objects(message, smallText)
    TextRect.center = ( (x + (w/2)), (y+(h/2)) )
    gameDisplay.blit(TextSurf, TextRect)

#scoring- increment the score once the obstacle is avoided, and display on the top right
def add_score(score):
    font = pygame.font.SysFont(None,25)
    text =  font.render("Score: "+ str(score), True, BLACK)
    gameDisplay.blit(text,(0,0))

#load a start screen
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(WHITE)

        
        TextSurf, TextRect = text_objects("Dodger", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("START",200,450,100,50,GREEN,LIGHT_GREEN,"play")
        button("QUIT",500,450,100,50,RED,LIGHT_RED,"quit")
        pygame.display.update()
        clock.tick(15)

#game loop
def game_loop():
    #setting the starting position of car
    x = 0.45 * display_width
    y = 0.8 * display_height 

    x_change = 0 #change in x direction(when key is pressed)

    thing_startx = random.randrange(0,display_width)
    thing_starty =  -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100
    thing_repeat = [random.randrange(0,display_width-thing_width)]
    thing_count = 1
    score = 0 #starting score is zero
    
    #the game is about not crashing into another object- so a crash variable is used to end the game
    isCrashed = False
    gameExit = False
    car_width = 128
    while not gameExit:
        #creating a list of events(in this case, key presses) that may happen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#in this event, the user decides to quit the game
                pygame.quit()
                quit
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                
            #when key is released, there must be no change in position
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    x_change = 0
        
        x+=x_change

        gameDisplay.fill(WHITE)#change background color

        things(thing_startx , thing_starty, thing_width, thing_height)

        thing_starty += thing_speed
        car(x,y)
        #important to print score last, so that there's no overlapping
        add_score(score)

        #crash if the car hits the window boundary
        if x > (display_width - car_width) or x < 0:
            crash()

        #block goes off the screen, reset. Also means that the car avoided the obstacle, increasing the score
        if thing_starty > display_height : 
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, (display_width-thing_width))
            score += 1
            if(score%5== 0):
                thing_speed += 2

        if (y+22 < thing_starty + thing_height) and (y+22>thing_starty):
            if( (thing_startx + thing_width) > x > (thing_startx - car_width) ):
                crash()

        pygame.display.update() #can update specific parameters, or entire display(no parameters)
        clock.tick(60) #frames per second
game_intro()
game_loop()
pygame.quit()
quit
