from ast import Global
from asyncio.windows_events import NULL
from asyncore import loop
from pydoc import cli

import pygame
import time
import wall
import healt
import button
import numpy

pygame.init()

WIDTH  = 704#256
HEIGHT = 512#240
FPS    = 120

YELLOWSAND = (252,216,168)
WHITE  = (255,255,255)

RUN    = True

WINDOWS = pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption('TheLegendOfZelda-PythonClone-MapGenerator')

wall_list  = []
healt_list = []

#0 = HUD #1 Tile
type_tile = 0 
section_index = 0
section_tile  = 0


button_list = []
rows, cols = (22, 22)

T = [[0]*cols for _ in range(rows)]

#DRAW IN WINDOW
def Draw_And_Refresh_Window():
    pygame.draw.rect(WINDOWS,YELLOWSAND,(0,0,WIDTH,HEIGHT))
    for map_wall  in wall_list   : map_wall.Draw()
    for map_healt in healt_list  : map_healt.Draw()
    for button    in button_list : button  .draw()
    IconDraw()
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

#DRAW BUTTON GRID ACROSS THE SCREEN
def drawMapGrid():
    cell = pygame.image.load('assets/Sprites/placeholder.png')
    xmap = 0 ; ymap = 0 
    for i in range(rows):#r
        for j in range(cols):#c
            buttonobj = button.Button(WINDOWS,xmap,ymap,cell,32,32)
            button_list.append(buttonobj)
            T[i][j] = '@@'
            ymap += 32
        xmap+=32 ; ymap = 0

#DRAW TILE IN THE MAP WHEN CLICK THE BUTTON
def click(button):
    pos = button.rect
    mstr = ''
    if(button.click()):
        #Check what kind of tile draw in the map
        #0 = HUD #1 Tile
        if(type_tile == 0): 
            mstr = 'h'
            healtobj = healt.Healt(pos[0],pos[1])
            healt_list.append(healtobj)

        if(type_tile == 1):
            mstr = 'w'
            wallobj = wall.Wall(pos[0],pos[1],section_index,mstr+str(section_tile))
            wall_list.append(wallobj)

        AddToArray(pos[0],pos[1],mstr)
        button_list.remove(button)
    else: return
    
#ADD TO ARRAY THE TILESET ELEMENT THAT CORRESPONDIG TO TILEMAP
def AddToArray(x,y,mstr):
    if(int(x/32) <= 0): x=0 
    else: x = int(x/32)
    if(int(y/32) <= 0): y=0
    else: y = int(y/32)

    if(type_tile == 0): T[y][x] = (mstr)
    if(type_tile == 1): T[y][x] = (mstr+str(section_tile))
    
    

#WHEN THE ARRAY2D IS READY THEN PRINT HIM TO A FILE.TXT
def printArray():
    #apro il file esempio1.txt in scrittura/write(w)
    file1 = open("map1.txt","w")
    for i in range(rows):
        for j in range(cols):
            file1.write(T[i][j]+'  ')
        file1.write('\n')
    file1.close()
    
#ICON THAT APPEAR IN MOUSE POS
def IconDraw():
    if(type_tile == 0):
        imgicon = pygame.image.load('assets/Sprites/hud/healt_2.png')
    if(type_tile == 1):
        imgicon = pygame.image.load('assets/Sprites/tile/section_'+str(section_index)+'/w'+str(section_tile)+'.png')

    imgicon 		  = pygame.transform.scale(imgicon, (32, 32))
    recticon 		  = imgicon.get_rect()
    recticon.topleft = (32, 32)
    WINDOWS.blit(imgicon, pygame.mouse.get_pos())

#CONTROL TILE FUNCTION
def SectionUp():
    global section_index
    if(section_index >= 1): section_index = 1
    else : section_index += 1

def SectionDown():
    global section_index
    if(section_index <= 0): section_index = 0
    else : section_index -= 1

def SectionTileUp():
    global section_tile
    if(section_tile >= 5): section_tile = 5
    else : section_tile += 1

def SectionTileDown():
    global section_tile
    if(section_tile <= 0): section_tile = 0
    else : section_tile -= 1

def TypeTileDown():
    global type_tile
    if(type_tile <= 0): type_tile = 0
    else : type_tile -= 1

def TypeTileUp():
    global type_tile
    if(type_tile >= 1): type_tile = 1
    else : type_tile += 1


def KeyListener():
    for event in  pygame.event.get():
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_e]): pygame.quit()

        if(keys[pygame.K_s]): printArray()  

        if(keys[pygame.K_RIGHT]): SectionUp() 
        if(keys[pygame.K_LEFT]): SectionDown() 

        if(keys[pygame.K_UP]): SectionTileUp() 
        if(keys[pygame.K_DOWN]): SectionTileDown() 

        if(keys[pygame.K_PLUS]) : TypeTileUp()
        if(keys[pygame.K_MINUS]) : TypeTileDown()

        for button in button_list : click(button)
        return

#Function that define gameLoop
def Loop():
    drawMapGrid()
    while RUN:
        KeyListener()
        Draw_And_Refresh_Window()
    while RUN == False: KeyListener()
#-------------------------------------------------------------

Loop()