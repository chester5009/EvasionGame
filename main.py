import pygame
from Sprite import MySprite
from heroe import Heroe
from enemy import *
import random

size=(640,480)
window= pygame.display.set_mode(size)
pygame.display.set_caption("Evasion")
screen=pygame.Surface((640,480))

isRun=True




heroe= Heroe(10,200,"assets/heroe.png")
enemys=[]

nowTime=pygame.time.get_ticks()

spawnTimer=pygame.time.get_ticks()
spawnTime=1500
def spawnEnemy():
    x=640
    y=random.randint(0,480-30)
    newEnemy=Enemy(x,y,"assets/enemy.png")
    enemys.append(newEnemy)
    pass
spawnEnemy()
while isRun:
    nowTime=pygame.time.get_ticks()
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            isRun=False
       
    screen.fill((0,0,0))
    heroe.render(screen)
    heroe.update()
    heroe.setMove(0)
  
    for i in enemys:
        i.update()
        i.render(screen)
        if i.isLife==False:
            
            enemys.remove(i)
            print "dead"
        pass
        print len(enemys)
    q=pygame.Rect(20,20,50,50)    
    
    if(nowTime-spawnTimer>spawnTime):
        spawnEnemy()
        spawnTimer=pygame.time.get_ticks()
    
    press=pygame.key.get_pressed()
    for i in xrange(0,len(press)):
        if press[i]==1:
            key=pygame.key.name(i)
            if(key=="w" or key=="up"): 
                heroe.setMove(1)
            if(key=="s" or key=="down"):
                heroe.setMove(2)
                
            pass
    
    pygame.time.wait(1000/150)
    
    window.blit(screen,(0,0))
    
    pygame.display.flip()

print "Hello1"