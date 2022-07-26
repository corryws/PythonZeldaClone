import pygame
import init
import time
import maps

class Link:
    def __init__(self):
        self.x      = init.WIDTH/2
        self.y      = init.HEIGHT/2
        self.spd    = 10

        self.img       = pygame.image.load('assets/Sprites/link/link_down_1.png')
        self.img       = pygame.transform.scale(self.img , (32, 32))
        self.anim      = -1

        self.health    = 3
        self.healthimg = pygame.image.load('assets/Sprites/hud/healt_2.png')
        self.healthimg = pygame.transform.scale(self.healthimg , (16, 16))

        self.rupie      = 0
        self.key        = 0
        self.bomb       = 0

    def KeyListener(self):
        for event in  pygame.event.get():
            #if(event.type == pygame.KEYDOWN): print(pygame.key.name(event.key))
            keys = pygame.key.get_pressed()
            if(keys[pygame.K_q]): init.RUN = not init.RUN
            if(keys[pygame.K_e]): pygame.quit()
            if(init.RUN):
                if(keys[pygame.K_w]): self.y -= self.spd ; self.AnimationDirection('up'   )
                if(keys[pygame.K_s]): self.y += self.spd ; self.AnimationDirection('down' )
                if(keys[pygame.K_d]): self.x += self.spd ; self.AnimationDirection('right')
                if(keys[pygame.K_a]): self.x -= self.spd ; self.AnimationDirection('left' )
                self.MapBorderCheck() ; self.anim = -self.anim ; return
    
    def AnimationDirection(self,dir):
            time.sleep(0.05)
            self.img  = pygame.image.load('assets/Sprites/link/link_'+str(dir)+'_'+str(self.anim)+'.png')
            self.img  = pygame.transform.scale(self.img , (32, 32))
            #print('X' + str(self.x) + ' Y' + str(self.y))

    def Draw(self): init.WINDOWS.blit(self.img,(self.x,self.y))

    def MapBorderCheck(self):
        if(self.y <= init.hudH)  :
            self.y = init.HEIGHT-32
            self.MapBorderGenerateMap(-1,0)
            
        if(self.y >= init.HEIGHT):
            self.y = init.hudH
            self.MapBorderGenerateMap(1,0)
            
        if(self.x <= 0)          :
            self.x = init.WIDTH-32
            self.MapBorderGenerateMap(0,-1)
            
        if(self.x >= init.WIDTH) :
            self.x = 0
            self.MapBorderGenerateMap(0,1)
                   
    def MapBorderGenerateMap(self,addx,addy):
        maps.overworldy += (addy)
        maps.overworldx += (addx)
        init.RestartMap()
        init.GenerateMap(maps.ReadMap(maps.StartMap(maps.overworldx,maps.overworldy)))

    def Collider(self,obstacle,name):
        ox = obstacle.x ; oy = obstacle.y

        if(name == 'healt'):
            col = 16
            if(self.x >= ox-col and self.x <= ox+col and self.y >= oy-col and self.y <= oy+col
            and self.health < 16 and not obstacle.destroy): self.LifeSystem() ; obstacle.destroy = True
        
        if(name == 'rupee'):
            col = 16
            if(self.x >= ox-col and self.x <= ox+col and self.y >= oy-col and self.y <= oy+col
            and self.health < 16 and not obstacle.destroy): self.RupeeSystem() ; obstacle.destroy = True
        
        if(name == 'enemy'):
            col = 32
            if(self.x >= ox-col and self.x <= ox+col and self.y >= oy-col and self.y <= oy+col
            and self.health < 16 and not obstacle.destroy): self.RupeeSystem() ; obstacle.destroy = True

        if(name == 'wall' and obstacle.imgtxt != 'd'):
            col = 32
            if(self.x > ox-col and self.x < ox+col and self.y > oy-col and self.y < oy+col):
                if(self.y <= oy-col+self.spd): self.y -= self.spd
                if(self.y >= oy+col-self.spd): self.y += self.spd
                if(self.x <= ox-col+self.spd): self.x -= self.spd
                if(self.x >= ox+col-self.spd): self.x += self.spd
                
    
    def LifeSystem(self):
        time.sleep(0.09)
        self.health+=1
    
    def RupeeSystem(self):
        time.sleep(0.09)
        self.rupie +=1