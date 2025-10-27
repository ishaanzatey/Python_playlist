# str.format() = optional method that gives users
#                more control when displaying output

name = "Bro"

# print("Hello, my name is {} ".format(name)) # basic way of using format method"
# print("Hello, my name is {:10}. Nice to meet you".format(name)) # padding / spacing
# print("Hello, my name is {:>10}. Nice to meet you".format(name)) # right align
# print("Hello, my name is {:<10}. Nice to meet you".format(name)) # left align
# print("Hello, my name is {:^10}. Nice to meet you".format(name)) # center align
print("Hello, my name is {:*^11}. Nice to meet you".format(name)) # center align with * as padding character