age = 21
#age = age + 1
age += 1
print(age)
print(type(age))

# print("Your age is: " + age) #throws error TypeError: can only concatenate str (not "int") to str
print("Your age is: " + str(age)) #type casting
print("Your age is: ", age) #preferred way
print("Your age is: {}".format(age)) #formatted string

