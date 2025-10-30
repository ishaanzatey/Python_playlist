# frame = rectangular container to group and hold widgets

from tkinter import *


window = Tk()


frame = Frame(window,
              bg='pink',
              bd=5,     # this will set the border
              relief=SUNKEN)
# frame.pack(side=BOTTOM) # side = BOTTOM will set the frame at the bottom of the window
frame.place(x=100,y=100) # we can use this instead of the above to fix the frame at particular coordinate

Button(frame,text='W',font=("Consolas",25), width=3).pack(side=TOP)
Button(frame,text='A',font=("Consolas",25), width=3).pack(side=LEFT)
Button(frame,text='S',font=("Consolas",25), width=3).pack(side=LEFT)
Button(frame,text='D',font=("Consolas",25), width=3).pack(side=LEFT)


# button = Button(window,text='W',font=("Consolas",25), width=3)
# button.pack()

# # above lines can also be written as below in one line
# Button(window,text='W',font=("Consolas",25), width=3).pack(side=TOP)
# Button(window,text='A',font=("Consolas",25), width=3).pack(side=LEFT)
# Button(window,text='S',font=("Consolas",25), width=3).pack(side=LEFT)
# Button(window,text='D',font=("Consolas",25), width=3).pack(side=LEFT)


window.mainloop()