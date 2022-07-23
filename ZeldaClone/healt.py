from re import X
import pygame
import init
import time

class Healt:
    def __init__(self,x,y):
        self.name = 'healt'
        self.x = x
        self.y = y

        self.img = pygame.image.load('assets/Sprites/hud/healt_2.png')
        self.img = pygame.transform.scale(self.img , (16, 16))

        self.destroy = False
    
    def Draw(self):
        if(not self.destroy): init.WINDOWS.blit(self.img,(self.x,self.y))