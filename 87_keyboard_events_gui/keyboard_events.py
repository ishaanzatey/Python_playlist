from tkinter import *


def doSomething(event):
    print("You pressed: " + event.keysym)   # the event.keysym will print the key which you are pressing
    label.config(text=event.keysym)

window = Tk()

# window.bind(event,function)
# window.bind("<Return>",doSomething)     # this will only return if you press enter
# window.bind("<q>",doSomething)          # this will return if you press q or press enter
window.bind("<Key>",doSomething)          # this will return when you press any key


label = Label(window,font=("Helvetica",100))
label.pack()


window.mainloop()