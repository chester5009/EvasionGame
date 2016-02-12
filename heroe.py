from Sprite import MySprite
import pygame
class Heroe(MySprite):
    
    isMoveUp=False
    isMoveDown=False
    reloadTimer=pygame.time.get_ticks()
    reloadTime=250
    nowTime=0
    isFire=True
    speed=2.5
    def setMove(self,i):
        if i==0:
            self.isMoveDown=False
            self.isMoveUp=False
        if i==1:
            self.isMoveDown=False
            self.isMoveUp=True
        if i==2:
            self.isMoveDown=True
            self.isMoveUp=False
        pass
    
    def moveUp(self):
        if(self.isMoveUp==True): self.y-=self.speed
        if self.y<0:
            self.y=0
        pass
    def moveDown(self):
        if(self.isMoveDown==True): self.y+=self.speed
        if self.y+self.bitmap.get_height()>480:
            self.y=480-self.bitmap.get_height()
    
    def update(self):
        self.nowTime=pygame.time.get_ticks()
        if(self.reloadTimer+self.reloadTime>self.nowTime):
            self.isFire=False
        else:
            self.isFire=True
        self.moveDown()
        self.moveUp()
        self.boundRect.left=self.x
        self.boundRect.top=self.y
        
        pass
    
    pass

    
    
    