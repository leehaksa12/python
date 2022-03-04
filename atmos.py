from hashlib import new
from tkinter import *
import tkinter.font

from tkinter import ttk

import pandas as pd
from IPython.display import display

atmos = Tk()
atmos.title('Meteological Observation Web ')

atmos.geometry("1440x900")
atmos.configure(bg = 'aqua')

#font 
font = tkinter.font.Font(family = '강원교육모두 Light', size = 25)
font1 = tkinter.font.Font(family = '강원교육모두 Light', size = 40)
font2 = tkinter.font.Font(family = '강원교육모두 Light', size = 10)
font3 = tkinter.font.Font(family = '강원교육모두 Light', size = 16)
font4 = tkinter.font.Font(family = '강원교육모두 Light', size = 20)
#font


#defination ASOS
def click_btn():
 
    stn = '속초(90)', '북춘천(93)', '광덕산(94)', '철원(95)', '대관령(100)', '춘천(101)', '북강릉(104)', '강릉(105)', '동해(106)', '원주(114)', '영월(121)', '인제(211)', '홍천(212)', '삼척(214)', '태백(216)', '정선군(217)'
    
    year = list(range(2000, 2020+1))
      
    #TopLevel
    toplevel = tkinter.Toplevel(atmos, bg = 'lavender')
    toplevel.geometry('400x400')
    
    label3 = Label(toplevel, text = '찾고 싶은 자료의 지점과 년도를 선택해주세요', font = font3, bg = 'lavender')
    label3.place(x = 30, y = 50)
    
    label4 = Label(toplevel, text = '강원도 관측소 입니다', font = font4, bg = 'lavender')
    label4.place(x = 35, y = 300)
    
    #combo box
    combo1 = ttk.Combobox(toplevel, values = stn, font = font4)
    
    print(dict(combo1))
    combo1.place(x = 30, y = 100)
    combo1.current(0)
    
    print(combo1.current(), combo1.get())
    
    combo2 = ttk.Combobox(toplevel, values = year, font = font4)
    
    print(dict(combo2))
    combo2.place(x = 30, y = 150)
    combo2.current(0)
    
    print(combo2.current(), combo2.get())
    
    btn3 = Button(toplevel, text = '찾기', font = font4, command = click_btn2)
    btn3.place(x = 30, y = 230)
    
def click_btn2():
    toplevel1 = tkinter.Toplevel(atmos)
    toplevel1.geometry('800x1200')
    
    asos = pd.read_csv('E:\python\ASOS_file.csv', encoding = 'euc-kr')
    display(asos)
    
    
        
#Button
btn1 = Button(atmos, text = "AWS(자동기상관측)", padx = 30, pady = 30, font = font1,
              bg = 'indigo', fg = 'white', command = click_btn)
btn1.place(x = 150, y = 100)

btn2 = Button(atmos, text = 'ASOS(종관기상관측)', padx = 30, pady = 30, font = font1,
              bg = 'indigo', fg = 'white', command = click_btn)
btn2.place(x = 750, y = 100)

#Label
label1 = Label(atmos,
               text = 'AWS는 실시간 기상 측정 및 연산, 저장, 표출 등 모든 과정을 자동으로 처리하는 기상관측 장비이다. 현재 악기상 연속 감시를 위해 전국 539소로 구성되어 있으며 소규모의 악기상이 빈번히 발생함에 따라, 소규모 국지기상감시의 선도관측을 위한 도서지역과 관측공백지대인 산간등지에도 설치 운영중에 있다.',
               padx = 10, pady = 10, font = font, bg = 'aqua', fg = 'black', wraplength = 1200)
label1.place(x = 90, y = 400)

label2 = Label(atmos,
               text = 'ASOS는 종관 규모의 날씨를 파악하기 위하여 정해진 시각에 모든 관측소에서 실시하는 지상관측을 말한다. 주로 기상관서에 설치되고 전국 10개소에서 그 지역의 현재 기상 실시간 제공 및 기상예보에 활용하고 있다.',
               padx = 10, pady = 10, font = font, bg = 'aqua', fg = 'black', wraplength = 1000)
label2.place(x = 200, y = 600)

atmos.mainloop()