import pygame
from Sprite import MySprite
from heroe import *
size=(640,480)
window= pygame.display.set_mode(size)
pygame.display.set_caption("Evasion")
screen=pygame.Surface((640,480))

isRun=True




heroe= MySprite(100,100,"assets/enemy.png")

while isRun:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            isRun=False
       
    screen.fill((0,255,0))
    heroe.render(screen)
     
    window.blit(screen,(0,0))
    
    pygame.display.flip()

print "Hello1"