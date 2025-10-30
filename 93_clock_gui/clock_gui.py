from tkinter import *
from time import *


def update():
    time_string = strftime("%I:%M:%S %p")
    time_Label.config(text=time_string)

    day_string = strftime("%A")
    day_Label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_Label.config(text=date_string)


    window.after(1000,update)       # 1000 is in miliseconds, and the update is the function which is being called
    
    

window = Tk()

time_Label = Label(window, font=("Ariel",50),fg="#00FF00",bg="black")
time_Label.pack()

day_Label = Label(window, font=("Ariel",50),fg="yellow")
day_Label.pack()

date_Label = Label(window, font=("Ariel",50),fg="yellow")
date_Label.pack()


update()

window.mainloop()