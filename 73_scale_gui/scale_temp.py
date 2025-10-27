from email.mime import image
from tkinter import *

window = Tk()

hot_image = PhotoImage(file='/Users/ishan/Documents/BroCode/73_scale_gui/hot.png')
hotLabel = Label(image=hot_image)
hotLabel.pack()



def submit():
    print("The temprature is: "+ str(scale.get()) + " degree C")


scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,  # orientatin of scale can be horizantal or vertical
              font=('Consolas',20),
              tickinterval=10,  # this adds numeric indicators for value
            #   showvalue=0     # this will hide the current value, so we will need to print it to see the actual value to see the value
            #   resolution=5      # increment of slider by 5 degrees
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='#111111'
              )

# scale.set(50)   # will set the default value of the slider at 50 degree

# or can also be written as below

scale.set(((scale['from']-scale['to'])/2)+scale['to'])  # sets current value of the slider to the between number



scale.pack()


cold_image = PhotoImage(file='/Users/ishan/Documents/BroCode/73_scale_gui/cold.png')
coldLabel = Label(image=cold_image)
coldLabel.pack()


button = Button(window,text='submit',command=submit)
button.pack()


window.mainloop()