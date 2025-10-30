from tkinter import *


def openFile():
    print("file has been opened!")

def saveFile():
    print("file has been saved!")

def cut():
    print("you cut some text!")

def copy():
    print("you copied some text!")

def paste():
    print("you pasted some text!")



window = Tk()

openImage = PhotoImage(file='/Users/ishan/Documents/BroCode/80_menubar_gui/file.png')
saveImage = PhotoImage(file='/Users/ishan/Documents/BroCode/80_menubar_gui/save.png')
exitImage = PhotoImage(file='/Users/ishan/Documents/BroCode/80_menubar_gui/exit.png')


menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0,font=("MC Boli",10)) # tearoff will remove the blank line if you have on the windows(niot seenon the mac)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile,image=openImage,compound='left')
fileMenu.add_command(label="Save", command=saveFile,image=saveImage,compound='left')
fileMenu.add_separator()            # this will show the opeion seperated by a line
fileMenu.add_command(label="Exit", command=quit,image=exitImage,compound='left')    # this will end the execution of the program as we just mentioned the quit as the quit is the keyword here


editMenu = Menu(menubar, tearoff=0,font=("MC Boli",10))
menubar.add_cascade(label='Edit',menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)


window.mainloop()