from re import X
import pygame
import init
import time

class Rupee:
    def __init__(self,x,y):
        self.name = 'rupee'
        self.x = x
        self.y = y

        self.img = pygame.image.load('assets/Sprites/hud/rupie.png')
        self.img = pygame.transform.scale(self.img , (16, 16))

        self.destroy = False
    
    def Draw(self):
        if(not self.destroy): init.WINDOWS.blit(self.img,(self.x,self.y))