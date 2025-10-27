from tkinter import *

# windows = serves as a container to hold or contain these widgets
# widgets = GUI elements: buttons, textboxes, labels, images

window = Tk()                                                                   # instantiate an instance of a window
window.geometry("420x420")                                                      # changes the windo dimension
window.title("Ishan's first GUI program")                                       # giving the title to the window

icon = PhotoImage(file="/Users/ishan/Documents/BroCode/66_GUI/photo.png")       # taking the icon
window.iconphoto(True,icon)                                                     # keeping the icon photo for the window
window.config(background="#5cfcff")                                           # setting background color of the window with hex colour format



window.mainloop()    # place window on computer screen, listen for events