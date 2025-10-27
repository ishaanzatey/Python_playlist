# listbox = A listing of selectable text items within its own container

from tkinter import *


def submit():
    food = []
    
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered:")
    for index in food:
        print(index)

    # print(listbox.get(listbox.curselection()))    # this only works with if we only want to select one option



def add():
    listbox.insert(listbox.size(),entryBox.get())


def delete():
    # listbox.delete(listbox.curselection())    # this only works for deleting one element
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size()+3)


window = Tk()

listbox = Listbox(window,
                  fg="black",
                  bg="#f7ffde",
                  font=('Constantia',35),
                  width=12,
                  selectmode=MULTIPLE
                  )
listbox.pack()


listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"toast")
listbox.insert(5,"salad")


listbox.config(height=listbox.size()+3)

entryBox = Entry(window)
entryBox.pack()


submitButton = Button(window,text='submit',command=submit)
submitButton.pack()


addButton = Button(window,text='add',command=add)
addButton.pack()



deleteButton = Button(window,text='delete',command=delete)
deleteButton.pack()


window.mainloop()
