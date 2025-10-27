# entry widget = textbox that accepts a single line of user input

from tkinter import *

window = Tk()

def submit():
    username = entry.get()
    print("Hello "+ username)
    # entry.config(state=DISABLED) # this will allow only one input and then it will disable the window

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)


entry = Entry(window,font=("Arial",50),
              fg="#00FF00",
              bg="black",
              show="*")
# entry.insert(0,'Spongbob') # just an example where the spongbob can be present while we run the program starting at index 0
# entry.config(state=DISABLED) # this will allow only one input and then it will disable the window
# entry.config(show="*") # this will help us to show the charachter, used where we usually type the password

entry.pack(side=LEFT)


submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)


delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)


backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)



window.mainloop()