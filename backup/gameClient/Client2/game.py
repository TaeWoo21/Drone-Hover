# -*- coding: utf-8 -*-
"""
tensorflow 기반 강화학습 드론 호버링 구현




"""
import pygame, sys
import sysv_ipc
from pygame.locals import *

FPS = 60 # 주사율
resolution = (1500,1000) #해상도
COLOR = {'BLACK':(0,0,0),'WHITE':(255,255,255),'BLUE':(0,0,25),'YELLOW':(255,215,0),'RED':(255,0,0),'GREEN':(0,255,255),} # 컬러 코드 프리셋
quator_num = 0
text_rocation1 = (0,0)

#memory = sysv_ipc.SharedMemory(510) # 공유 메모리

#smp = sysv_ipc.Semaphore(22)       #세마포어

"""
def check_degree():
    smp.acquire(10)                    #세마포어 ON
    vari = memory.read()
    smp.release()                      #세마포어 OFF
    degree360 = 360 - (float(vari.rstrip('\x00')) + 360) % 360  # 각도 360도로 변환
    degree180 = -1 * float(vari.rstrip('\x00'))                 # 각도 왼쪽 오른쪽 변환

    return degree360, degree180
"""
def font_init():
    global FONT


    name_score = fontObj.render("enter your name ---->", True, COLOR['BALCK'])

    name_socreObj = name_score.get_rect()
    name_socreObj.center = (500, 520)
    return name_socreObj

def Drone_simulation():

    SCREEN = pygame.display.set_mode(resolution, 0, 32)            # 해상도 및 기초 설정
    fpsClock = pygame.time.Clock()                                      # 주사율 설정
    FONT = pygame.font.Font('nanum.ttf', 50)

    pygame.display.set_caption('AI_Drone_game')
    name_scoreObj = font_init()

    while(True):
            #degree360, degree180 = self.check_degree()
            #print degree180
        for event in pygame.event.get():                                    #게임 이벤트 핸들로
            if event.type == pygame.QUIT:                                   # 게임 종료시 시스템 종료
                pygame.quit()
                sys.exit()

        if quator_num == 0:
            pass
        SCREEN.blit(name_scoreObj, (400, 300))
        SCREEN.fill(COLOR['WHITE'])                                   #게임 화면을 하얀색으로 덮기
        pygame.display.update()
        fpsClock.tick(FPS)
def main():

    global fpsClock, SCREEN, FONT
    pygame.init()
    SCREEN = pygame.display.set_mode(resolution, 0, 32)
    fpsClock = pygame.time.Clock()
    pygame.display.set_caption('AI_Drone_game')
    FONT = pygame.font.Font('nanum.ttf', 50)

    text1 = FONT.render("enter your name ---->", True, COLOR['BLACK'])
    textObj1 = text1.get_rect()
    textObj1.center = text_rocation1

    while True:  # main game loop
        SCREEN.fill(COLOR['WHITE'])
        SCREEN.blit(text1, textObj1)









if __name__ == "__main__":
    main()