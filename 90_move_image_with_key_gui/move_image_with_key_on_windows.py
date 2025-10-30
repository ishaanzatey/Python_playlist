# moving a image on windows and canvas

from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)

def move_down(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()+10)

def move_left(event):
    label.place(x=label.winfo_x()-10,y=label.winfo_y())

def move_right(event):
    label.place(x=label.winfo_x()+10,y=label.winfo_y())



window = Tk()

window.geometry("500x500")

window.bind("<w>",move_up)
window.bind("<a>",move_left)
window.bind("<s>",move_down)
window.bind("<d>",move_right)


myimage = PhotoImage(file="/Users/ishan/Documents/BroCode/90_move_image_with_key_gui/race_car.png")
label = Label(window, image=myimage)
label.place(x=0,y=0)



window.mainloop()