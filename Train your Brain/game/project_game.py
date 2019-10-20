import pygame,random,time
pygame.init()
screen=pygame.display.set_mode([700,700])

class React:
    
    class Sheep:
        def __init__(self):
            self.image1=pygame.image.load('sheep.png').convert()
            self.image2=pygame.image.load('sheep2.png').convert()
            self.image1.set_colorkey((255,255,255))
            self.image2.set_colorkey((255,255,255))
            self.image=self.image1
            self.x1=random.randrange(500)
            self.y1=random.randrange(500)
            self.xv=random.choice([1,2,3,4])*random.choice([1,-1])
            self.yv=random.choice([1,2,3,4])*random.choice([1,-1])

            
        def move(self):
            if self.yv<0:
                self.image=self.image2
            else:
                self.image=self.image1
            self.x1=self.x1+self.xv
            self.y1=self.y1+self.yv
            if 650<=self.x1 or self.x1<=0:
                self.xv=-self.xv
            if 550<=self.y1 or self.y1<=0:
                self.yv=-self.yv
    
    def __init__(self):
        self.score=0
        self.winimg=pygame.image.load('youwin.png').convert()
        pygame.font.init()
        self.font=pygame.font.SysFont('comicsansms',30)
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
        
        for event in pygame.event.get():pass
        start=time.time()
        while time.time()-start<=6:
            screen.blit((self.background),(0,0))
            for sheep in self.sheeplist:
                screen.blit(sheep.image,(sheep.x1,sheep.y1))
            for sheep in self.sheeplist:
                sheep.move()
            remtime=abs(6-(time.time()-start))+1
            fontsurf=self.font.render(str(int(remtime)),True,(255,0,0))
            screen.blit(fontsurf,(10,10))
            pygame.display.flip()
            time.sleep(0.02)
            if self.sheeplist==[]:
                break
            
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
        else:
            screen.blit(pygame.image.load('youlose.png').convert(),(100,650))
            pygame.display.flip()
            time.sleep(2)
            screen.blit(self.blackbar,(100,650))
            writescore(self.score)
            begin()
                            
        screen.blit(self.blackbar,(100,650))
        screen.blit(self.winimg,(100,650))
        self.score+=1
        pygame.display.flip()
        time.sleep(1.5)
        screen.blit(self.blackbar,(100,650))
        pygame.display.flip()
      

