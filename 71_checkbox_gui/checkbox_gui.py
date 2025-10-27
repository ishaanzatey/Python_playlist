from curses import window
from tkinter import *
from turtle import left

window = Tk()

def display():
    if(x.get()==1):
        print("You agree!")
    else:
        print("You don't agree :(")


x = IntVar()

photo = PhotoImage(file='/Users/ishan/Documents/BroCode/71_checkbox_gui/google.png')

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial',20),
                           fg='#00FF00',
                           bg='black',
                           activebackground='black',
                           activeforeground='#00FF00',
                           padx=25,
                           pady=10,
                           image=photo,
                           compound='left')

check_button.pack()


window.mainloop()