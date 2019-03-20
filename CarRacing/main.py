import pygame
pygame.init()

#basic window creation - width and height for dynamic reference
display_width =1000
display_height = 800

#rgb color codes
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
GREY = (119,136,153)
PURPLE = (255,0,255)

gameDisplay = pygame.display.set_mode((display_width,display_height)) #setting height and width of game window
pygame.display.set_caption("Car Racing") #title of game window

carImg = pygame.image.load("Images/car.png")

clock = pygame.time.Clock() #timing for game

def car(x,y):
    gameDisplay.blit(carImg, (x,y)) #draws the car(in this case, the image) at (x,y) position

#game loop
def game_loop():
    #setting the starting position of car
    x = 0.45 * display_width
    y = 0.8 * display_height 

    x_change = 0 #change in x direction(when key is pressed)
    
    #the game is about not crashing into another object- so a crash variable is used to end the game
    isCrashed = False
    gameExit = False
    car_width = 128
    while not gameExit:
        #creating a list of events(in this case, key presses) that may happen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#in this event, the user decides to quit the game
                gameExit = True
            
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
        car(x,y)

        if x > (display_width - car_width) or x < 0:
            gameExit = True

        pygame.display.update() #can update specific parameters, or entire display(no parameters)
        clock.tick(60) #frames per second

game_loop()
pygame.quit()
quit
