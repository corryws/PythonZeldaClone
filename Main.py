from itertools import count
from pickle import TRUE

import pygame
import time

from Link import Link
import init
import Link
import healt
import random
import wall
import maps

pygame.init()

l = Link.Link()
maps.FillMapList()
init.GenerateMap(maps.ReadMap(maps.StartMap(maps.overworldx,maps.overworldy)))

#set FONT
FONT = pygame.font.SysFont('Nintendo NES Font regular',24)

#Draw in Window
def Draw_And_Refresh_Window():
    pygame.draw.rect(init.WINDOWS,init.YELLOWSAND,(0,0,init.WIDTH,init.HEIGHT))
    
    DrawHUD()
    init.DrawMap()
    l.Draw()

    if(not init.RUN): print("PAUSE")

    #Update Windows Frame
    pygame.display.update()
    pygame.time.Clock().tick(init.FPS)

def DrawHUD():
    #rectangle
    pygame.draw.rect(init.WINDOWS,init.BLACK,(0,0,init.hudW,init.hudH))
    
    #health
    lifehud = FONT.render('-LIFE-',1,init.RED)
    init.WINDOWS.blit(lifehud,(init.WIDTH-85,0))
    healtlist = []
    for i in range(l.health):
        healtlist.append(l.healthimg)

    spacex = init.WIDTH-132
    countx = spacex
    county = 16
    counth = 0
    for singleheart in healtlist:
        init.WINDOWS.blit(singleheart,(countx,county))
        countx += 16 ; counth += 1
        if(counth == 8): 
            countx = spacex  ; county = 32

    #rupie
    init.WINDOWS.blit(init.rupyimg,(80,0))
    rupyinfo = FONT.render('x' + str(init.rupy),1,init.WHITE)
    init.WINDOWS.blit(rupyinfo,(96,0))

    #key
    init.WINDOWS.blit(init.keyimg,(80,16))
    keyinfo = FONT.render('x' + str(init.key),1,init.WHITE)
    init.WINDOWS.blit(keyinfo,(96,16))

    #bomb
    init.WINDOWS.blit(init.bombimg,(80,32))
    bombinfo = FONT.render('x' + str(init.bomb),1,init.WHITE)
    init.WINDOWS.blit(bombinfo,(96,32))

def ColliderCheck():
    for singleh in init.healt_list: l.Collider(singleh,singleh.name)
    for singlew in init.wall_list: l.Collider(singlew,singlew.name)

#Function that define gameLoop
def GameLoop():
    while init.RUN:
        l.KeyListener()
        ColliderCheck()
        Draw_And_Refresh_Window()
    while init.RUN == False: l.KeyListener()
    return GameLoop()
#-------------------------------------------------------------

GameLoop()