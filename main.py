import pygame
from Sprite import MySprite
from heroe import Heroe
from enemy import *
from bullet import *
import random

pygame.init()
size=(640,480)
window= pygame.display.set_mode(size)
pygame.display.set_caption("Evasion")
screen=pygame.Surface((640,480))

isRun=True




heroe= Heroe(10,200,"assets/heroe.png")
enemys=[]
hBullets=[]

nowTime=pygame.time.get_ticks()

scores="Scores: _"
score=0

def addScore():
    score=score+1
    pass

def intersects(l1,l2,type):
    for i in l1:
        for j in l2:
            if(i.boundRect.colliderect(j.boundRect)):
                l1.remove(i)
                l2.remove(j)
                print "BOOM"
                if(type==1):
                    addScore()
                    print s
                pass
    pass

def shoting():
    if(heroe.isFire==True):
        x=heroe.x+heroe.bitmap.get_width()+10
        y=heroe.y+heroe.bitmap.get_height()/2
        
        newBullet=bullet(x,y,"assets/bullet.png")
        newBullet.initBullet(x,y,4,0)
        
        hBullets.append(newBullet)
        heroe.reloadTimer=pygame.time.get_ticks()
    pass

spawnTimer=pygame.time.get_ticks()
spawnTime=1500

def spawnEnemy():
    x=640
    y=random.randint(0,480-30)
    newEnemy=Enemy(x,y,"assets/enemy.png")
    enemys.append(newEnemy)
    pass
spawnEnemy()

def drawScores():
    scores="Scores: "+str(score)
    font = pygame.font.Font(None, 36)
    text=font.render(scores,1,(100,100,100))
    textpos=text.get_rect()
    screen.blit(text,textpos)
    pass

while isRun:
    nowTime=pygame.time.get_ticks()
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            isRun=False
       
    screen.fill((0,0,0))
    
   
    
    
    heroe.render(screen)
    heroe.update()
    heroe.setMove(0)
    drawScores()
    for i in enemys:
        i.update()
        i.render(screen)
        if i.isLife==False:
            
            enemys.remove(i)
            print "dead"
        pass
        #print len(enemys)
    q=pygame.Rect(20,20,50,50)    
    
    for i in hBullets:
        i.update()
        i.render(screen)
        
    
    if(nowTime-spawnTimer>spawnTime):
        spawnEnemy()
        spawnTimer=pygame.time.get_ticks()
    intersects(hBullets, enemys,1)
    press=pygame.key.get_pressed()
    for i in xrange(0,len(press)):
        if press[i]==1:
            key=pygame.key.name(i)
            if(key=="w" or key=="up"): 
                heroe.setMove(1)
            if(key=="s" or key=="down"):
                heroe.setMove(2)
            if(key=="space"):
                shoting()
                
            pass
    
    pygame.time.wait(1000/350)
    
    window.blit(screen,(0,0))
    
    pygame.display.flip()

print "Hello1"