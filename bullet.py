from Sprite import *
import pygame

class bullet(MySprite):

    x=0
    y=0
    dx=0
    dy=0

    
    def initBullet(self,x,y,dx,dy):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.bitmap=pygame.transform.scale(self.bitmap,(5,5))
        self.boundRect=pygame.Rect(self.x,self.y,5,5)
        pass
    
    def update(self):
        self.x+=self.dx
        self.y+=self.dy
        self.boundRect.left=self.x
        self.boundRect.top=self.y
        pass
    

    pass