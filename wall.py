from re import X
import pygame
import init
import time

class Wall:
    def __init__(self,x,y,section,imgtxt):
        self.section = section
        self.name = 'wall'
        self.x = x
        self.y = y
        self.imgtxt = imgtxt
        self.destroy = False

        self.img = pygame.image.load('assets/Sprites/tile/section_'+str(self.section)+'/'+self.imgtxt+'.png')
        self.img = pygame.transform.scale(self.img , (32, 32))
        self.rect = self.img.get_rect()
        self.rect.center = (init.WIDTH/2,init.HEIGHT/2)

        
    
    def Draw(self):
        if(not self.destroy): init.WINDOWS.blit(self.img,(self.x,self.y))