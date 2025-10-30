from re import L
from tkinter import *

def move_up(event):
    canvas.move(myimage,0,-10)

def move_down(event):
    canvas.move(myimage,0,10)

def move_left(event):
    canvas.move(myimage,-10,0)

def move_right(event):
    canvas.move(myimage,10,0)

window = Tk()

window.bind("<w>",move_up)
window.bind("<a>",move_left)
window.bind("<s>",move_down)
window.bind("<d>",move_right)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

photoimage = PhotoImage(file="/Users/ishan/Documents/BroCode/90_move_image_with_key_gui/race_car.png")
myimage = canvas.create_image(0,0,image=photoimage,anchor=NW)

window.mainloop()