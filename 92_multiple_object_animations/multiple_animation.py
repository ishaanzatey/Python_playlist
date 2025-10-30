from tkinter import *
from Ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()


volly_ball = Ball(canvas,0,0,75,3,2,"blue")
tennis_ball = Ball(canvas,0,0,10,1,3,"yellow")
basketball_ball = Ball(canvas,0,0,100,1,3,"orange")



while True:
    volly_ball.move()
    tennis_ball.move()
    basketball_ball.move()
    window.update()
    time.sleep(0.01)


window.mainloop()