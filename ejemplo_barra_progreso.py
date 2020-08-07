import sys
from tkinter import *
from tkinter import ttk
import time

myGui = Tk()

myGui.geometry('300x200')
myGui.title('Retro Code 80s')

style = ttk.Style()
style.configure("black.Horizontal.TProgressbar", background='black')
bar = ttk.Progressbar(myGui,orient ="horizontal",length = 200, style='black.Horizontal.TProgressbar',mode ="determinate")
bar["maximum"] = 100
bar.place(x=50,y=80)
Label(myGui, text = 'Retro Code').place(x=120,y=50)


for i in range(1,101,1):
    bar["value"] = i
    bar.update()
    time.sleep(0.5)
    Label(myGui, text = str(i)+' %').place(x=135,y=100)
    
myGui.mainloop()
