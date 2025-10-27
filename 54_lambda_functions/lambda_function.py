# lambda function = function written in 1 line using lambda keyword
#                      accepts any number of arguments, but only has one expression
#                      (think of it as a shorthand function)
#                      (used often as an anonymous function / function without a name)
#                      (commonly used in higher order functions)


# lambda parameters:expression

# def double(x):
#     return x * 2

# print(double(5))

# above syntax can also be written as:

# double = lambda x:x * 2
# print(double(5))


# multiple arguments

multiply = lambda x,y: x*y
print(multiply(5,6))

add = lambda x,y,z: x+y+(10*z)
print(add(5,6,2))

fullname = lambda first_name , last_name : first_name + " " + last_name
print(fullname("Ishaan","Zatey"))

age_check = lambda age: True if age >= 18 else False
print(age_check(18))