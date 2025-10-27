# functions = a block of code which only runs when it is called or invoked
#          = used to perform a single task
#          = reusable code
#          = helps to make code modular
#          = syntax: def function_name():

from os import name


# def hello(first_name,last_name):  #function definition
#     #pass
#     print('hello!', first_name, last_name)
#     print("have a nice day! ")


# hello("Bro","code")  #function call

# hello("bro") # only works if there is one parameter in function definition
# hello("dude")# only works if there is one parameter in function definition

def hello(first_name,last_name, age):  #function definition
    #pass
    print('hello!', first_name, last_name)
    print("Your age is " + str(age) + " have a nice day! ")


hello("Bro","code",21)  #function call



