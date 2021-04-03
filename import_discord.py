import discord
from discord.ext import commands
import numpy as np
import matplotlib.pyplot as plt
import os
import Random_Module #Module ที่ใช้ในการสุ่มไอเทม
import Plot_Module #Module ที่ใช้ในการพล็อตกราฟ

class Stack(object): #ระบบ stack ค่าของข้อมูลที่ส่งออกมา
    count4 = 0
    count5 = 0
    history_txt = '[History]\n'
    roll = 1
def __init__(self,i,count4,count5,history,roll,history_txt):
    self.count4 = count4 #เก็บจำนวนการการันตีของอไเทม 4 ดาวรอบถัดไป
    self.count5 = count5 #เก็บจำนวนการการันตีของอไเทม 5 ดาวรอบถัดไป
    self.history_txt = history_txt #เก็บประวัตการสุ่มไอเทม
    self.roll = roll #นับจำนวนรอบในการสุ่มไอเทม
def myhist(x):
    s = np.zeros(90)
    for i in x:
        s[i] += 1
    return s

bot = commands.Bot(command_prefix='!') #ใช้ ! ในการเป็น prefix ในการเรียกใช้งาน bot
@bot.event
async def on_ready() :  #หาก Bot พร้อมใช้งานจะแสดงผลว่า Bot Started!
    print("Bot Started!") 
@bot.event
async def on_message(message) : #ทำการตรวจข้อความที่เข้ามาการมี prefix ที่ใช้ในการเรียกใช้งาน Bot
    if message.content.lower().startswith('!compu'): #หากข้อความที่รับเข้ามาเริ่มต้นด้วย !compu ให้ปรับข้อความเป็น lower case ทั้งหมด
        text = message.content[len('!compu')+1:].split() #  
        command = text[0].lower() #ปรับข้อมูล text ใน array ตัวแรกให้เป็น lower case เก็บในตัวแปร command

        if command == 'help': #ถ้าสั่งคำสั่งว่า !compu help จะแสดง List คำสั่งระบบ Bot ทั้งหมดออกมา
            await message.channel.send('**Command**\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t**Funtion**\n**!compu gacha roll**\t\t\t\t\trolling Genshin Impact gacha 10 pull\n**!compu gacha history**\t\t\t showing rolling history\n**!compu gacha plot [Time]**\t plot graph how many 5 star was appear')

        elif command == 'gacha': #ถ้าสั่งคำสั่งว่า !compu gacha จะต้องใส่คำสั่งย่อยต่อท้าย
            sub_command = text[1].lower() #ปรับข้อมูล text ใน array ตัวที่ 2 ให้เป็น lower case เก็บในตัวแปร sub_command
            if sub_command == 'history': #ถ้าสั่งคำสั่งว่า !compu gacha history จะส่งไฟล์ text ประวัติการสุ่มออกมา
                f = open("History.txt","w+") #ทำการส้างไฟล์ History.txt ออกมา
                f.write(Stack.history_txt) #บันทึกค่าประวัติจากการสุ่มลงไปในไฟล์
                f.close() #ปิดไฟล์
                await message.channel.send(file=discord.File('History.txt')) #ให้ระบบ Bot ทำการส่งไฟล์ History.txt ออกมา
                os.remove(f"{__file__}History.txt") #ทำการลบไฟล์ History.txt เพื่อป้องกันการเขียนซ้อนทับกัน

            elif sub_command == 'roll': #ถ้าสั่งคำสั่งว่า !compu gacha roll จะแสดง List ไอเทมจากการสุ่มของ Random Module ออกมา
                get = '**[Gacha]**\n'
                gacha = Random_Module.gacha(10,Stack.count4,Stack.count5) #เรียกใช้ Random Module เพื่อใช้ในการสุ่มไอเทมจะนวน 10 ครั้ง
                Stack.count4 = int(gacha[1]) #เก็บจำนวนการการันตีของอไเทม 4 ดาวรอบถัดไป
                Stack.count5 = int(gacha[2]) #เก็บจำนวนการการันตีของอไเทม 5 ดาวรอบถัดไป
                for i in range(10): #ทำการ Stack ข้อความผลการสุ่มเพื่อใช้ในการแสดงผล
                    get += gacha[0][i]
                    Stack.history_txt += str(Stack.roll)+" | "+gacha[3][i]
                    Stack.roll += 1
                await message.channel.send(get) #แสดงผลการสุ่มไอเทมออกมา
            
            elif sub_command == 'plot': #ถ้าสั่งคำสั่งว่า !compu gacha plot [จำนวนรอบ] จะแสดงกราฟแท่งจากการจำลองอัตราการออกของไอเทม 5 ดาวออกมา
                sub2_command = int(text[2].lower()) #ปรับข้อความต่อการคำว่า plot เป็นตัวเลขเพื่อใช้เป็นจำนวนรอบในการสุ่ม
                s = []
                for i in range(sub2_command): #ทำการสุ่มจำนวน 90 ครั้งเป็นจำนวน N รอบ แล้วเก็บข้อมูลลงใน list s
                    a = Plot_Module.gacha(90,0,0)
                    for i in range(len(a)):
                        s.append(a[i])
                s.sort() #ทำการ sort ข้อมูลใน list s
                find90 = np.linspace(0,len(s),len(s))
                plt.figure(figsize = (16,8)) #ทำการกำหนดขนาดของกราฟ
                plt.xlabel('Roll (time)') #กำหนดให้แกน x เป็นจำนวนครั้งในการสุ่ม
                plt.ylabel('Get 5 star (time)') #กำหนดให้แกน y เป็นโอกาศในการได้รับไอเทม 5 ดาว
                plt.bar(range(90),(myhist(s)/sub2_command)*100) #พล็อตกราฟแท่งออกมา
                plt.savefig('Figure.png') #ทำการบันทึกการพล็อตกราฟเป็นไฟล์ Figure.png
                await message.channel.send(file=discord.File('Figure.png')) #ให้ระบบ Bot ทำการส่งไฟล์ Figure.png ออกมา
                os.remove("Figure.png") #ทำการลบไฟล์ Figure.png เพื่อทำการเคลียแคช

bot.run('ODIwMjM3OTI3MTA2ODcxMzc2.YEyQGQ.06LeOaOgwauYNhk4152ZnCSibKc') #Token ที่ใช้ในการ Run ระบบ Bot