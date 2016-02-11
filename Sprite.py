import pygame
class MySprite:
    def __init__(self,posx,posy,filename):
        self.x=posx
        self.y=posy
        self.bitmap=pygame.image.load(filename)
        self.bitmap.set_colorkey((0,0,0))
        self.bitmap=pygame.transform.scale(self.bitmap,(30,30))
        pass
        
    def render(self,screen):
        screen.blit(self.bitmap,(self.x,self.y))
        pass
    
    def update(self):
        pass
       
        