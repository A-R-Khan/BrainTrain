import pygame,random,time

pygame.init()
screen=pygame.display.set_mode([700,700])


class Vision:
    
    class Fish:
        def __init__(self,isTarget=False):
            self.image=pygame.image.load('fish.png').convert()
            self.image.set_colorkey((0,0,0))
            self.isTarget=isTarget
            if self.isTarget:
                pygame.draw.rect(self.image,(255,0,0),[0,0,20,20])
            self.x1=random.randrange(500)
            self.y1=random.randrange(500)
            self.xv=random.choice([1,2])*random.choice([1,-1])
            self.yv=random.choice([1,2])*random.choice([1,-1])

        def move(self):
            self.x1=self.x1+self.xv
            self.y1=self.y1+self.yv
            if 650<=self.x1 or self.x1<=0:
                self.xv=-self.xv
            if 550<=self.y1 or self.y1<=0:
                self.yv=-self.yv
    
    def __init__(self):
        pygame.font.init()
        self.clock=pygame.time.Clock()
        self.fishlist=[]
        self.fishno=2
        self.noise=4
        self.background=pygame.image.load('fishbg.png').convert()
        self.prompt1=pygame.image.load('promptvision1.png').convert()
        self.prompt2=pygame.image.load('promptvision2.png').convert()
        self.blackbar=pygame.image.load('blackbar.png').convert()
        screen.blit((self.background),(0,0))
        screen.blit(pygame.image.load('quit.png').convert(),(0,650))
        pygame.display.flip()
        while 1 :
            self.mainloop()
        
    def mainloop(self):
        self.fishlist=[]
        screen.blit((self.background),(0,0))
    
        for i in range(self.fishno):
            f=Vision.Fish(True)
            self.fishlist.append(f)
            screen.blit(f.image,(f.x1,f.y1))
            time.sleep(0.2)
            pygame.display.flip()
        screen.blit(self.prompt1,(100,650))
        pygame.display.flip()
        time.sleep(2)
        screen.blit(self.blackbar,(100,650))
        pygame.display.flip()
        
        for i in range(self.noise):
            f=Vision.Fish()
            self.fishlist.append(f)
            screen.blit(f.image,(f.x1,f.y1))
        screen.blit(self.prompt2,(100,650))
        pygame.display.flip()
        time.sleep(2)
        screen.blit(self.blackbar,(100,650))
        pygame.display.flip()
        time.sleep(2)
            
        result=self.gameloop()
        if not result:
            return
        self.fishno+=1
        self.noise+=1


    def gameloop(self):
        correctfish,wrongfish=0,0
        start=time.time()
        while time.time()-start<=8:
            for fish in self.fishlist:
                fish.move()
            screen.blit((self.background),(0,0))
            for fish in self.fishlist:
                screen.blit(fish.image,(fish.x1,fish.y1))
            pygame.display.flip()
            time.sleep(0.02)
        flag=True
        while flag:
            for event in pygame.event.get():
                if correctfish+wrongfish==self.fishno:
                    flag=False
                    break
                if event.type==pygame.QUIT:
                    return
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    pos=event.pos
                    if 0<=event.pos<=100 and 650<=event.pos<=700:
                        return
                    xp,yp=pos[0],pos[1]
                    for fish in self.fishlist:
                        x1=fish.x1
                        x2=x1+50
                        y1=fish.y1
                        y2=y1+50
                        if x1<xp<x2 and y1<yp<y2:
                            if fish.isTarget:
                                if fish.isTarget==2:
                                    break
                                correctfish+=1
                                fish.isTarget=2
                            break
                    else: wrongfish+=1
        print correctfish
        print wrongfish
        font=pygame.font.SysFont('comicsansms',30)
        fontsurf=font.render('Correct:'+str(correctfish)+'  Wrong:'+str(wrongfish),True,(255,201,14))
        screen.blit(fontsurf,(250,660))
        pygame.display.flip()
        time.sleep(1.5)
        screen.blit(self.blackbar,(100,650))
        pygame.display.flip()
        if correctfish<wrongfish:
            return False
        return True
        
                
                    
                

        
                     