class Vision:
    
    class Fish:
        def __init__(self,isTarget=False):
            self.image=pygame.image.load('fish.png').convert()
            self.image.set_colorkey((0,0,0))
            self.image1=pygame.image.load('fish.png').convert()
            self.image1.set_colorkey((0,0,0))
            self.image2=pygame.transform.flip(self.image1,1,0)
            self.isTarget=isTarget
            self.x1=random.randrange(500)
            self.y1=random.randrange(500)
            self.xv=random.choice([1,2])*random.choice([1,-1])
            self.yv=random.choice([1,2])*random.choice([1,-1])

        def move(self):
            if self.xv<0:
                self.image=self.image1
            else:
                self.image=self.image2
            self.x1=self.x1+self.xv
            self.y1=self.y1+self.yv
            if 650<=self.x1 or self.x1<=0:
                self.xv=-self.xv
            if 550<=self.y1 or self.y1<=0:
                self.yv=-self.yv
    
    def __init__(self):
        self.score=0
        pygame.font.init()
        font=pygame.font.SysFont('comicsansms',25)
        self.textsurf=font.render('Click on the fishes you were spying on',1,(255,201,14))
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
            
        self.gameloop()
        self.score+=1
        self.fishno+=1
        self.noise+=1


    def gameloop(self):
        caught=0
        correctfish,wrongfish=0,0
        start=time.time()
        while time.time()-start<=8:
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if 0<=event.pos[0]<=100 and 650<=event.pos[1]<=700:
                        begin()
                elif event.type==pygame.QUIT:
                    pygame.quit()
            for fish in self.fishlist:
                fish.move()
            screen.blit((self.background),(0,0))
            for fish in self.fishlist:
                screen.blit(fish.image,(fish.x1,fish.y1))
            pygame.display.flip()
            time.sleep(0.02)
        flag=True
        screen.blit(self.textsurf,(150,660))
        pygame.display.flip()
        while flag:
            for event in pygame.event.get():
                if correctfish+wrongfish==self.fishno:
                    flag=False
                    break
                if event.type==pygame.QUIT:
                    begin()
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    pos=event.pos
                    if 0<=event.pos[0]<=100 and 650<=event.pos[1]<=700:
                        begin()
                    elif 0<=event.pos[1]<=600:
                        xp,yp=pos[0],pos[1]
                        for fish in self.fishlist:
                            x1=fish.x1
                            x2=x1+50
                            y1=fish.y1
                            y2=y1+50
                            if x1<xp<x2 and y1<yp<y2:
                                if fish.isTarget:
                                    if not fish.isTarget==2:
                                        correctfish+=1
                                        fish.isTarget=2
                                else:
                                    wrongfish+=1
                                break
                            
        print correctfish
        print wrongfish
        font=pygame.font.SysFont('comicsansms',30)
        fontsurf=font.render('Correct:'+str(correctfish)+'  Wrong:'+str(wrongfish),True,(255,201,14))
        screen.blit(self.blackbar,(100,650))
        screen.blit(fontsurf,(100,660))
        pygame.display.flip()
        time.sleep(1.5)
        screen.blit(self.blackbar,(100,650))
        pygame.display.flip()
        if correctfish<wrongfish:
            screen.blit(pygame.image.load('youlose.png').convert(),(100,650))
            pygame.display.flip()
            time.sleep(2)
            screen.blit(self.blackbar,(100,650))
            writescore(self.score)
            begin()
        
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
        self.score=0
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
                            self.score+=1
                            return
                        elif len(numstr)>=len(str(Calc.Number.total)) or int(numstr)!=Calc.Number.total:
                            screen.blit(pygame.image.load('youlose.png').convert(),(100,650))
                            pygame.display.flip()
                            time.sleep(2)
                            screen.blit(self.blackbar,(100,650))
                            writescore(self.score)
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
        return self.score


class Memory:
    def __init__(self):
        self.score=0
        self.limit=2
        self.start=True
        screen.blit(pygame.image.load('quit.png').convert(),(0,0))
        self.close=[[0,100],[650,700]]
        self.score=0
        a,b=200,200
        step=50
        self.posns=[]
        for i in range(7):
            a=(200+50*i)
            for j in range(7):
                b=200+50*j
                lis=[a,b]
                self.posns.append(lis)

        self.rects=[]
        for i in range(49):
            a=self.posns[i][0]-20
            b=self.posns[i][1]-20
            lis=[a,b]
            self.rects.append(lis)

        self.mainloop()
    
    def mainloop(self):
        
        screen.blit(pygame.image.load('mem.png').convert(),(0,0))
        if self.start:
            screen.blit(pygame.image.load('quit.png').convert(),(0,650))        
            screen.blit(pygame.image.load('prompt.png').convert(),(100,650))
        self.start=False
        pygame.display.flip()
        clickspot=0
        while 1:
            while not clickspot:
                for event in pygame.event.get():
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        if event.button==1:
                            clickspot=pygame.mouse.get_pos()
              
            if self.close[0][0]<clickspot[0]<self.close[0][1] and self.close[1][0]<clickspot[1]<self.close[1][1]:
                return
                    
            else:
                break
        
        screen.blit(pygame.image.load('blackbar.png').convert(),(100,650))
        pygame.display.flip()

        self.gameloop()
        
        
    def gameloop(self):
        abscorrectcnt=0
        messages=['','nice!','awesome!','woaaah!','dayymmm!','you\'re invincible!','keep going!']
        screen.blit(pygame.image.load('mem.png').convert(),(0,0))
        pygame.display.flip()
        self.selected=[]
        posns=[]
        print 1
        while 1:
            posn=random.choice(self.posns)
            if len(posns)==int(self.limit):
                break
            if posn in posns:
                continue
            posns.append(posn)
        for posn in posns:
            pygame.draw.rect(screen,(0,0,0),[posn[0]-20,posn[1]-20,40,40])
            time.sleep(0.5)
            pygame.display.flip()
            self.selected.append([posn[0]-20,posn[1]-20])
        time.sleep(0.5)
        screen.blit(pygame.image.load('meminplay.png').convert(),(0,0))
        pygame.display.flip()
        clickedrects=[]
        clickspot=0
        correctcnt=0
        start=time.time()
        pygame.event.pump()
        print 2
        while 1:
            for event in pygame.event.get():
                pass
            if clickspot:
                clickspot=0
            while not clickspot:
                for event in pygame.event.get():
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        if event.button==1:
                            clickspot=pygame.mouse.get_pos()
            if self.close[0][0]<clickspot[0]<self.close[0][1] and self.close[1][0]<clickspot[1]<self.close[1][1]:
                return
            for rect in self.rects:
                if rect[0]<clickspot[0]<rect[0]+40 and rect[1]<clickspot[1]<rect[1]+40:
                    if rect not in self.selected:
                        print 'wrong'
                        pygame.draw.rect(screen,(255,0,0),rect+[40,40])
                        screen.blit(pygame.image.load('youlose.png').convert(),(100,650))
                        pygame.display.flip()
                        time.sleep(1)
                        writescore(self.score)
                        begin()
                    elif rect in clickedrects:
                        print 'repeated'
                    elif rect in self.selected:
                        print 'correct'
                        pygame.draw.rect(screen,(0,255,0),rect+[40,40])
                        pygame.display.flip()
                        correctcnt+=1
                    clickedrects.append(rect)
            if correctcnt==self.limit:
                print 'win'
                self.score+=1
                abscorrectcnt+=1
                screen.blit(pygame.image.load('youwin.png').convert(),(100,650))
                pygame.display.flip()
                time.sleep(0.5)
                screen.blit(pygame.image.load('blackbar.png').convert(),(100,650))
                pygame.display.flip()
                if self.limit%3==0:
                    print 'zero'
                    font=pygame.font.SysFont('arialblack',50)
                    try:
                        fontsurf=font.render(messages[abscorrectcnt/4],True,(0,200,200))
                    except:
                        fontsurf=font.render(messages[6],True,(0,200,200))                        
                    x=325-(fontsurf.get_width()/2)+25
                    y=350-(fontsurf.get_height()/2)
                    screen.blit(fontsurf,(x,y))
                    pygame.display.flip()
                    time.sleep(1)
                self.limit+=1
                self.gameloop()


