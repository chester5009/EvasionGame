from Sprite import MySprite

class Enemy(MySprite):
    
    speed=0;
    acceleration=0.1
    maxSpeed=0.7
    isLife=True
    
    def update(self):
        self.speed+=self.acceleration
        if(self.speed>self.maxSpeed): self.speed=self.maxSpeed
        self.x-=self.speed
        
        if self.x+self.bitmap.get_width()<0:
            self.isLife=False
        self.boundRect.left=self.x
        self.boundRect.top=self.y
        pass
