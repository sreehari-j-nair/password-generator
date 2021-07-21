import random
from tkinter import *

window=Tk()
window.resizable(width=False,height=False)

head=Label(window , text="Password-Generator" , font="Impact" , fg="darkblue")
head.grid(row=0 , column=0 , columnspan=4)

screen=Entry(window , width=3 , borderwidth=3)
screen.grid(row=1 , column=0)

def generator():
        password=""
        num=screen.get()
        num=int(num)
        for i in range(num):
                letter=random.choice(alpha)
                password=password+letter
        genlabel=Label(window , text=password , font="Impact" , fg="darkblue")
        genlabel.grid(row=2 , column=0 , columnspan=4)

alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

generate=Button(window , text="Generate" , padx=10 , command=generator)
generate.grid(row=1 , column=1 , columnspan=3)
window.mainloop()