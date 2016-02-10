import pygame
class MySprite:
    def __init__(self,posx,posy,filename):
        self.x=posx
        self.y=posy
        self.bitmap=pygame.image.load(filename)
        self.bitmap.set_colorkey((0,0,0))
        
    def render(self,screen):
        screen.blit(self.bitmap,(self.x,self.y))
    
    def update(self):
        self.x+=0.05
        