from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="/Users/ishan/Documents/BroCode/79_save_file(file_dialog)", # this is not neccessary but it will take this directory as initial directory
                                    defaultextension='.txt',  # this will only help us to save the file without any content
                                    filetypes=[("Text file",".txt"),
                                               ("HTML file",".html"),
                                               ("All files",".*")])  
    

    if file is None:        # this helps to not get the error if we cancel the saving of the file in the middle of the task
        return
    # filetext = str(text.get(1.0,END))                         # this is taking the text from the starting index to the end of the text
    # we can also take input from the user instead of using the above line where we will give the etxt in the consol window
    filetext = input("Enter some text I guess:")        # this will help to enter the text in the consol instead of the gui window popup
    file.write(filetext)                                      # this will help to add the text to the file
    file.close()

window = Tk()

button = Button(text='save',command=saveFile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()