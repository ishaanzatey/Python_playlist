# button = you click it, then it does stuff

from itertools import count
from tkinter import *


count = 0

def click():
    global count
    count += 1
    # print(count)
    print(f"You clicked the button! {count} time")

window = Tk()

photo = PhotoImage(file='/Users/ishan/Documents/BroCode/68_button_gui/photo.png')

button = Button(window, 
                text= "click me!",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='bottom')


button.pack()


window.mainloop()