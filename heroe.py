from Sprite import MySprite

class Heroe(MySprite):
    isMoveUp=False
    isMoveDown=False
    
    def setMove(self,i):
        if i==0:
            self.isMoveDown=False
            self.isMoveUp=False
        if i==1:
            self.isMoveDown=False
            self.isMoveUp=True
        if i==2:
            self.isMoveDown=True
            self.isMoveUp=False
        pass
    
    def moveUp(self):
        if(self.isMoveUp==True): self.y-=1
        if self.y<0:
            self.y=0
        pass
    def moveDown(self):
        if(self.isMoveDown==True): self.y+=1
        if self.y+self.bitmap.get_height()>480:
            self.y=480-self.bitmap.get_height()
    
    def update(self):
        self.moveDown()
        self.moveUp()
        
        pass
    
    pass

    
    
    