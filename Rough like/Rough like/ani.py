from Values import *
def ani():
        for men in char2:
            men.move()
            men.floor()
            men.dx*=0.95
            
        for man in char:
            man.move()
            man.floor()
            for a in range(1):
                if man.aa==0:
                    if man.dx==0:
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
                      
                        
                    if man.dx == -5 and man.y>460:
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
                        

                    if man.dx == 5 and man.y>460:
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


                if man.aa==0:
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
                if 1==1:
                    if man.quick==1:
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
                    
                        if man.a==30:
                            man.aa=0
                            man.a=0
                            fire=ent((1,1),size)
                            fire.dx=0
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
                        man.a+=1

#fireasdadasdasdasdf-----------------------------------------
                if man.aa==1:
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
                
            if man.aa==1 and man.w==1 and man.left==1 and man.a<12 and man.a>-1 and man.arrow==0:
                img=Lattack0
            if man.aa==1 and man.w==1 and man.left==1 and man.a<24 and man.a>12 and man.arrow==0:
                img=Lattack1

            pygame.draw.line(wn,red,(man.x+74,man.y+5),(man.x+106,man.y+5),8)
            pygame.draw.line(wn,green,(man.x+75,man.y+5),(man.x+105,man.y+5),6)
            pygame.draw.line(wn,green,(0,600),(1000,600),20)
