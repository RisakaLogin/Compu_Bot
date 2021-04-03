import numpy as np
def gacha(num,x,y):
    star5 = ["Keqing","Mona","Qiqi","Diluc","Jean","Amos' Bow","Skyward Harp","Lost prayer to the Sacred Winds","Skyward Atlas","Primordial Jade Winged-Spear","Skyward Spine","Wolf's Gravestone","Skyward Pride","Skyward Blade","Aquila Favonia"]
            #list ไอเทม 5 ดาว

    star4 = ["Xinyan","Sucrose","Diona","Chongyun","Noelle","Bennett","Fischl","Ningguang","Xingqiu","Beidou","Xiangling","Amber","Razor","Kaeya","Barbara","Lisa","Rust","Sacrificial Bow","The Stringless","Favonius Warbow","Eye of Perception","Sacrificial Fragments","The Widsith","Favonius Codex","Favonius Lance","Dragon's Bane","Rainslasher","Sacrificial Greatsword","The Bell","Favonius Greatsword","Lion's Roar","Sacrificial Sword","The Flute","Favonius Sword"]
            #list ไอเทม 4 ดาว


    star3 = ["Slingshot","Sharpshooter's Oath","Raven Bow","Emerald Orb","Thrilling Tales of Dragon Slayers","Magic Guide","Black Tassel","Debate Club","Bloodtainted Greatsword","Ferrous Shadow","Skyrider Sword","Harbinger of Dawn","Cool Steel"]
            #list ไอเทม 3 ดาว

    rate4,rate5=0.051,0.006 #โอกาศในการได้รับไอเทม 4 ดาว และ 5 ดาว
    count4,count5=x,y #ตัวนับจำนวนการัตีของไอเทม 4 ดาว และ 5 ดาว
    reward4,reward5,reward=0,0,0
    get = [] #ทำการเก็บระดับ item ที่ได้ออกมาเป็น list
    stack = [] #ทำการเก็บข้อความที่ใช้ในการแสดงผลของไอเทมที่ทำการสุ่มได้
    stack_txt = [] #ทำการเก็บข้อความที่ใช้ในการส่งออกมาเป็นไฟล์ .txt ของไอเทมที่ทำการสุ่มได้
    for i in range(num): #ทำการสุ่มเป็นจำนวน num ครั้ง
        r=np.random.uniform(0,1) #random เลขตั่งแต่ 0 ถึง 1 เพื่อใช้ในการสุ่ม
        if(count5<75): #การจำนวนการสุ่มนั้นยั้งน้อยกว่า 75 ครั้ง จะทำกาใช้ rate ตามปกติ
            if(r<rate5):
                reward=5
                get.append(5)
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
        elif count5<89: #หากเลย 75 ครั้งมาแล้วจะเข้าสู่การใช้ pity rate(เรตช่วย)
            if r<0.324:
                reward=5
                get.append(5)
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
        else: #หาก 89 ครั้งยังไม่ได้ไอเทม 5 ดาวระบบจะทำการการันตีไอเทม 5 ดาวให้ในครั้งที่ 90
            reward=5
            get.append(5)
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
    for e in get: #ทำการดึงข้อมูลระดับไอเทมที่ได้ใน get มาแปลงเป็นข้อความแล้วทำการเก็บค่าลงใน stack และ stack_txt
        if e == 3: 
            item3 = np.random.choice(star3)
            findstar3 = "**[\u26053]** "+item3+"\n"
            findstar3_txt = "[3] "+item3+"\n"
            stack.append(findstar3)
            stack_txt.append(findstar3_txt)
        elif e == 4: 
            item4 = np.random.choice(star4)
            findstar4 = "**[\u26054]** "+item4+"\n"
            findstar4_txt = "[4] "+item4+"\n"
            stack.append(findstar4)
            stack_txt.append(findstar4_txt)
        else:
            item5 = np.random.choice(star5)
            findstar5 = "**[\u26055]** "+item5+"\n"
            findstar5_txt = "[5] "+item5+"\n"
            stack.append(findstar5)
            stack_txt.append(findstar5_txt)

    return stack,count4,count5,stack_txt #ทำการ return ค่าของ stack, จำนวนการันตี 4 ดาวครั้งถัดไป, จำนวนการันตี 5 ดาวครั้งถัดไป, stack_txt
