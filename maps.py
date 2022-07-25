from cmath import sin
import pygame

import array
import os.path

rows, cols = (22, 22)

maps_list  = []

overworldmap = [[1,0,2],
                [0,0,2],
                [1,2,1]]

overworldx = 0
overworldy = 0

def FillMapList():
    global overworldx ; global overworldy
    id = 0
    file_exists = os.path.exists("Assets/Maps/map"+str(id)+".txt")
    while file_exists != False:
        file_exists = os.path.exists("Assets/Maps/map"+str(id)+".txt")
        if(file_exists):
            single_file = open("Assets/Maps/map"+str(id)+".txt")
            maps_list.append(single_file)
            id+=1
    
    for i in range(len(overworldmap)):#r
        for j in range(len(overworldmap[0])):#c
            if(overworldmap[i][j] == 0):
                overworldx = i
                overworldy = j

def StartMap(x,y):
    global overworldx ; global overworldy
    colon = len(overworldmap[0])
    rows  = len(overworldmap)
    print('prima del controllo ' + str(x) + str(y))

    if(x > colon-1)  : x = colon-1
    if(x < 0)        : x = 0
    if(y > rows-1)   : y = rows-1
    if(y < 0)        : y = 0

    print('dopo del controllo ' + str(x) + str(y))
    overworldx = x ; overworldy = y
    
    return overworldmap[x][y] 

def ReadMap(id):
    T = [[0]*cols for _ in range(rows)]

    for i in range(rows):#r
        for j in range(cols):#c
            T[i][j] = '  '

    file1 = open("Assets/Maps/map"+str(id)+".txt","r")#apro il file esempio1.txt in scrittura/write(w)
    with file1 as file:
        line_array = file.read().splitlines()
        T = [line.split() for line in line_array]
    return T
    