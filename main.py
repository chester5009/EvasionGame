import pygame

size=(640,480)
window= pygame.display.set_mode(size)
pygame.display.set_caption("Evasion")
screen=pygame.Surface((640,480))

isRun=True

cloud= pygame.image.load("assets/spr.png")
rect=cloud.get_rect()

while isRun:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            isRun=False
    screen.fill((0,255,0))
    screen.blit(cloud,rect)
    
    window.blit(screen,(0,0))
    
    pygame.display.flip()

print "Hello1"