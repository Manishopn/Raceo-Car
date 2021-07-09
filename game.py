import pygame
import time
import sys
import random
pygame.init()

dis_Width = 600
dis_height = 600
gray = (0, 100, 0)
black = (0, 255, 255)
red = (240, 0, 0)
green = (240,0,0)
bright_red = (255,0,0)
bright_green = (240,255,255)
bright_blue = (0,0,255)
blue = (0,0, 200)

#create a window & Caption
pygame.mixer.music.load("intro.wav")
g_display = pygame.display.set_mode((dis_Width, dis_height))
pygame.display.set_caption("RACEO GAME")
clock = pygame.time.Clock()
carimg = pygame.image.load('car4.png')
pygame.display.update()

#create the background of the game
backgroundimg = pygame.image.load("background.png")
carimg_small = pygame.transform.scale(carimg, (50, 100))
intro_background = pygame.image.load("background2.jpg")
intro_background_sl = pygame.transform.scale(intro_background, (600,600))
instruction_background = pygame.image.load("background3.jpg")
instruction_background_sl=pygame.transform.scale(instruction_background, (600, 600))
car_width = 50
pause=False

def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        g_display.blit(intro_background_sl,(0,0))
        largetext = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = text_object(" RACEO CAR", largetext)
        TextRect.center = ((280, 50))
        g_display.blit(TextSurf,TextRect)
        button("START",80,500,100,50,green,bright_green,"play")
        button("QUIT",200,500,100,50,red,bright_red,"quit")
        button("INSTRUCTION",320,500,200,50,blue,bright_blue,"intro")
        pygame.display.update()
        clock.tick(100)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(g_display,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                countdown()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                introduction()
            elif action=="menu":
                intro_loop()
            elif action=="pause":
                paused()
            elif action=="unpause":
                unpaused()


    else:
        pygame.draw.rect(g_display,ic,(x,y,w,h))
    smalltext = pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect= text_object(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    g_display.blit(textsurf,textrect)


def introduction():
    introduction = True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        g_display.blit(intro_background_sl,(0,0))
        largetext= pygame.font.Font('freesansbold.ttf',60)

        smalltext= pygame.font.Font('freesansbold.ttf',18)
        mediumtext= pygame.font.Font('freesansbold.ttf',40)
        textsurf,textrect= text_object("This is an car game in which you need judge the coming cars",smalltext)
        textrect.center=((300),(180))
        TextSurf,TextRect = text_object("INSTRUCTION",largetext)
        TextRect.center=((320),(90))
        g_display.blit(TextSurf,TextRect)
        g_display.blit(textsurf,textrect)
        stextSurf,stextRect= text_object("ARROW LEFT : LEFT TURN",smalltext)
        stextRect=((85),(430))
        hTextSurf,hTextRect= text_object("ARROW RIGHT : RIGHT TURN",smalltext)
        hTextRect.center=((220),(480))
        atextSurf,atextRect = text_object("A : ACCELERATION",smalltext)
        atextRect.center= ((180),(520))
        rtexrSurf,rtextRect = text_object("B :BREAK",smalltext)
        rtextRect.center = ((140),(560))
        ptextSurf,ptextRect = text_object("P : PAUSE", smalltext)
        ptextRect.center= ((240),(390))
        sTextSurf,sTextRect = text_object("CONTROLS",mediumtext)
        sTextRect.center = ((300),(270))

        g_display.blit(stextSurf,stextRect)
        g_display.blit(hTextSurf,hTextRect)
        g_display.blit(TextSurf,TextRect)
        g_display.blit(textsurf,textrect)
        g_display.blit(sTextSurf,sTextRect)
        g_display.blit(ptextSurf,ptextRect)
        g_display.blit(rtexrSurf,rtextRect)
        g_display.blit(atextSurf,atextRect)


        button("BACK",480,500,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)


def paused():
    global pause
    pygame.mixer_music.stop()

    while pause:


            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            g_display.blit(instruction_background_sl,(0,0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_object("PAUSED",largetext)
            TextRect.center=((dis_Width/2),(dis_height/2))
            g_display.blit(TextSurf,TextRect)
            button("CONTINUE",30,450,150,50,green,bright_green,"unpause")
            button("RESTART",200,450,150,50,blue,bright_blue,"play")
            button("MAIN MENU",370,450,200,50,red,bright_red,"menu")
            pygame.display.update()
            clock.tick(30)


def unpaused():
    global pause
    pause=False
    if pause==False:
        pygame.mixer.music.play(-1)


def countdown_background():
    font= pygame.font.SysFont(None,25)
    x = (dis_Width * 0.6)
    y = (dis_height * 0.93)
    g_display.blit(backgroundimg, (0,0))
    g_display.blit(carimg_small, (x, y))
    text = font.render("DODGED: 0", True, black)
    score = font.render("SCORE: 0", True, red)
    g_display.blit(text, (0, 50))
    g_display.blit(score, (0, 30))
    button("PAUSE", 650, 0, 150, 50, blue, bright_blue, "pause")

def countdown():
    countdown=True

    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            g_display.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_object("3",largetext)
            TextRect.center=((dis_Width/2),(dis_height/2))
            g_display.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            g_display.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_object("2",largetext)
            TextRect.center=((dis_Width/2),(dis_height/2))
            g_display.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            g_display.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_object("1",largetext)
            TextRect.center=((dis_Width/2),(dis_height/2))
            g_display.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            g_display.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_object("GO!!!",largetext)
            TextRect.center=((dis_Width/2),(dis_height/2))
            g_display.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_loop()


#import all the obstracle
def obstracle(obs_startx,obs_starty,obs):
    if obs ==0:
        obs_pic = pygame.image.load("car0.png")
        obs_pic_sl = pygame.transform.scale(obs_pic, (50, 100))
    elif obs ==1:
        obs_pic = pygame.image.load("car2.png")
        obs_pic_sl = pygame.transform.scale(obs_pic, (50, 100))
    elif obs ==2:
        obs_pic = pygame.image.load("car3.png")
        obs_pic_sl = pygame.transform.scale(obs_pic, (50, 100))
    elif obs ==3:
        obs_pic = pygame.image.load("car5.png")
        obs_pic_sl = pygame.transform.scale(obs_pic, (50, 100))
    elif obs ==5:
        obs_pic = pygame.image.load("bike.png")
        obs_pic_sl = pygame.transform.scale(obs_pic, (50, 100))
    elif obs == 6:
        obs_pic = pygame.image.load("racecar.png")
        obs_pic_sl = pygame.transform.scale(obs_pic, (50, 100))
    else:
        obs_pic = pygame.image.load("car.png")
        obs_pic_sl = pygame.transform.scale(obs_pic, (50, 100))



    g_display.blit(obs_pic_sl, (obs_startx, obs_starty))


#Show score of the our Game
def score_system(passed, score):
    font = pygame.font.SysFont(None, 55)
    text = font.render("passed" +str(passed),True,black)
    score = font.render("score" +str(score),True,red)
    # text = font.render("Score : " + str(count), True, black)
    # g_display.blit(text, (0, 0)

    g_display.blit(text, (0,50))
    g_display.blit(score, (0,30))






def text_object(text,font):
    textsurface = font.render(text, True, black)
    return textsurface,textsurface.get_rect()


def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    textsurf,textrect = text_object(text, largetext)
    textrect.center = ((dis_Width/2), (dis_height/2))
    g_display.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    pygame.mixer_music.stop()
    message_display("YOU CRASHED")


def background():
    g_display.blit(backgroundimg, (0, 0))

def car(x, y):
    g_display.blit(carimg_small, (x, y))


# def highscore(count):
# 	font = pygame.font.SysFont(None,20)
# 	)

def game_loop():
    global pause
    pygame.mixer.music.play(-1)
    x = (dis_Width*0.5)
    y = (dis_height*0.83)
    x_change = 0
    obstracle_speed = 9
    obs=0
    y_change = 0
    obs_startx= random.randrange(200, dis_Width)
    obs_starty=-575
    obs_width=50
    obs_height=100
    passed=0
    level=0
    score=0
    ax_y=15
    FPS=120


    bumped = False
    while not bumped:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()


           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                   x_change = -5
               if event.key == pygame.K_RIGHT:
                   x_change = 5
               if event.key == pygame.K_a:
                   obstracle_speed += 2
               if event.key == pygame.K_b:
                   obstracle_speed -= 2
           if event.type == pygame.KEYUP:
               if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                   x_change = 0

        x+=x_change
        pause=True
        g_display.fill(gray)


        rel_y=ax_y%backgroundimg.get_rect().width
        g_display.blit(backgroundimg, (0, rel_y - backgroundimg.get_rect().width))
        g_display.blit(backgroundimg, (600, rel_y - backgroundimg.get_rect().width))
        if rel_y<600:
            g_display.blit(backgroundimg, (0, rel_y))
            g_display.blit(backgroundimg, (600, rel_y))

        ax_y+=obstracle_speed


        obs_starty-=(obstracle_speed/4)
        obstracle(obs_startx,obs_starty,obs)
        obs_starty+=obstracle_speed
        car(x, y)
        score_system(passed, score)


        if x>600-car_width or x<10:
            crash()

        if obs_starty > dis_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(0, dis_Width)
            obs=random.randrange(0, 8)
            passed=passed+1
            score = score+1
            score=score+49
            if int(passed)%10 == 0:
                level=level+1
                obstracle_speed+2
                largetext = pygame.font.Font("freesansbold.ttf", 80)
                textsurf, textrect = text_object("LEVEL"+str(level),largetext)
                textrect.center = ((dis_Width / 2), (dis_height / 2))
                g_display.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)

        if y < obs_starty+obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x +car_width <obs_startx+obs_width:
                crash()
        button("Pause",470,0,150,50,blue,bright_blue,"pause")
        pygame.display.update()
        clock.tick(50)

intro_loop()
game_loop()
pygame.quit()
quit()
