import pygame,random,time,math

pygame.init()
screen=pygame.display.set_mode([700,700])


class React:
    
    class Sheep:
        def __init__(self):
            self.image=pygame.image.load('sheep.png').convert()
            self.image.set_colorkey((255,255,255))
            self.x1=random.randrange(500)
            self.y1=random.randrange(500)
            self.xv=random.choice([1,2,3,4])*random.choice([1,-1])
            self.yv=random.choice([1,2,3,4])*random.choice([1,-1])

        def move(self):
            self.x1=self.x1+self.xv
            self.y1=self.y1+self.yv
            if 650<=self.x1 or self.x1<=0:
                self.xv=-self.xv
            if 550<=self.y1 or self.y1<=0:
                self.yv=-self.yv
    
    def __init__(self):
        self.winimg=pygame.image.load('youwin.png').convert()
        pygame.font.init()
        self.font=pygame.font.SysFont('comicsansms',25)
        self.sheeplist=[]
        self.sheepno=2
        self.background=pygame.image.load('reactbg.png').convert()
        self.prompt=pygame.image.load('promptreact.png').convert()
        self.blackbar=pygame.image.load('blackbar.png').convert()
        screen.blit((self.background),(0,0))
        screen.blit(pygame.image.load('quit.png').convert(),(0,650))
        pygame.display.flip()
        while 1 :
            self.mainloop()
        
    def mainloop(self):
        self.sheeplist=[]
        screen.blit((self.background),(0,0))
    
        for i in range(self.sheepno):
            f=React.Sheep()
            self.sheeplist.append(f)
            screen.blit(f.image,(f.x1,f.y1))
            time.sleep(0.2)
            pygame.display.flip()
            
        screen.blit(self.prompt,(100,650))
        pygame.display.flip()
        time.sleep(2)
        screen.blit(self.blackbar,(100,650))
        pygame.display.flip()
        time.sleep(2)
            
        self.gameloop()
            
        self.sheepno+=2


    def gameloop(self):
        
        pygame.event.pump()
        start=time.time()
        while time.time()-start<=8:
            
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if 0<=event.pos[0]<=100 and 650<=event.pos[1]<=700:
                        begin()
                elif event.type==pygame.QUIT:
                    pygame.quit()

                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=event.pos
                    if 0<=event.pos[0]<=100 and 650<=event.pos[1]<=700:
                        begin()
                    elif 0<=event.pos[1]<=600:
                        xp,yp=pos[0],pos[1]
                        for sheep in self.sheeplist:
                            x1=sheep.x1
                            x2=x1+50
                            y1=sheep.y1
                            y2=y1+50
                            if x1<xp<x2 and y1<yp<y2:
                                self.sheeplist.remove(sheep)
                                print self.sheeplist
            for sheep in self.sheeplist:
                sheep.move()
            screen.blit((self.background),(0,0))
            for sheep in self.sheeplist:
                screen.blit(sheep.image,(sheep.x1,sheep.y1))
            remtime=abs(6-(time.time()-start))+1
            fontsurf=self.font.render(str(int(remtime)),True,(255,255,255))
            screen.blit(fontsurf,(10,10))
            pygame.display.flip()
            time.sleep(0.02)
            if self.sheeplist==[]:
                break
            
        else:
            screen.blit(pygame.image.load('youlose.png').convert(),(100,650))
            pygame.display.flip()
            time.sleep(2)
            screen.blit(self.blackbar,(100,650))
            begin() 
                            
        screen.blit(self.blackbar,(100,650))
        screen.blit(self.winimg,(100,650))
        pygame.display.flip()
        time.sleep(1.5)
        screen.blit(self.blackbar,(100,650))
        pygame.display.flip()
      
React()    
        
        


        
