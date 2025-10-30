from tkinter import *


def create_window():
    # there are two ways to create a window, one is Tk() and other is Toplevel()
    new_window = Tk()        # this is a new independent window
    # new_window = Toplevel()     # this will create a new window 'on top' of other window, which is linked to a 'bottom' window probably created with Tk()
    old_window.destroy()        # this will close or destroy the old window once the new window is created

old_window = Tk()

button = Button(old_window,text="create new window", command=create_window)
button.pack()

old_window.mainloop()