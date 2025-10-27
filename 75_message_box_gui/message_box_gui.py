from tkinter import *
from tkinter import messagebox      # this will import hte messagebox library


def click():
    # messagebox.showinfo(title='This is an info message box', message='You are a person')
    # messagebox.showwarning(title='WARNING!', message='You have a virus')
    # messagebox.showerror(title='Error', message='Something went wrong')



# # ask ok cancel 

    # if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing?'):
    #     print("You did a thing!")
    # else:
    #     print("You canceled the thing")


# # ask retry cancel
#     if messagebox.askretrycancel(title='ask retry cancel',message='Do you want to retry the thing?'):
#         print("You retired a thing!")
#     else:
#         print("You canceled the thing")


# # ask yes no
    # if messagebox.askyesno(title='ask yes no',message='Do you like cake?'):
    #     print("I like cake too!")
    # else:
    #     print("Why do you not like cake?")



# # ask question
    # answer = messagebox.askquestion(title='ask question',message='Do you like pie?')
    # if(answer == 'yes'):
    #     print("I like pie too!")
    # else:
    #     print("Why do you not like pie?")



# # ask yes no cancel
    answer = messagebox.askyesnocancel(title='Yes no cancel', message='Do you like to code?', icon='warning')
    if answer==True:
        print("You like to code")
    elif answer==False:
        print("They why are you in this repo?")
    else:
        print("Youhave dodged the question")



window = Tk()

button = Button(window,command=click,text='click me!')
button.pack()


window.mainloop()