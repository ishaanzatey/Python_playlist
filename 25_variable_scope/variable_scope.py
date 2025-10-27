# scope = region that a variable is recognized
#         a variable is only available from inside the region it is created
#         a global and locally scoped versions of a variable can be creat

name = "Bro" # global scope (available iside and ourside the functions)

def display_name():
    name = "Code" # local scope (available only inside this function)
    print(name)

display_name()


def display_name():
    #name = "Code" # local scope (available only inside this function)
    print(name)

display_name()

print(name)