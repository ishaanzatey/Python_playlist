# str.format() = optional method that gives users
# more control when displaying output

number = 3.14159
# print("The number pi is {:.2f}".format(number)) # limit to 2 decimal places
# print("The number pi is {:10.2f}".format(number)) # limit to 2 decimal places and padding / spacing
# print("The number pi is {:<10.2f}".format(number)) # limit to 2 decimal places and left align
# print("The number pi is {:^10.2f}".format(number)) # limit to 2 decimal places and center align
# print("The number pi is {:>10.2f}".format(number)) # limit to 2 decimal places and right align
# print("The number pi is {:*^10.2f}".format(number)) # limit to 2 decimal places and center align with * as padding character


num = 1000000
print("the number is {:,}".format(num)) # add commas as thousand separator
print("the number is {:b}".format(num)) # makes the number binary
print("the number is {:o}".format(num)) # makes the number octal
print("the number is {:X}".format(num)) # makes the number hexadecimal (uppercase)
print("the number is {:E}".format(num)) # scientific notation (uppercase)