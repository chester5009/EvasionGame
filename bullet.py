import pygame
import MySprite

class Bullet(MySprite):
    
    def __init__(self):
        super().__init__()
        pass
    x=0
    y=0
    dx=0
    dy=0
    def setBullet(self,x,y,dx,dy):
        self.x=x
        self.y=y
        self.dx=dx
        
        pass
    pass