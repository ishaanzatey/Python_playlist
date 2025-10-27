# keyword argument = argument preceded by an identifier when we pass it to a function
#                     The order of the arguments doesn't matter, unlike positional arguments
#                     Python knows the names of the arguments that our function receives


def hello(first,middle,last):
    print("Hello " + first + " " + middle + " " + last)

hello("Code","Bro","Dude")
hello(last="Dude",first="Code",middle="Bro")  #order doesn't matter