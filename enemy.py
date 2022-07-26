from re import X
import pygame
import init
import time

class Enemy:
    def __init__(self,x,y):
        self.name = 'enemy'
        self.x = x
        self.y = y
        self.life = 1
        self.spd = 5

        self.anim = 1

        self.img = pygame.image.load('assets/Sprites/enemy/e0/0_'+str(self.anim)+'.png')
        self.img = pygame.transform.scale(self.img , (32, 32))

        self.destroy = False
    
    def Draw(self):
        if(not self.destroy): init.WINDOWS.blit(self.img,(self.x,self.y))
    
    def AnimationDirection(self):
        time.sleep(0.05)
        self.img = pygame.image.load('assets/Sprites/enemy/e0/0_'+str(self.anim)+'.png')
        self.img  = pygame.transform.scale(self.img , (32, 32))
        self.anim = -self.anim
        self.y += self.spd 

    def Collider(self,obstacle,name):
        ox = obstacle.x ; oy = obstacle.y
        if(name == 'wall' and obstacle.imgtxt != 'd'):
            col = 32
            if(self.x > ox-col and self.x < ox+col and self.y > oy-col and self.y < oy+col):
                if(self.y <= oy-col+self.spd): self.y -= self.spd
                if(self.y >= oy+col-self.spd): self.y += self.spd
                if(self.x <= ox-col+self.spd): self.x -= self.spd
                if(self.x >= ox+col-self.spd): self.x += self.spd