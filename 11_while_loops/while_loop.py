# while loop = statement will execute its block of code, as long as its condition remains true

while 1 ==1:
    print("help i am stuck in a loop")  # infinite loop
    break  # stops the loop

name = ""
while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)

#or

name = None
while not name:
    name = input("Enter your name: ")


print("Hello " + name)