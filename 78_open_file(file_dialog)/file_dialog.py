from curses import window
from tkinter import *
from tkinter import filedialog


def openfile():
    filepath = filedialog.askopenfilename(initialdir="/Users/ishan/Documents/BroCode/78_open_file(file_dialog)/demo_file.txt",
                                          title="Open file okay?",
                                          filetypes=(("text files","*.txt"),
                                          ("all files","*.*")))
    # print(filepath)   # this will print the file path
    file = open(filepath,'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(text="Open", command=openfile)
button.pack()

window.mainloop()