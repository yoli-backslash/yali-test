import pygame
for a in range(1):
    
    exp0=pygame.image.load('png/exp0.png')

    exp0=pygame.transform.scale(exp0, (100,100))

    quick0=pygame.image.load('png/quick0.png')
    quick1=pygame.image.load('png/quick1.png')
    quick2=pygame.image.load('png/quick2.png')
    quick3=pygame.image.load('png/quick3.png')

    Rquick0 = pygame.transform.scale(quick0, (180, 110))
    Rquick1 = pygame.transform.scale(quick1, (180, 110))
    Rquick2 = pygame.transform.scale(quick2, (180, 110))
    Rquick3 = pygame.transform.scale(quick3, (180, 110))

    Lquick0 = pygame.transform.flip(Rquick0, True,False)
    Lquick1 = pygame.transform.flip(Rquick1, True,False)
    Lquick2 = pygame.transform.flip(Rquick2, True,False)
    Lquick3 = pygame.transform.flip(Rquick3, True,False)

    kick0=pygame.image.load('png/kick0.png')
    kick1=pygame.image.load('png/kick1.png')
    kick2=pygame.image.load('png/kick2.png')
    kick3=pygame.image.load('png/kick3.png')

    Rkick0 = pygame.transform.scale(kick0, (180, 110))
    Rkick1 = pygame.transform.scale(kick1, (180, 110))
    Rkick2 = pygame.transform.scale(kick2, (180, 110))
    Rkick3 = pygame.transform.scale(kick3, (180, 110))

    Lkick0 = pygame.transform.flip(Rkick0, True,False)
    Lkick1 = pygame.transform.flip(Rkick1, True,False)
    Lkick2 = pygame.transform.flip(Rkick2, True,False)
    Lkick3 = pygame.transform.flip(Rkick3, True,False)


    dr0=pygame.image.load('png/dr5.png')
    dr1=pygame.image.load('png/dr4.png')
    dr2=pygame.image.load('png/dr3.png')
    dr3=pygame.image.load('png/dr2.png')
    dr4=pygame.image.load('png/dr1.png')
    dr5=pygame.image.load('png/dr0.png')

    Rdr0 = pygame.transform.scale(dr0, (180, 110))
    Rdr1 = pygame.transform.scale(dr1, (180, 110))
    Rdr2 = pygame.transform.scale(dr2, (180, 110))
    Rdr3 = pygame.transform.scale(dr3, (180, 110))
    Rdr4 = pygame.transform.scale(dr4, (180, 110))
    Rdr5 = pygame.transform.scale(dr5, (180, 110))

    Ldr0 = pygame.transform.flip(Rdr0, True,False)
    Ldr1 = pygame.transform.flip(Rdr1, True,False)
    Ldr2 = pygame.transform.flip(Rdr2, True,False)
    Ldr3 = pygame.transform.flip(Rdr3, True,False)
    Ldr4 = pygame.transform.flip(Rdr4, True,False)

        
    walking0=pygame.image.load('png/walking0.png')
    walking1=pygame.image.load('png/walking1.png')
    walking2=pygame.image.load('png/walking2.png')
    walking3=pygame.image.load('png/walking3.png')
    walking4=pygame.image.load('png/walking4.png')
    walking5=pygame.image.load('png/walking5.png')
    walking6=pygame.image.load('png/walking6.png')
    print('hi')
    idle0=pygame.image.load('png/idle0.png')
    idle1=pygame.image.load('png/idle1.png')
    idle2=pygame.image.load('png/idle2.png')

    eb0=pygame.image.load('png/eb0.png')
    eb1=pygame.image.load('png/eb1.png')
    eb2=pygame.image.load('png/eb2.png')
    eb3=pygame.image.load('png/eb3.png')
    
    jump0=pygame.image.load('png/jump0.png')
    jump1=pygame.image.load('png/jump1.png')
    jump2=pygame.image.load('png/jump2.png')

    fire0=pygame.image.load('png/FIRE1.png')
    fire1=pygame.image.load('png/FIRE2.png')
    fire2=pygame.image.load('png/FIRE3.png')
    fire3=pygame.image.load('png/FIRE4.png')
    fire4=pygame.image.load('png/FIRE5.png')
    fire5=pygame.image.load('png/FIRE6.png')

    R2=pygame.image.load('png/R2.png')
    jump=pygame.image.load('png/jump.png')
    idle=pygame.image.load('png/idle.png')
    R1=pygame.image.load('png/R1.png')

    attack0=pygame.image.load('png/attack0.png')
    attack1=pygame.image.load('png/attack1.png')
    attack2=pygame.image.load('png/attack2.png')

    roll0=pygame.image.load('png/roll0.png')
    roll1=pygame.image.load('png/roll1.png')
    roll2=pygame.image.load('png/roll2.png')
    roll3=pygame.image.load('png/roll3.png')
    roll4=pygame.image.load('png/roll4.png')
    roll5=pygame.image.load('png/roll5.png')
    roll6=pygame.image.load('png/roll6.png')

    Reb0=pygame.transform.scale(eb0,(200,160))
    Reb1=pygame.transform.scale(eb1,(200,160))
    Reb2=pygame.transform.scale(eb2,(200,160))
    Reb3=pygame.transform.scale(eb3,(200,160))

    Leb0 = pygame.transform.flip(Reb0, True,False)
    Leb1 = pygame.transform.flip(Reb1, True,False)
    Leb2 = pygame.transform.flip(Reb2, True,False)
    Leb3 = pygame.transform.flip(Reb3, True,False)


    idle = pygame.transform.scale(idle, (100, 100))
    R1 = pygame.transform.scale(R1, (100, 100))

    Rattack0 = pygame.transform.scale(attack0, (180, 110))
    Rattack1 = pygame.transform.scale(attack1, (180, 110))
    Rattack2 = pygame.transform.scale(attack2, (180, 110))

    jump0 = pygame.transform.scale(jump0,(180,110))
    jump1 = pygame.transform.scale(jump1,(180,110))
    jump2 = pygame.transform.scale(jump2,(180,110))


    Lattack0 = pygame.transform.flip(Rattack0, True,False)
    Lattack1 = pygame.transform.flip(Rattack1, True,False)
    Lattack2 = pygame.transform.flip(Rattack2, True,False)

    Rroll0 = pygame.transform.scale(roll0, (180, 110))
    Rroll1 = pygame.transform.scale(roll1, (180, 110))
    Rroll2 = pygame.transform.scale(roll2, (180, 110))
    Rroll3 = pygame.transform.scale(roll3, (180, 110))
    Rroll4 = pygame.transform.scale(roll4, (180, 110))
    Rroll5 = pygame.transform.scale(roll5, (180, 110))
    Rroll6 = pygame.transform.scale(roll6, (180, 110))

    Rfire0 = pygame.transform.scale(fire0, (180, 110))
    Rfire1 = pygame.transform.scale(fire1, (180, 110))
    Rfire2 = pygame.transform.scale(fire2, (180, 110))
    Rfire3 = pygame.transform.scale(fire3, (180, 110))
    Rfire4 = pygame.transform.scale(fire4, (180, 110))
    Rfire5 = pygame.transform.scale(fire5, (180, 110))

    Lroll0 = pygame.transform.flip(Rroll0,True,False)
    Lroll1 = pygame.transform.flip(Rroll1,True,False)
    Lroll2 = pygame.transform.flip(Rroll2,True,False)
    Lroll3 = pygame.transform.flip(Rroll3,True,False)
    Lroll4 = pygame.transform.flip(Rroll4,True,False)
    Lroll5 = pygame.transform.flip(Rroll5,True,False)
    Lroll6 = pygame.transform.flip(Rroll6,True,False)

    Lfire0 = pygame.transform.flip(Rfire0,True,False)
    Lfire1 = pygame.transform.flip(Rfire1,True,False)
    Lfire2 = pygame.transform.flip(Rfire2,True,False)
    Lfire3 = pygame.transform.flip(Rfire3,True,False)
    Lfire4 = pygame.transform.flip(Rfire4,True,False)
    Lfire5 = pygame.transform.flip(Rfire5,True,False)



    walking0 = pygame.transform.scale(walking0, (180, 150))
    walking1 = pygame.transform.scale(walking1, (180, 150))
    walking2 = pygame.transform.scale(walking2, (180, 150))
    walking3 = pygame.transform.scale(walking3, (180, 150))
    walking4 = pygame.transform.scale(walking4, (180, 150))
    walking5 = pygame.transform.scale(walking5, (180, 150))
    walking6 = pygame.transform.scale(walking6, (180, 150))
    idle0 = pygame.transform.scale(idle0, (180, 150))
    idle1 = pygame.transform.scale(idle1, (180, 150))
    idle2 = pygame.transform.scale(idle2, (180, 150))
    img=idle1
    R2 = pygame.transform.scale(R2, (100, 100))
    jump = pygame.transform.scale(jump, (100, 100))

    
