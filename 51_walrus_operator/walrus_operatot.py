# walrus operator :=

# new to python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)

# print(happy = True) # this does not work so we need to use the walrus operator so that we can asign the value to the operator in the print statement

print(happy := True) # if the value of the happy variable is set 5 it will be assigned the value of 5 from this print statement

print(happy)

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)


# the above code can also be written as the below using the walrus operator


foods = list()
while(food := input("What food do you like?: ")) != "quit":
    foods.append(food)
    
print(f"The list of the food which I like is {foods}")