from Values import *

arrows=[]   

#Main game-----------------------------------------------
def game():

    global img
    fireball=False
    attack=False
    crashed=False
    fuck=True
    for man in char:
        man.ww=0
        man.wr=0
        man.wl=0
        man.kick=0
    for men in char:
        men.img=Reb0
    while not crashed:
        for event in pygame.event.get(): #get keypress
            if event.type == pygame.quit:
                crashed = True #breakes the loop
            for man in char:
                

                if event.type==pygame.KEYDOWN:#if key is pressed
                    if event.key== pygame.K_g and man.y>460 or man.y>230 and man.y<240 and man.x>140 and man.x<740 and event.key== pygame.K_g:
                        man.arrow=1
                        man.dy=10
                        if man.right==1:
                            man.dx=4
                        elif man.left==1:
                            man.dx=-4
                    if event.key==pygame.K_j and man.arrow==0 and man.kick==0:
                        man.kick=1
                    if event.key ==pygame.K_a and man.arrow==0:#left arrow
                        man.dx=-5
                        man.left=1
                        man.right=0
                        man.wl=1
                        man.wr=0
                        img = pygame.transform.flip(img, True,False)
                    elif event.key==pygame.K_d and man.arrow==0:
                        man.dx=5
                        man.wr=1
                        man.wl=0
                        man.left=0
                        man.right=1
                    if event.key==pygame.K_w and man.y>460 and man.arrow==0 or event.key==pygame.K_w and man.y>230 and man.y<240 and man.x>140 and man.x<740 and man.arrow==0:
                        man.dy=8
                    if event.key==pygame.K_1:
                        man.w=1
                    if event.key==pygame.K_2:
                        man.w=2
                    if event.key==pygame.K_3:
                        man.w=3
                    if event.key==pygame.K_4:
                        man.w=4
                    if event.key==pygame.K_5:
                        man.w=5
                    if event.key==pygame.K_k and man.roll==0 and man.w==5 and man.arrow==0:
                         man.ww=5
                    if event.key==pygame.K_k and man.roll==0 and man.w==4 and man.arrow==0:
                         man.ww=4
                    if event.key==pygame.K_k and man.roll==0 and man.w==3 and man.arrow==0:
                        man.ww=3
                        if man.right==1:
                            img=Rquick0
                        elif man.left==1:
                            img=Lquick0
                    if event.key==pygame.K_t:
                        if man.right==1:
                            boi=ent((man.x+100,man.y-10) , 8)
                            boi.dx=0
                            boi.dy=0
                            boi.q=0
                            boi.hp=40
                            boi.img=Reb0
                            boi.a=-1
                            boi.right=1
                            boi.left=0
                            char2.append(boi)
                        if man.left==1:
                            boi=ent((man.x-100,man.y-10) , 8)
                            boi.dx=0
                            boi.dy=0
                            boi.q=0
                            boi.hp=40
                            boi.img=Reb0
                            boi.a=-1
                            boi.right=1
                            boi.left=0
                            char2.append(boi)
                            
                    if event.key==pygame.K_k and man.roll==0 and man.w==1 and man.arrow==0:
                        if man.right==1:
                            img=Rattack0
                        elif man.left==1:
                            img=Lattack0
                        man.aa=1
                    if event.key==pygame.K_k and man.roll==0 and man.w==2 and man.arrow==0:
                        man.aa=1
                    if event.key==pygame.K_s and man.arrow==0:
                        man.roll=1
                if event.type==pygame.KEYUP:#if key is unpressed
                    if event.key == pygame.K_d or event.key == pygame.K_a:
                        if man.arrow==0:
                            man.dx=0
                            man.wr=0
                            man.wl=0
                    if event.key==pygame.K_k and man.w==1 and man.arrow==0:
                        man.a=0
                        man.aa=0
                        img=idle1
                    #if event.key == pygame.K_UP:
                    
                        
                







        wn.fill(white)#fills screen with color
        wn.blit(papa,(0,0))
        
        for men in char2:
            men.x+=men.dx
            
            
            men.dx*=0.95
            men.q+=1
            men.a+=1
            if men.a==0:
                if men.right==1:
                    men.img=Reb0
                elif men.left==1:
                    men.img=Leb0

            if men.a<9:
                for man in char:
                    dist(man,men)
                    if men.dis<60:
                        if men.left==1 and men.x>man.x:
                            man.dx=-8
                            man.hp-=1
                            man.hit=True
                            man.dy=1
                        elif men.right==1 and man.x>men.x:
                            man.dx=8
                            man.hp-=1
                            man.hit=True
                            man.dy=1
            if men.a==9:
                if men.right==1:
                    men.img=Reb1
                elif men.left==1:
                    men.img=Leb1
            if men.a>18:
                if men.right==1:
                    men.img=Reb2
                elif men.left==1:
                    men.img=Leb2
            if men.a==27:
                men.a=-9
                if men.right==1:
                    men.img=Reb3
                elif men.left==1:
                    men.img=Leb3
                    
            if men.x>880:
                men.q=-200
                men.x=870
            elif men.q==300:
                men.q=-300
            elif men.q>0:
                men.dx=0.8
                men.right=1
                men.left=0
            elif men.q<0:
                men.dx=-0.8
                men.right=0
                men.left=1
            wn.blit(men.img,(men.x,men.y-10))
            
        for man in char:
            man.move()
            man.floor()

            if man.kick==1:
                if man.right==1:
                    man.dx=1
                elif man.left==1:
                    man.dx=-1
                if man.a==0:
                    if man.right==1:
                        img=Rkick0
                    elif man.left==1:
                        img=Lkick0
                if man.a==9:
                    if man.right==1:
                        img=Rkick1
                    elif man.left==1:
                        img=Lkick1
                if man.a==18:
                    if man.right==1:
                        img=Rkick2
                    elif man.left==1:
                        img=Lkick2
                if man.a>27 and man.a <40:
                    for men in char2:
                        dist(men,man)
                    if man.right==1:
                        img=Rkick3
                        if man.dis<50 and men.x>man.x:
                            men.hp-=0.3
                            men.dx=1
                            men.dy=1
                            men.x+=8
                    elif man.left==1:
                        img=Lkick3
                        if man.dis<50 and man.x>men.x:
                            men.hp-=0.3
                            men.dx=-1
                            men.dy=1
                            men.x-=8

                if man.a>35 and man.a<40 or man.a>50:
                    man.dx=0
                    man.kick=0
                    man.a=0
                
                man.a+=1

            
            if man.x > 890 and man.y > 400:
                man.x = -50
            if man.x < -50 and man.y > 400:
                man.x = 890
            man.dx*=0.95
            if man.wr==1:
                man.dx=5
            elif man.wl==1:
                man.dx=-5
            if man.arrow==1:
                if man.right==1:
                    man.dx=3
                if man.left==1:
                    man.dx=-3
            for a in range(1):
                if man.aa==0:
                    if man.dx==0 and man.ww<3:
                        man.i+=1
                        if man.i==10:
                            img=idle1
                        if man.i==20:
                            img=idle0
                        if man.i==30:
                            img=idle1
                        if man.i==40:
                            img=idle2
                            man.i=0
                    
                    if man.q > 42:
                        man.q=1
                      
                        
                    if man.dx == -5 and man.y>460 or man.dx==-5 and man.y>230 and man.y<240 and man.x>140 and man.x<740:
                        man.q+=1
                        if man.q==6:
                            img=walking0
                            img = pygame.transform.flip(img, True,False)
                        if man.q==12:
                            img=walking1
                            img = pygame.transform.flip(img, True,False)
                        if man.q==18:
                            img=walking2
                            img = pygame.transform.flip(img, True,False)
                        if man.q==24:
                            img=walking3
                            img = pygame.transform.flip(img, True,False)
                        if man.q==30:
                            img=walking4
                            img = pygame.transform.flip(img, True,False)
                        if man.q==36:
                            img=walking5
                            img = pygame.transform.flip(img, True,False)
                        if man.q==42:
                            img=walking6
                            img = pygame.transform.flip(img, True,False)
                            man.q = 0
                        

                    if man.dx == 5 and man.y>460 or man.dx==5 and man.y>230 and man.y<240 and man.x>140 and man.x<740:
                        man.q+=1
                        if man.q==6:
                            img=walking0
                        if man.q==12:
                            img=walking1
                        if man.q==18:
                            img=walking2
                        if man.q==24:
                            img=walking3
                        if man.q==30:
                            img=walking4
                        if man.q==36:
                            img=walking5
                        if man.q==42:
                            img=walking6
                            man.q = 0
                            
                    if man.roll==1:
                        man.r+=1
                        if man.right==1:
                            man.dx=7
                            if man.r==6:
                                img=Rroll0
                            if man.r==12:
                                img=Rroll1
                            if man.r==18:
                                img=Rroll2
                            if man.r==24:
                                img=Rroll3
                            if man.r==30:
                                img=Rroll4
                            if man.r==36:
                                img=Rroll5
                            if man.r==42:
                                img=Rroll6
                                man.r=5
                                man.roll=0
                                man.dx=0


                            
                        elif man.left==1:
                            man.dx=-7
                            if man.r==6:
                                img=Lroll0
                            if man.r==12:
                                img=Lroll1
                            if man.r==18:
                                img=Lroll2
                            if man.r==24:
                                img=Lroll3
                            if man.r==30:
                                img=Lroll4
                            if man.r==36:
                                img=Lroll5
                            if man.r==42:
                                img=Lroll6
                                man.r=5
                                man.roll=0
                                man.dx=0



                if man.aa==0 and man.ww > 3:
                    man.a=-1
                
                for men in char2:
                            dist(men,man)
                            for arrow in arrows:
                                if arrow.y>500:
                                    arrows.remove(arrow)
                                dist(men,arrow)
                                if len(arrows)>0:
                                    dist(men,arrow)
                                    
                                    if arrow.dis<40:
                                        men.hp-=12
                                        arrows.remove(arrow)                                    
                            if len(proj)>0:
                                for ball in proj:
                                    dist(men,ball)
                                    if ball.i==3:
                                         if ball.dis<20:
                                            men.hp-=5
                                            ball.q=2
                                            for meen in char2:
                                                dist(ball,meen)
                                                if meen.dis<60:
                                                    meen.hp-=5
                                                
                                                
                                                    if ball.right==1 and men.x-ball.x>0:
                                                        #char2.remove(men)
                                                        #fuck=False
                                            
                                                        meen.dx=1
                                                        meen.dy=1
                                                    elif ball.left==1 and ball.x-men.x>0:
                                                        meen.dx=-1
                                                        meen.dy=1
                                            proj.remove(ball)
                                            
                                    if ball.i==2:
                                         if ball.dis<40:
                                            men.hp-=2
                                            ball.q=2
                                            
                                            if ball.right==1 and men.x-ball.x>0:
                                                #char2.remove(men)
                                                #fuck=False
                                    
                                                men.dx=1
                                                men.dy=1
                                            elif ball.left==1 and ball.x-men.x>0:
                                                men.dx=-1
                                                men.dy=1
                                            proj.remove(ball)
                                    if ball.i==1:
                                        if ball.dis<40 and ball.q==1:
                                            men.hp-=8
                                            ball.q=2
                                            
                                            if ball.right==1 and men.x-ball.x>0:
                                                #char2.remove(men)
                                                #fuck=False
                                    
                                                men.dx=2
                                                men.dy=2
                                            elif ball.left==1 and ball.x-men.x>0:
                                                men.dx=-2
                                                men.dy=2
                    
                if man.w==3:
                    if man.ww==3:
                        man.a+=1
                        #man.y+=25
                        man.aa=1
                        if man.a==0:
                            if man.right==1:
                                img=Rquick0
                            elif man.left==1:
                                img=Lquick0
                        if man.a==6:
                            if man.right==1:
                                img=Rquick1
                            elif man.left==1:
                                img=Lquick1
                        if man.a==12:
                            if man.right==1:
                                img=Rquick2
                            elif man.left==1:
                                img=Lquick2
                        if man.a==18:
                            img=idle1
                            man.aa=0
                            man.a=0
                            man.ww=0
                            fire=ent((1,1),size)
                            fire.dx=0
                            fire.i=2
                            fire.dy=0
                            fire.x=man.x
                            fire.y=man.y
                            if man.right==1:
                                fire.right=1
                                fire.left=0
                                fire.x+=20
                            elif man.left==1:
                                fire.right=0
                                fire.left=1
                                fire.x+=-20
                            proj.append(fire)
                            
                if man.w==5:
                    if man.ww==5:
                        man.a+=1
                        #man.y+=25
                        man.aa=1
                        if man.a==0:
                            if man.right==1:
                                img=Rpoison0
                            elif man.left==1:
                                img=Lpoison0
                        if man.a==6:
                            if man.right==1:
                                img=Rpoison1
                            elif man.left==1:
                                img=Lpoison1
                        if man.a==12:
                            if man.right==1:
                                img=Rpoison2
                            elif man.left==1:
                                img=Lpoison2
                        if man.a==18:
                            img=idle1
                            man.aa=0
                            man.a=0
                            man.ww=0
                            fire=ent((1,1),size)
                            fire.dx=0
                            fire.i=2
                            fire.dy=0
                            fire.x=man.x
                            fire.y=man.y
                            if man.right==1:
                                img=Rpoison3
                                fire.right=1
                                fire.left=0
                                fire.x+=20
                            elif man.left==1:
                                img=Lpoison3
                                fire.right=0
                                fire.left=1
                                fire.x+=-20
                            bul=ent((1,1),size)

                            bul.right=fire.right
                            bul.left=fire.left
                            bul.dx=0
                            bul.i=3
                            bul.dy=0
                            bul.x=fire.x
                            bul.y=fire.y+10

                            proj.append(bul)
                            
                if man.w==4:
                    if man.ww==4:
                        man.a+=1
                        #man.y+=25
                        man.aa=1
                        if man.a==0:
                            if man.right==1:
                                img=Rdual0
                            elif man.left==1:
                                img=Ldual0
                        if man.a==6:
                            if man.right==1:
                                img=Rdual1
                            elif man.left==1:
                                img=Ldual1
                        if man.a==12:
                            if man.right==1:
                                img=Rdual2
                            elif man.left==1:
                                img=Ldual2
                        if man.a==18:
                            img=idle1
                            man.aa=0
                            man.a=0
                            man.ww=0
                            fire=ent((1,1),size)
                            fire.dx=0
                            fire.i=2
                            fire.dy=0
                            fire.x=man.x
                            fire.y=man.y
                            if man.right==1:
                                img=Rdual3
                                fire.right=1
                                fire.left=0
                                fire.x+=20
                            elif man.left==1:
                                img=Ldual3
                                fire.right=0
                                fire.left=1
                                fire.x+=-20
                            bul=ent((1,1),size)

                            bul.right=fire.right
                            bul.left=fire.left
                            proj.append(fire)
                            bul.dx=0
                            bul.i=2
                            bul.dy=0
                            bul.x=fire.x
                            bul.y=fire.y+10

                            proj.append(bul)




                            
                        
                if man.aa==1:
    
                            #fire
                    if man.w==2:
                        if man.a==0:
                            if man.right==1:
                                img=Rfire0
                            elif man.left==1:
                                img=Lfire0
                        
                        if man.a==6:
                            if man.right==1:
                                img=Rfire1
                            elif man.left==1:
                                img=Lfire1
                        
                        if man.a==12:
                            if man.right==1:
                                img=Rfire2
                            elif man.left==1:
                                img=Lfire2
                        
                        if man.a==18:
                            if man.right==1:
                                img=Rfire3
                            elif man.left==1:
                                img=Lfire3
                        
                        if man.a==24:
                            if man.right==1:
                                img=Rfire4
                            elif man.left==1:
                                img=Lfire4
                        if man.a==30:
                            
                            man.aa=0
                            man.a=0
                            fire=ent((1,1),size)
                            fire.dx=0
                            fire.dy=0
                            fire.i=1
                            fire.x=man.x
                            fire.y=man.y
                            if man.right==1:
                                fire.right=1
                                fire.left=0
                                fire.x+=20
                            elif man.left==1:
                                fire.right=0
                                fire.left=1
                                fire.x+=-20
                            proj.append(fire)
                        man.a+=1
                        
                    
      

                    if man.w==1:
                        man.a+=1
                        
                       
                                
                              
                        if man.a<0 and man.dis<100 and fuck==True and man.w==1:
                            men.hp-=0.2
                            if man.right==1 and men.x-man.x>0:
                                    #char2.remove(men)
                                    #fuck=False
                                men.dx=1
                                men.dy=1
                            elif man.left==1 and man.x-men.x>0:
                                men.dx=-1
                                men.dy=1
                        if man.a==0:
                            if man.right==1:
                                img=Rattack0
                            elif man.left==1:
                                img=Lattack0
                        if man.a==12:
                            if man.right==1:
                                img=Rattack1
                            elif man.left==1:
                                img=Lattack1
                        if man.a==24:
                            
                            if man.right==1:
                                img=Rattack2
                            elif man.left==1:
                                img=Lattack2
                            man.a=-12

                if man.arrow==1:
                    if man.ar==0:
                        if man.right==1:
                            img=Rdr0
                        elif man.left==1:
                            img=Ldr0
                    man.ar+=1
                    if man.ar==15:
                        if man.right==1:
                            img=Rdr1
                        elif man.left==1:
                            img=Ldr1
                    if man.ar==30:
                        if man.right==1:
                            img=Rdr2
                        elif man.left==1:
                            img=Ldr2
                    if man.ar==45:
                        if man.right==1:
                            img=Rdr3
                        elif man.left==1:
                            img=Ldr3
                    if man.ar==60:
                        arr=ent((1,1),size)
                        arr.dx=0
                        arr.dy=-3
                        arr.x=man.x
                        arr.y=man.y
                        if man.right==1:
                            arr.right=1
                            arr.left=0
                            arr.x+=20
                        elif man.left==1:
                            arr.right=0
                            arr.left=1
                            arr.x+=-20
                        arrows.append(arr)

                        
                        if man.right==1:
                            img=Rdr4
                        elif man.left==1:
                            img=Ldr4
                    if man.ar==80:
                        img=idle1
                    if man.ar==100:
                        man.ar=0
                        man.dx=0
                        man.arrow=0
                    
            for arrow in arrows:
                arrow.move()
            if man.aa==1 and man.w==1 and man.left==1 and man.a<0 and man.arrow==0:
                img=Lattack2
            pygame.draw.line(wn,green,(200,340),(800,340),20)

                
            if man.aa==1 and man.w==1 and man.left==1 and man.a<12 and man.a>-1 and man.arrow==0:
                img=Lattack0
            if man.aa==1 and man.w==1 and man.left==1 and man.a<24 and man.a>12 and man.arrow==0:
                img=Lattack1

            pygame.draw.line(wn,red,(man.x+74,man.y+5),(man.x+106,man.y+5),8)
            if man.hp>50:
                pygame.draw.line(wn,green,(man.x+85+30-man.hp/2,man.y+5),(man.x+105+man.hp/2-40,man.y+5),6)
            else:
                char.remove(man)
            
            if man.aa==1 and man.ww<3 or man.roll==1 and man.ww<3:# or man.ww==3:
                wn.blit(img,(man.x,man.y+25)) #displays
            elif man.ww==3:
                wn.blit(img,(man.x,man.y+17))
          
            else:
                wn.blit(img,(man.x,man.y)) #displays
            for men in char2:
                men.y+=2
                if men.y>460 or (men.y>220 and men.y<240 and men.x<700 and men.x>120):
                    men.y-=2
                
                
                pygame.draw.line(wn,red,(men.x+84,men.y+5),(men.x+116,men.y+5),8)
                if men.hp>25:
                    pygame.draw.line(wn,green,(men.x+85+40-men.hp,men.y+5),(men.x+115+men.hp-40,men.y+5),6)
                else:
                    char2.remove(men)
                
            for arrow in arrows:
                wn.blit(Rdr5,(arrow.x,arrow.y))
            if len(proj)>0:
                for ball in proj:
                    if ball.x>900 or ball.x<-70:
                        proj.remove(ball)
                    if ball.i==1:
                        if ball.q>1:
                            wn.blit(exp0,(ball.x+40,ball.y))
                            ball.q+=1
                            if ball.q==20:
                                ball.q=-1
                                proj.remove(ball)
                                
                        elif ball.q==1:
                            if ball.x>900 or ball.x<-70 and len(proj)>0:
                                if ball==True:
                                    proj.remove(ball)
                            if ball.right==1:
                                wn.blit(Rfire5,(ball.x,ball.y))
                                ball.x+=3
                            if ball.left==1:
                                wn.blit(Lfire5,(ball.x,ball.y))
                                ball.x+=-3
                                
                    elif ball.i==3:
                        if ball.right==1:
                            wn.blit(Rpoison4,(ball.x,ball.y))
                            ball.x+=6
                        elif ball.left==1:
                            wn.blit(Lpoison4,(ball.x,ball.y))
                            ball.x-=6
                            
                    elif ball.i==2:
                        if ball.right==1:
                            wn.blit(Rquick3,(ball.x,ball.y))
                            ball.x+=6
                        elif ball.left==1:
                            wn.blit(Lquick3,(ball.x,ball.y))
                            ball.x-=6
                   
                    
        pygame.display.update() #update something
        clock.tick(70) #fps
game()
