from tkinter import *


# labels = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file='/Users/ishan/Documents/BroCode/67_labels/photo.png')

label = Label(window,
              text="Hello World", 
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='top')


label.pack()

# label.place(x=0,y=0)




window.mainloop()