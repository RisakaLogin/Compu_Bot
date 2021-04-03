import numpy as np
import matplotlib.pyplot as plt
def gacha(num,x,y):
    star5 = ["Keqing","Mona","Qiqi","Diluc","Jean","Amos' Bow","Skyward Harp","Lost prayer to the Sacred Winds","Skyward Atlas"
         ,"Primordial Jade Winged-Spear","Skyward Spine","Wolf's Gravestone","Skyward Pride","Skyward Blade","Aquila Favonia"]

    star4 = ["Xinyan","Sucrose","Diona","Chongyun","Noelle","Bennett","Fischl","Ningguang","Xingqiu"
         ,"Beidou","Xiangling","Amber","Razor","Kaeya","Barbara","Lisa","Rust","Sacrificial Bow","The Stringless","Favonius Warbow"
         ,"Eye of Perception","Sacrificial Fragments","The Widsith","Favonius Codex","Favonius Lance","Dragon's Bane","Rainslasher"
         ,"Sacrificial Greatsword","The Bell","Favonius Greatsword","Lion's Roar","Sacrificial Sword","The Flute","Favonius Sword"]
    
    star3 = ["Slingshot","Sharpshooter's Oath","Raven Bow","Emerald Orb","Thrilling Tales of Dragon Slayers","Magic Guide","Black Tassel","Debate Club","Bloodtainted Greatsword"
         ,"Ferrous Shadow","Skyrider Sword","Harbinger of Dawn","Cool Steel"]
    
    rate4,rate5=0.051,0.006
    count4,count5=x,y
    reward4,reward5,reward=0,0,0
    get = []
    stack = []
    find5star = []
    for i in range(num):
        r=np.random.uniform(0,1)
        if(count5<75):
            if(r<rate5):
                reward=5
                get.append(5)
                find5star.append(i)
            else:
                if count4<8:
                    if r<rate5+rate4:
                        reward=4
                        get.append(4)
                    else:
                        reward=0
                        get.append(3)
                elif count4<9:
                    if r <rate5+0.511:
                        reward=4
                        get.append(4)
                    else:
                        reward=0
                        get.append(3)
                else:
                    reward=4
                    get.append(4)
        elif count5<89:
            if r<0.324:
                reward=5
                get.append(5)
                find5star.append(i)
            else:
                if count4<8:
                    if r<rate5+rate4:
                        reward=4
                        get.append(4)
                    else:
                        reward=0
                        get.append(3)
                elif count4<9:
                    if r <rate5+0.511:
                        reward=4
                        get.append(4)
                    else:
                        reward=0
                        get.append(3)
                else:
                    reward=4
                    get.append(4)
        else:
            reward=5
            get.append(5)
            find5star.append(i)
        if reward==5:
            reward5+=1
            count4+=1
            count5=0
        elif reward==4: 
            reward4+=1
            count5+=1
            count4=0
        else:
            count4+=1
            count5+=1

    for e in get:
        if e == 5:
            findstar5 = "**[★5]** "+np.random.choice(star5)+"\n"
            stack.append(findstar5)
    return find5star #นับเฉพาะไอเทม 5 ดาวแล้ว return ค่าออกมา
