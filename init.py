from os import remove
import pygame

import healt
import wall
import random

import array
import maps

#set variable screen && FPS
WIDTH  = 704#256
HEIGHT = 576#240
FPS    = 120
RUN    = True

#set variable hud
hudW = WIDTH
hudH = 64


rupy      = 0
rupyimg   = pygame.image.load('assets/Sprites/hud/rupie.png')
rupyimg   = pygame.transform.scale(rupyimg , (16, 16))

key       = 0
keyimg    = pygame.image.load('assets/Sprites/hud/key.png')
keyimg    = pygame.transform.scale(keyimg , (16, 16))

bomb      = 0
bombimg   = pygame.image.load('assets/Sprites/hud/bomb.png')
bombimg   = pygame.transform.scale(bombimg , (16, 16))

#COLOR VARIABLE
WHITE  = (255,255,255)
BLACK  = (0, 0, 0)
YELLOW = (255,255,0)
RED    = (255,0,0)

YELLOWSAND = (252,216,168)

#optimization map variable
healt_list = []
wall_list  = []

#set window
WINDOWS = pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption('TheLegendOfZelda-PythonClone')

#Optimazion Function
def GenerateMap(T):
    #A quanto pare y e x sono invertiti
    xmap = 64 ; ymap = 0 ; xt   = 0 ; yt = 0
    for i in T:
        for j in i:
            if(T[xt][yt] != '@@' and T[xt][yt] != 'h'):
                wallobj = wall.Wall(ymap,xmap,0,T[xt][yt])
                wall_list.append(wallobj)
            if(T[xt][yt] == 'h'):
                healtobj = healt.Healt(ymap,xmap)
                healt_list.append(healtobj)
            ymap += 32 ; yt += 1
        
        xmap += 32 ; xt += 1
        yt = 0 ; ymap = 0

def RestartMap():
     #A quanto pare y e x sono invertiti
   healt_list.clear()
   wall_list.clear()    

def DrawMap():
     for map_healt in healt_list: map_healt.Draw()
     for map_wall  in wall_list : map_wall.Draw()