class start_screen:
    def __init__(self):
        
        self.bg=pygame.image.load('start.jpg').convert()

        self.startbtn=0
        self.helpbtn=1
        self.quitbtn=2
        self.optionsbtn=3

        self.buttons=([[230,450],[30,60]],[[110,310],[610,690]],[[320,370],[610,690]],[[380,430],[610,690]],[[50,110],[610,700]])

    def check_press(self):
        index=-1
        clickspot=pygame.mouse.get_pos()
        for button in self.buttons:
            index+=1
            if button[0][0]<clickspot[0]<button[0][1] and button[1][0]<clickspot[1]<button[1][1]:
                return index

class gameChooser:
    def __init__(self):
        screen.fill((0,0,0))
        img=pygame.image.load('games.png').convert()
        screen.blit(img,(0,0))
        screen.blit(pygame.image.load('close.png').convert(),(0,0))
        pygame.display.flip()
        self.mainloop()

    def mainloop(self):
        memory=[[180,500],[210,260]]
        vision=[[180,500],[270,310]]
        calc=[[180,500],[320,360]]
        react=[[180,500],[370,400]]
        close=[[0,50],[0,50]]
        
        clickspot=1
        while True:
            if clickspot:
                clickspot=0
            while 1:
                while not clickspot:
                    for event in pygame.event.get():
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            if event.button==1:
                                clickspot=pygame.mouse.get_pos()
                    
                if memory[0][0]<clickspot[0]<memory[0][1] and memory[1][0]<clickspot[1]<memory[1][1]:
                    score=Memory()
                    begin()
                    break
                elif vision[0][0]<clickspot[0]<vision[0][1] and vision[1][0]<clickspot[1]<vision[1][1]:
                    score=Vision()
                    begin()
                    break
                elif calc[0][0]<clickspot[0]<calc[0][1] and calc[1][0]<clickspot[1]<calc[1][1]:
                    score=Calc()
                    break
                elif react[0][0]<clickspot[0]<react[0][1] and react[1][0]<clickspot[1]<react[1][1]:
                    score=React()
                    break
                elif close[0][0]<clickspot[0]<close[0][1] and close[1][0]<clickspot[1]<close[1][1]:
                    begin()
                
                else:break


