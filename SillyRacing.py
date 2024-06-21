import pygame
import random
pygame.init()


display_width = 800
display_height = 600

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Silly lil racecar')

black = (0,0,0)
block_color = (53,115,255)
white = (255,255,255)
green = (0,200,0)
red = (200,0,0)

pause = True

bright_red = (225,0,0)
bright_green = (0,225,0)
crash_sound = pygame.mixer.Sound("crash.wav")


clock = pygame.time.Clock()
carImg = pygame.image.load("racecar.png")
gameIcon = pygame.image.load('icon.png')

pygame.display.set_icon(gameIcon)

def quitgame():
    pygame.quit()
    quit()

def things_dodged(count):
    font = pygame.font.SysFont("comicsansms",25)
    text = font.render("Dodged: " + str(count), True ,black)
    gameDisplay.blit(text,(0,0))

def things(thingx , thingy , thingh , thingw , color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface, textSurface.get_rect()

def crash():
    pygame.mixer.Sound.play(crash_sound)
    largeText = pygame.font.SysFont("comicsansms",115)
    textSurf,textRect = text_objects("You Crashed",largeText)
    textRect.center = (display_width/2,display_height/2)
    gameDisplay.blit(textSurf,textRect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        

        button("Play Again",150,450,100,50,green,bright_green,gameLoop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15) 


# def message_display(text):
#     largeText = pygame.font.SysFont("comicsansms",115)
#     textSurf,textRect = text_objects(text,largeText)
#     textRect.center = (display_width/2,display_height/2)
#     gameDisplay.blit(textSurf,textRect)

#     pygame.display.update()

#     time.sleep(2)
#     gameLoop()

def button(msg,x,y,width,height,inactiveColor,activeColor,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if (x <= mouse[0] <= width+x and y <= mouse[1] <= y + height):
        pygame.draw.rect(gameDisplay,activeColor,(x,y,width,height))
        if(click[0] == True and action != None):
            action()

    else:
        pygame.draw.rect(gameDisplay,inactiveColor,(x,y,width,height))

    smalltext = pygame.font.SysFont("comicsansms",20)
    textSurf,textRect = text_objects(msg,smalltext)
    textRect.center = (x+(width/2),y + (height/2))
    gameDisplay.blit(textSurf,textRect)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",80)
        textSurf,textRect = text_objects("Silly Lil Racecar",largeText)
        textRect.center = (display_width/2,(display_height/2) - 20)
        gameDisplay.blit(textSurf,textRect)

        button("GO!",150,450,100,50,green,bright_green,gameLoop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
def resume():
    global pause
    pause = False

def pause_game():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        largeText = pygame.font.SysFont("comicsansms",80)
        textSurf,textRect = text_objects("Paused",largeText)
        textRect.center = (display_width/2,(display_height/2) - 20)
        gameDisplay.blit(textSurf,textRect)

        button("Continue",150,450,100,50,green,bright_green,resume)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def gameLoop():
    dodged = 0
    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    x_change=0
    car_speed = 0
    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100
    crashed = False
    global pause
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    pause_game()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            

        x += x_change
        if( x > display_width-car_width or x < 0):
            crash()

        if( thing_starty > display_height):
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed+=0.5
            thing_width += 0.1

        if(y < thing_starty + thing_height):
            if(x > thing_startx and x < thing_startx + thing_width or 
               x + car_width > thing_startx and x+car_width < thing_startx + thing_width):
                crash()

        
        gameDisplay.fill(white)
        things(thing_startx,thing_starty,thing_height,thing_width,block_color) #def things(thingx , thingy , thingh , thingw , color):
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
        pygame.display.update()
        clock.tick(60)
game_intro()
gameLoop()  
pygame.quit()
quit()
# <Event(768-KeyDown {'unicode': '', 'key': 1073741906, 'mod': 4096, 'scancode': 82, 'window': None})> UP ARROW
# <Event(769-KeyUp {'unicode': '', 'key': 1073741906, 'mod': 4096, 'scancode': 82, 'window': None})> 
# <Event(768-KeyDown {'unicode': '', 'key': 1073741905, 'mod': 4096, 'scancode': 81, 'window': None})> DOWN ARROW
# <Event(769-KeyUp {'unicode': '', 'key': 1073741905, 'mod': 4096, 'scancode': 81, 'window': None})>
# <Event(768-KeyDown {'unicode': '', 'key': 1073741904, 'mod': 4096, 'scancode': 80, 'window': None})> LEFT ARROW
# <Event(769-KeyUp {'unicode': '', 'key': 1073741904, 'mod': 4096, 'scancode': 80, 'window': None})>
# <Event(768-KeyDown {'unicode': '', 'key': 1073741903, 'mod': 4096, 'scancode': 79, 'window': None})> RIGHT ARROW
# <Event(769-KeyUp {'unicode': '', 'key': 1073741903, 'mod': 4096, 'scancode': 79, 'window': None})>

'''
            #MOVE UP
            if(event.type == 768 and event.dict['key'] == 1073741906):
                y-=5
                y = 0 if y<0 else y
            #MOVE DOWN
            if(event.type == 768 and event.dict['key'] == 1073741905):
                y+=5
                y = display_height*0.8 if y > display_height*0.8 else y
            #MOVE RIGHT
            if(event.type == 768 and event.dict['key'] == 1073741903):
                x+=5
                x = display_width * 0.45 if x > display_width * 0.45 else x
            #MOVE LEFT
            if(event.type == 768 and event.dict['key'] == 1073741904):
                x-=5
                x = 0 if x < 0 else x

'''