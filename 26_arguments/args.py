# *args = parameters that will pack all arguments into a tuple
#       useful so that a function can accept a varying amount of arguments

# def add(num1,num2):
#     sum = num1 + num2
#     print(sum)

# print(add(1,2,3)) #error


def add(*args): # "*" is imaportant "args" can be any name
    sum = 0
    #args[0] = 10 #args is immutable and will throw error
    args = list(args) #convert to list to make it mutable
    args[9] = 1 # changes the 9th index to value 1 i.e 10 will become 1 in print(add(1,2,3,4,5,6,7,8,9,10))
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,8,9,10)) #works
