from tkinter import *


def doSomethingleft(event):
    print("you clicked a left mouse button" + " at the coordinate: "+ str(event.x)+ "," + str(event.y))

def doSomethingscroll(event):
    print("you are scrolling" + " at the coordinate: "+ str(event.x)+ "," + str(event.y))

def doSomethingright(event):
    print("you clicked a right mouse button" + " at the coordinate: "+ str(event.x)+ "," + str(event.y))


def releaseleft(event):
    print("you released a left mouse button" + " at the coordinate: "+ str(event.x)+ "," + str(event.y))

def releasescroll(event):
    print("you released scrolling" + " at the coordinate: "+ str(event.x)+ "," + str(event.y))

def releaseright(event):
    print("you released a right mouse button" + " at the coordinate: "+ str(event.x)+ "," + str(event.y))



window = Tk()

# window.bind("<Button-1>",doSomethingleft)      # left mouse click
# window.bind("<Button-2>",doSomethingright)     # middle scroll wheel
# window.bind("<Button-3>",doSomethingscroll)     # rigth mouse click
window.bind("<ButtonRelease>",releaseleft)      # triggers when we release button
window.bind("<ButtonRelease>",releaseright)     # triggers when we release button
window.bind("<ButtonRelease>",releasescroll)    # triggers when we release button
window.bind("<Enter>",doSomethingleft)          # when the mouse enetr the window
window.bind("<Leave>",doSomethingleft)          # when the mouse levaes the window
window.bind("<Motion>",doSomethingleft)         # tells the live location of the cursor on the window and outside the window


window.mainloop()