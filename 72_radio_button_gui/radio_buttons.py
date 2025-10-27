# radio button = similar to checkbox, but you can only select one from a group

from operator import index
from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

window = Tk()

x = IntVar()

pizza_img = PhotoImage(file='/Users/ishan/Documents/BroCode/72_radio_button_gui/pizza_img.png')
hamburger_img = PhotoImage(file='/Users/ishan/Documents/BroCode/72_radio_button_gui/hamburger_img.png')
hotdog_img = PhotoImage(file='/Users/ishan/Documents/BroCode/72_radio_button_gui/hotdog_img.png')


foodImages = [pizza_img, hamburger_img, hotdog_img]

pizza_count = 0 
hamburger_count = 0
hotdog_count = 0

def order():
    global pizza_count, hamburger_count, hotdog_count
    if(x.get()==0):
        pizza_count += 1
        print(f"You ordered {pizza_count} pizza")
    elif(x.get()==1):
        hamburger_count += 1
        print(f"You ordered {hamburger_count} hamburger")
    elif(x.get()==2):
        hotdog_count += 1
        print(f"You ordered {hotdog_count} hotdog")
    else:
        print("huh?")



for i in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[i],    # adds text to radio buttons
                               variable=x,      # groups radiobuttons together if they share the same variable
                               value=i,         # this assigns each radiobutton a different value
                               padx=25,         # adds padding on x -axis
                               font=("Impact",20),
                               image = foodImages[i], # adds images to the radiobutton
                               compound='left', # adds images and text left side
                               #indicatoron=0,   # eleminates circle indicators
                               width= 375,       # this sets the width of the radio buttons
                               command=order    # this will set command of radio button to funcation
                               )         
    
    
    radio_button.pack(anchor=W)


window.mainloop()