# slicing = creating a substring by extracting elements from another string
# indexing[] = gives access to a single character in a string
# slice() = gives access to a substring (a part of string)
# [start:stop:step]


name = "Bro Code"

first_name = name[:3]
last_name = name[4:]
funky_name = name[0::2]
reverse_name = name[::-1]

print(first_name + " " +last_name)
print(funky_name)
print(reverse_name)




name = input("Enter your name: ")

# result = len(name)
# result = name.find("o") # first occurrence of the character
# result = name.rfind("o") # last occurrence of the character
#result = name.capitalize() # capitalizes the first letter of the string
# result = name.upper() # converts the string to uppercase
# result = name.lower() # converts the string to lowercase
#result = name.isdigit() # checks if the string is a digit
#result = name.isalpha() # checks if the string is alphabetic and no spaces as
#result = name.count("o") # counts the number of occurrences of the character
#result = name.replace("-", "") # replaces the character with another character
result = name.count("-") # counts the number of occurrences of the substring


print(result)