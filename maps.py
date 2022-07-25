from cmath import sin
import pygame

import array
import os.path

rows, cols = (22, 22)

maps_list  = []

#ARRAY MAPP
map = [
    ['w0','w0','w0','w0','w0','w0','w0','w0','w0','w0',' ',' '  ,'w0','w0','w0','w0','w0','w0','w0','w0','w0','w0'] , #0
    ['w0','w0','w0','w0','w0','w0','w0','w0','w0','w0',' ',' '  ,'w0','w0','w0','w0','w0','w0','w0','w0','w0','w0'], #1
    ['w0','w0','w0','w0','w0','w0','w0', 'd','w0','w2',' ',' '  ,'w0','w0','w0','w0','w0','w0','w0','w0','w0','w0'], #2
    ['w0','w0','w0','w0','w0','w0','w2','  ','  ','  ',' ',' '  ,'w0','w0','w0','w0','w0','w0','w0','w0','w0','w0'], #3
    ['w0','w0','w0','w0','w0','w0','  ','  ','  ','  ',' ',' '  ,'w0','w0','w0','w0','w0','w0','w0','w0','w0','w0'], #4
    ['w0','w0','w0','w0','w0','w2','  ','  ','  ','  ',' ',' '  ,'w0','w0','w0','w0','w0','w0','w0','w0','w0','w0'], #5
    ['w0','w0','w0','w0','w2','  ','  ','  ','  ','  ',' ',' '  ,'w3','w0','w0','w0','w0','w0','w0','w0','w0','w0'], #6
    ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '], #7
    ['w1','w5','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','w1','w1'], #8
    ['w0','w0','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','w0','w0'], #9
    ['w0','w0','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','w0','w0'], #10
    ['w0','w0','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','w0','w0'], #11
    ['w0','w0','w1','w1','w1','w1','w1','w1','w1','w1','w1','w1','w1','w1','w1','w1','w1','w1','w1','w1','w0','w0'], #12
    ['w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0'], #13
    ['w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0'], #14
    ['w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0','w0']  #15
    ]

def FillMapList():
    for id in range(100):
        file_exists = os.path.exists("Assets/Maps/map"+str(id)+".txt")
        if(file_exists):
            single_file = open("Assets/Maps/map"+str(id)+".txt")
            maps_list.append(single_file)
    
    for single_file  in maps_list   : print(single_file.read())
    

def ReadMap(map,id):
    T = [[0]*cols for _ in range(rows)]

    for i in range(rows):#r
        for j in range(cols):#c
            T[i][j] = '  '

    file1 = open("Assets/Maps/map"+str(id)+".txt","r")#apro il file esempio1.txt in scrittura/write(w)
    with file1 as file:
        line_array = file.read().splitlines()
        #for line in line_array: print(line.split()) 
        T = [line.split() for line in line_array]
        #print(T)
    return T
    