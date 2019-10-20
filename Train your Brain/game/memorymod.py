
import pygame,random,time
pygame.init()
screen=pygame.display.set_mode([700,700])



class Memory:
    def __init__(self):

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
        messages=['nice!','awesome!','woaaah!','dayymmm!','you\'re invincible!']
        screen.blit(pygame.image.load('mem.png').convert(),(0,0))
        pygame.display.flip()
        self.selected=[]
        posns=[]
        print 1
        while 1:
            posn=random.choice(self.posns)
            if len(posns)==5:
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
            pygame.event.pump()
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
                        pygame.event.pump()
                        return                        
                    elif rect in clickedrects:
                        print 'repeated'
                    elif rect in self.selected:
                        print 'correct'
                        pygame.draw.rect(screen,(0,255,0),rect+[40,40])
                        pygame.display.flip()
                        correctcnt+=1
                    clickedrects.append(rect)
            if correctcnt==5:
                print 'win'
                screen.blit(pygame.image.load('youwin.png').convert(),(100,650))
                pygame.display.flip()
                time.sleep(0.5)
                screen.blit(pygame.image.load('blackbar.png').convert(),(100,650))
                pygame.display.flip()
                abscorrectcnt+=1
                self.gameloop()
                if (abscorrectcnt)%4==0:
                    screen.blit((pygame.image.load('msg'+str(abscorrectcnt)+'.png').convert()),(350,350))

