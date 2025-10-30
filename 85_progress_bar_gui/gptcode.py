from tkinter import *
from tkinter.ttk import *
import time

def start(progress=0):
    if progress <= 100:
        bar['value'] = progress
        percent.set(f"{progress}%")
        # Schedule next update after 1 second (1000 ms)
        window.after(1000, start, progress + 10)
    else:
        percent.set("Download Complete!")

window = Tk()
window.title("Progress Bar Example")

percent = StringVar()
percent.set("0%")

bar = Progressbar(window, orient=HORIZONTAL, length=300, mode='determinate')
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent)
percentLabel.pack()

button = Button(window, text="Download", command=start)
button.pack()

window.mainloop()
