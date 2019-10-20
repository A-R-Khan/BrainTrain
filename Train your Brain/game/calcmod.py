import pygame,random,time

pygame.init()
screen=pygame.display.set_mode([700,700])



class Calc:
    class Number:
        total=0
        def __init__(self,opt=False):
            imgid=random.randint(1,15)
            print Calc.Number.total
            self.image=pygame.image.load('num'+str(imgid)+'.png').convert()
            self.image.set_colorkey((255,255,255))
            self.isTarget=opt
            self.x1=random.randrange(500)
            self.y1=random.randrange(500)
            if self.isTarget:
                Calc.Number.total+=imgid
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
        self.font=pygame.font.SysFont('arialblack',40)
        self.background=pygame.image.load('calcbg.png').convert()
        self.blackbar=pygame.image.load('blackbar.png').convert()
        self.prompt1=pygame.image.load('promptcalc1.png').convert()
        self.prompt2=pygame.image.load('promptcalc2.png').convert()
        screen.blit(pygame.image.load('quit.png').convert(),(0,650))
        self.correct=pygame.image.load('correct.png').convert()
        self.numno=2
        self.noise=4
        pygame.display.flip()
        while 1 :
            self.mainloop()

    def mainloop(self):
        Calc.Number.total=0
        self.numlist=[]
        for i in range(self.numno):
            self.numlist.append(Calc.Number(True))
        screen.blit((self.background),(0,0))
        pygame.display.flip()
        for num in self.numlist:
            screen.blit(num.image,(num.x1,num.y1))
        screen.blit(self.prompt1,(100,650))
        pygame.display.flip()
        time.sleep(1)
        
        for i in range(self.noise):
            self.numlist.append(Calc.Number())
        for num in self.numlist:
            screen.blit(num.image,(num.x1,num.y1))
        screen.blit(self.prompt2,(100,650))
        pygame.display.flip()
        time.sleep(1)
        screen.blit(self.blackbar,(100,650))
        pygame.display.flip()
        self.gameloop()
        self.noise+=1
        self.numno+=1

    def gameloop(self):
        numstr=''
        start=time.time()
        while time.time()-start<=6:
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if 0<=event.pos[0]<=100 and 650<=event.pos[1]<=700:
                        begin()
                elif event.type==pygame.QUIT:
                    pygame.quit()
                elif event.type==pygame.KEYDOWN:
                    keyy=event.key
                    if keyy in range(48,58):
                        numstr+=str(keyy-48)
                        print numstr
                        if numstr==str(Calc.Number.total):
                            screen.blit(self.correct,(100,650))
                            pygame.display.flip()
                            time.sleep(2)
                            return
                        elif len(numstr)>=len(str(Calc.Number.total)):
                            screen.blit(pygame.image.load('youlose.png').convert(),(100,650))
                            pygame.display.flip()
                            time.sleep(2)
                            screen.blit(self.blackbar,(100,650))
                            begin()

            for num in self.numlist:
                if num.isTarget:
                    num.move()
            screen.blit((self.background),(0,0))
            for num in self.numlist:
                screen.blit(num.image,(num.x1,num.y1))
            pygame.display.flip()
            remtime=abs(6-(time.time()-start))+1
            b=0
            if remtime<4:
                r,g=255,0
            else:
                r,g=0,255
            fontsurf=self.font.render(str(int(remtime)),True,(r,g,b))
            screen.blit(fontsurf,(10,10))
            pygame.display.flip()    
            time.sleep(0.02)
        screen.blit(pygame.image.load('youlose.png').convert(),(100,650))
        fontsurf=self.font.render(str(0),True,(r,g,b))
        screen.blit(fontsurf,(10,10))
        pygame.display.flip()    
        pygame.display.flip()
        time.sleep(2)
        screen.blit(self.blackbar,(100,650))
        begin()



        
Calc()        

