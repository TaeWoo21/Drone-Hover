# -*- coding: utf-8 -*-
import sysv_ipc
import time
import pygame, sys
from pygame.locals import *

import sqlite3
import math
from Tkinter import *


def time_calculate(start_time,end_time,now_sec):
    now_time = ""
    now_msec = end_time - start_time
    time_str = ""
    if now_msec >= 1000:
        now_sec = now_sec + 1
        now_msec = now_msec - 1000
        start_time = int(round(time.time() * 1000))
        strmsec = str(now_msec)
    time_str = str(now_sec) + "\"" + str(now_msec)
    return time_str, now_sec, start_time


    return now_time,now_sec
def ranking_update(now_time,user_name ):
    conn = sqlite3.connect('game_rank.db')
    curs = conn.cursor()

    game_name = ""

    print "your score is :",;print now_time

    sql = "INSERT INTO game_rank VALUES(?, ?);"
    name, time = user_name,now_time

    curs.execute(sql, (name, time))
    conn.commit()
    conn.close()




def ranking_print():
    conn = sqlite3.connect('game_rank.db')
    curs = conn.cursor()
    count = 0
    name_list = []
    rank_list = []

    curs.execute("select * from game_rank order by time desc")
    rows = curs.fetchall()

    for row in rows:
        name_list.append(row[0])
        rank_list.append(row[1])
        count = count +1
        if count == 10:
            conn.close()
            return name_list, rank_list,count


    return name_list,rank_list, count


#proc = subprocess.Popen(["python","thread_test7.py"])
COLOR = {'BLACK':(0,0,0),'WHITE':(255,255,255),'YELLOW':(255,255,224),'RED':(255,0,0),'GREEN':(0,255,255),'orange':(255,165,0)} # 컬러 코드 프리셋
memory =sysv_ipc.SharedMemory(510)
smp = sysv_ipc.Semaphore(22)
dbup = 0

pygame.init()

FPS = 30
# frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 500), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption('Animation')

catImg = pygame.image.load('123.png')
startbutton = pygame.image.load('button1.png')

degree =30



quit_check = 0
now_time = ""
button_name = "button1.png"
button_smp = 0
start_ok =0
end_ok = 0
start_time = 0

