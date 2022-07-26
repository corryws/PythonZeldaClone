from os import remove
import pygame

import healt
import wall
import rupee
import enemy

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

rupyimg   = pygame.image.load('assets/Sprites/hud/rupie.png')
rupyimg   = pygame.transform.scale(rupyimg , (16, 16))

keyimg    = pygame.image.load('assets/Sprites/hud/key.png')
keyimg    = pygame.transform.scale(keyimg , (16, 16))

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
rupee_list = []
enemy_list = []

#set window
WINDOWS = pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption('TheLegendOfZelda-PythonClone')

#Optimazion Function
def GenerateMap(T):
    #A quanto pare y e x sono invertiti
    xmap = 64 ; ymap = 0 ; xt   = 0 ; yt = 0
    for i in T:
        for j in i:
            if(T[xt][yt] != '@@' 
                and T[xt][yt] != 'h'
                and T[xt][yt] != 'r'
                and T[xt][yt] != 'e0'):
                wallobj = wall.Wall(ymap,xmap,0,T[xt][yt])
                wall_list.append(wallobj)
            if(T[xt][yt] == 'h'):
                healtobj = healt.Healt(ymap,xmap)
                healt_list.append(healtobj)
            if(T[xt][yt] == 'r'):
                rupeeobj = rupee.Rupee(ymap,xmap)
                rupee_list.append(rupeeobj)
            if(T[xt][yt] == 'e0'):
                enemyobj = enemy.Enemy(ymap,xmap)
                enemy_list.append(enemyobj)
            ymap += 32 ; yt += 1
        
        xmap += 32 ; xt += 1
        yt = 0 ; ymap = 0

def RestartMap():
   healt_list.clear()
   wall_list.clear()
   rupee_list.clear()    

def DrawMap():
     for map_healt in healt_list : map_healt.Draw()
     for map_wall  in wall_list  : map_wall.Draw()
     for map_rupee in rupee_list : map_rupee.Draw()
     for map_enemy in enemy_list : 
        map_enemy.Draw()
        map_enemy.AnimationDirection()
        map_enemy.MovementPattern()