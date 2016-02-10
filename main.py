import pygame
from Sprite import MySprite
size=(640,480)
window= pygame.display.set_mode(size)
pygame.display.set_caption("Evasion")
screen=pygame.Surface((640,480))

isRun=True




heroe= MySprite(100,100,"assets/spr.png")

while isRun:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            isRun=False
       
    screen.fill((0,255,0))
    heroe.render(screen)
    heroe.update()
     
    window.blit(screen,(0,0))
    
    pygame.display.flip()

print "Hello1"