hei = 600
str3213 = ""
now_sec = 0
now_time = ""
score = 0
resolutionx = 0
resolutiony = 0
font = pygame.font.Font(None, 40)
input_box = pygame.Rect(250, 200, 40, 40)
input_box2 =pygame.Rect(250, 300, 40, 40)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
color2 = color_inactive
active = False
active2 = False
text = ''
text2 =''
done = False
rank_count=1
degree2 = 0.0
while(True):
    check_input = 0





    img = pygame.image.load(button_name)

    image = pygame.image.load(button_name)
    imagerect = image.get_rect()
    imagerect.center=(400,400)

    nameObj = pygame.font.Font('123.ttf', 20)


    sector = pygame.image.load('124.png')
    sectorrect = sector.get_rect()
    sectorrect.center=(750,700)



    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos() # gets mouse position


            if imagerect.collidepoint(mouse_pos):

                print('button was pressed at {0}'.format(mouse_pos))
                button_name = "button3.png"
                button_smp = 1
                start_ok = 1

                game_start_time = time.time()
            if input_box.collidepoint(event.pos):
                # Toggle the active variable.
                active = not active

            else:
                active = False

            if input_box2.collidepoint(event.pos):
                active2 = not active2
            else:
                active2 = False

            color = color_active if active else color_inactive
            color2 = color_active if active2 else color_inactive
        elif event.type == pygame.MOUSEMOTION and button_smp != 1 :
            mouse_pos = pygame.mouse.get_pos()  # gets mouse position

            if imagerect.collidepoint(mouse_pos)and button_smp != 1:

                button_name = "button2.png"
            else:
                button_name = "button1.png"


        print pygame.mouse.get_pos()

        if not hasattr(event, 'key'):
            continue

        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print(text)
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            if active2:
                if event.key == pygame.K_RETURN:
                    print(text2)
                    text2 = ''
                elif event.key == pygame.K_BACKSPACE:
                    text2 = text2[:-1]
                else:
                    text2 += event.unicode
        if keys[pygame.K_ESCAPE]:
            print("Left key press...")
            #pygame.quit()

            end_ok = 0
            start_ok = 0
            button_smp = 0
            now_sec = 0
            end_time = 0
            score = 0
            text = ''
            text2 = ''

    game_end_time = time.time()

    DISPLAYSURF.fill(COLOR['WHITE'])
    if start_ok ==1 and game_end_time - game_start_time <5:

        resolution = text2.split('.')
        resolutionx = resolution[0]
        resolutiony = resolution[1]
        x_ratio = float(resolutionx)/1000
        y_ratio = float(resolutiony) / 1500


        DISPLAYSURF2 = pygame.display.set_mode((int(resolutionx), int(resolutiony)), pygame.HWSURFACE | pygame.DOUBLEBUF)
        DISPLAYSURF2.fill(COLOR['WHITE'])
        timerObj = pygame.font.Font('123.ttf', 200)
        if(int(game_end_time - game_start_time) ==0):
            timer = 5
        if(int(game_end_time - game_start_time) ==1):
            timer = 4
        if(int(game_end_time - game_start_time) ==2):
            timer = 3
        if(int(game_end_time - game_start_time) ==3):
            timer = 2
        if(int(game_end_time - game_start_time) ==4):
            timer = 1
        timer_score = timerObj.render(str(timer) + "", True, COLOR['RED'])
        timer_socreObj = timer_score.get_rect();
        #timer_socreObj.center = (750  , 500)
        timer_socreObj.center = (int(resolutionx)/2, int(resolutiony) /2 )
        DISPLAYSURF2.blit(timer_score, timer_socreObj)
        star_time = int(round(time.time() * 1000))
    if start_ok == 1 and game_end_time - game_start_time >=5:
        #start_time =  int(round(time.time() * 1000))
        now_time = ""
        end_time = int(round(time.time() * 1000))
        fontObj = pygame.font.Font('123.ttf', int (50 *(x_ratio + y_ratio)/2))
        now_time,now_sec, start_time =time_calculate(start_time, end_time, now_sec)
        time_score = fontObj.render(now_time, True, COLOR['BLACK'])

        time_socreObj = time_score.get_rect();
        time_socreObj.center = (float(resolutionx) *0.9, 20)

        dataObj = pygame.font.Font('123.ttf', int (50 *(x_ratio + y_ratio)/2))
        degree_score = dataObj.render(str(int(degree2)), True, COLOR['BLACK'])

        degree_socreObj = degree_score.get_rect();
        degree_socreObj.center = (float(resolutionx) *0.04, 20)

        ncountObj = pygame.font.Font('123.ttf', int (50 *(x_ratio + y_ratio)/2))
        ncount_score = ncountObj.render(str(score), True, COLOR['BLACK'])

        ncount_socreObj = ncount_score.get_rect()
        ncount_socreObj.center = (float(resolutionx)*0.7, 20)
        print score
        if now_sec>= 20 and now_sec <21:
            if dbup ==0:
                ranking_update(score, text)
                dbup = dbup +1

            end_ok = 1

    if end_ok ==0 and start_ok ==1  :
        catImg = pygame.transform.scale(catImg, (int( 997 * (x_ratio + y_ratio)/2) , int( 997* (x_ratio +y_ratio)/2)))
        rotated = pygame.transform.rotate(catImg, float(degree))
        rect = rotated.get_rect()
        rect.center = (int(resolutionx)/2  , int(float(resolutiony) *0.80) )
    if end_ok == 1:
        hei =0
        game_end_time = 0
        game_start_time = 0
        DISPLAYSURF2.fill(COLOR['WHITE'])
        font_size = 35 * int((x_ratio +y_ratio)/2)
        if font_size <= 20:
            font_size =20

        dataObj = pygame.font.Font('123.ttf', font_size  )

        howmany_count = 0
        name_list, rank_list, howmany_count = ranking_print()

        rankObj = pygame.font.Font('123.ttf', font_size)
        rankObj.set_bold(True)
        hei = int(float(resolutiony) * 0.35)

        rank_count = 1
        rank_color = COLOR['BLACK']
        for i in range(0,howmany_count):
            if name_list[i] == text:
                rank_color = COLOR['RED']
            else:
                rank_color = COLOR['BLACK']
            rank_score = rankObj.render(str(rank_list[i]), True, rank_color)


            name_score = rankObj.render(str(name_list[i]), True, rank_color)


            count_score = rankObj.render(str(rank_count), True, rank_color)
            strank_score = rankObj.render("RANK", True, COLOR['BLACK'])

            stname_score = rankObj.render("NAME", True, COLOR['BLACK'])

            stcount_score = rankObj.render("SCORE", True, COLOR['BLACK'])
            DISPLAYSURF2.blit(stcount_score, (int(float(resolutionx )* 0.2),int(float(resolutiony) * 0.25)))
            DISPLAYSURF2.blit(stname_score, (int(float(resolutionx )* 0.4),int(float(resolutiony )* 0.25)))
            DISPLAYSURF2.blit(strank_score, (int(float(resolutionx) * 0.8),int(float(resolutiony) * 0.25)))

            DISPLAYSURF2.blit(count_score, (int(float(resolutionx )* 0.2),hei))

            DISPLAYSURF2.blit(name_score, (int(float(resolutionx )* 0.4),hei))
            DISPLAYSURF2.blit(rank_score, (int(float(resolutionx) * 0.8) ,hei))
            hei = hei + int(40* (x_ratio +y_ratio)/2)
            rank_count  = rank_count + 1





    if start_ok == 1 and end_ok !=1 and game_end_time - game_start_time >=5:

        smp.acquire(20)
        vari = memory.read()
        smp.release()

        degree = 360 - (float(vari.rstrip('\x00')) + 360) % 360
        degree2 = -1 * float(vari.rstrip('\x00'))
        print degree
        aradar = (int(resolutionx)/2  , int(float(resolutiony) *0.80))
        aradar_len = int( 500 *(x_ratio + y_ratio)/2)
        ax = aradar[0] + math.cos(math.radians(280)) * aradar_len
        ay = aradar[1] + math.sin(math.radians(280)) * aradar_len
        bradar = (int(resolutionx)/2  , int(float(resolutiony) *0.80))
        bradar_len =int( 500 *(x_ratio + y_ratio)/2)
        bx = bradar[0] + math.cos(math.radians(260)) * bradar_len
        by = bradar[1] + math.sin(math.radians(260)) * bradar_len
        if (degree >= 350 and degree <360) or (degree >=0 and degree <10):
            score = score + 10
            tri_color = COLOR['YELLOW']
        else:
            tri_color = COLOR['RED']


        pygame.draw.line(DISPLAYSURF, COLOR['BLACK'], bradar, (bx, by), 9)
        pygame.draw.line(DISPLAYSURF, COLOR['BLACK'], aradar, (ax, ay), 9)
        pygame.draw.polygon(DISPLAYSURF, tri_color, ((ax, ay), (bx, by), (int(resolutionx)/2  , int(float(resolutiony) *0.80))))
        DISPLAYSURF2.blit(time_score, time_socreObj)
        DISPLAYSURF2.blit(degree_score, degree_socreObj)
        DISPLAYSURF2.blit(ncount_score, ncount_socreObj)
        DISPLAYSURF2.blit(rotated, rect)

    if start_ok == 0:

        nameObj = pygame.font.Font('123.ttf', 20)

        name_score = nameObj.render("enter your ID ---->", True, COLOR['BLACK'])

        name_socreObj = name_score.get_rect();
        name_socreObj.center = (input_box.x-100, input_box.y +20)

        name_score2 = nameObj.render("enter resolution ---->", True, COLOR['BLACK'])

        name_socreObj2 = name_score2.get_rect();
        name_socreObj2.center = (input_box2.x-102, input_box2.y+20)

        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        DISPLAYSURF.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(DISPLAYSURF, color, input_box, 2)


        txt_surface2 = font.render(text2, True, color)
        width2 = max(200, txt_surface2.get_width() + 10)
        input_box2.w = width
        DISPLAYSURF.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(DISPLAYSURF, color2, input_box2, 2)
        DISPLAYSURF.blit(name_score, name_socreObj)

        DISPLAYSURF.blit(name_score2, name_socreObj2)
    if start_ok != 1 and end_ok != 1:
        DISPLAYSURF.blit(image, imagerect)

    print degree









    pygame.display.update()
    fpsClock.tick(FPS)

time.sleep(100)
pygame.display.quit()
pygame.quit()