class HelpMenu:
    def __init__(self):
        screen.blit(pygame.image.load('close.png').convert(),(475,125))
        self.mainloop()
        
    def mainloop(self):
        imgs=[pygame.image.load('help1.png').convert(),pygame.image.load('help2.png').convert(),
        pygame.image.load('help3.png').convert(),pygame.image.load('help4.png').convert()]

        currentscr=0

        backward=[[30,100],[260,290]]
        forward=[[250,320],[260,290]]
        close=[[475,525],[125,175]]

        clickspot=1
        while True:
            if clickspot:
                clickspot=0
                screen.blit(imgs[currentscr],(175,175))
                pygame.display.flip()
            while 1:
                while not clickspot:
                    for event in pygame.event.get():
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            if event.button==1:
                                clickspot=pygame.mouse.get_pos()
                    
                if forward[0][0]<clickspot[0]-175<forward[0][1] and forward[1][0]<clickspot[1]-175<forward[1][1]:
                    if currentscr==3:
                        play()
                    else:currentscr+=1
                    break
                elif close[0][0]<clickspot[0]<close[0][1] and close[1][0]<clickspot[1]<close[1][1]:
                    begin()
                elif backward[0][0]<clickspot[0]-175<backward[0][1] and backward[1][0]<clickspot[1]-175<backward[1][1]:
                    if currentscr==0:
                        pass
                    else:currentscr-=1
                    break
                else:break

class HighScores:
    def __init__(self):
        screen.blit(pygame.image.load('close.png').convert(),(475,125))
        fp=open('scoredat.txt','r')
        filedat=fp.read().split(',')
        fp.close()
        self.font=pygame.font.SysFont('rockwellmtextrabold',50)
        self.textsurfs=[]
        for i in range(4):
            textsurf=self.font.render(filedat[i],True,(0,0,0))
            self.textsurfs.append(textsurf)
        self.mainloop()
        
    def mainloop(self):
        close=[[475,525],[125,175]]
        screen.blit(pygame.image.load('scores.png').convert(),(175,175))
        i=0
        for y in [10,90,170,250]:
            screen.blit(self.textsurfs[i],(240+175,180+y))
            i+=1
        pygame.display.flip()
        while 1:
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=event.pos
                    print pos
                    print close
                    if close[0][0]<pos[0]<close[0][1] and close[1][0]<pos[1]<close[1][1]:
                        begin()

def writescore(score):
    screen.blit(pygame.image.load('scoreboard.png'),(0,0))
    font=pygame.font.SysFont('rockwellmtextrabold',500)
    text=font.render(str(score),1,(255,201,14))
    screen.blit(text,(175,210))
    if score>5:
        screen.blit(pygame.image.load('happyface.png'),(600,600))
    pygame.display.flip()
    time.sleep(2)

def play():
    gameChooser()

def help_contents():
    HelpMenu()
           
def hiscores():
    HighScores()


def begin():
    global beginflag
    global scores
    if beginflag:
        scores=open('scoredat.txt','r').read().split(',')
        screen.blit(pygame.image.load('screen3.png').convert(),(0,0))
        pygame.display.flip()
        beginflag=False

        for i in range (0,750,5):
            if i%100==0:
                color=(255,0,0)
            pygame.draw.rect(screen,color,[0,600,i,10])
            pygame.display.flip()
            time.sleep(0.02)
        time.sleep(0.5)
    
    screencontents=start_screen()
    while 1:
        screen.blit(screencontents.bg,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN and event.key==pygame.K_q:
                pygame.quit()
            elif event.type==pygame.QUIT:
                pygame.quit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                clicked_at=screencontents.check_press()
                if clicked_at==0:
                    play()
                elif clicked_at==1:
                    help_contents()
                elif clicked_at==2:
                    hiscores()
                elif clicked_at==3:
                    pygame.quit()
        pygame.display.flip()
        time.sleep(0.1)


def test():
    ###################################################################################
    pass
beginflag=1
begin()



                
                               
        
