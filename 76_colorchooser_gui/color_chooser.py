from curses import window
from tkinter import *
from tkinter import colorchooser
from turtle import title # colorchooser is the submodlule thats why its not imported from the first import


def click():
    color = colorchooser.askcolor() # assigns color to a variable
    # print(color)
    colorHex = color[1]             # assigns element at index 1 to a variable
    # print(colorHex)
    window.config(bg=colorHex)      # this will change the background color

    # # above code can be also written as
    # window.config(bg=colorchooser.askcolor()[1])    # change background color

window = Tk()
window.geometry("420x420")
button = Button(text='click me', command=click)

button.pack()


window.mainloop()