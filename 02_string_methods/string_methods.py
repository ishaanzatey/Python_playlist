name = "bro code"
num = "123"

# print(len(name))  # length of string
# print(name.find("o"))  # find index of character
# print(name.capitalize())  # capitalize first letter
# print(name.upper())  # convert to uppercase
# print(name.lower())  # convert to lowercase
# print(num.isdigit())  # check if string is digit
# print(name.isalpha())  # check if string is alphabetic and no spcaces as well
# print(name.count("o"))  # count occurrences of character
# print(name.replace("o", "a"))  # replace character
# print(name*3)  # repeat string
# print(name[ : ])  # indexing
# print(name[0])  # first character
# print(name[-1])  # last character
# print(name[0:7:2])  # characters from index 0 to 6 with step 2
# print(name[ : : -1])  # reverse string
# print(name[7: : -1])  # characters from index 7 to start with step -1
# print(name[ : :-2])  # characters from end to start with step -2
# print(name[7:0:-2])  # characters from index 7 to 1 with step -2

# print(name.strip())  # remove leading and trailing whitespace
# print(name.split())  # split string into list of words
# print(name.startswith("bro code"))  # check if string starts with character
# print(name.endswith("e"))  # check if string ends with character
# print(name.swapcase())  # swap case of string (makes uppercase to lowercase and vice versa)
# print(name.title())  # capitalize first letter of each word
# print(name.center(12, "*"))  # center string with padding  
# print(name.rjust(12, "*"))  # right justify string with padding
# print(name.ljust(12, "*"))  # left justify string with padding
# print(name.encode())  # encode string to bytes
# print(name.isalnum())  # check if string is alphanumeric
# print(name.partition("o"))  # partition string into tuple
# print(name.removeprefix("bro"))  # remove prefix from string
# print(name.removesuffix("code"))  # remove suffix from string
# print(name.zfill(20))  # pad string with zeros on the left to a total length of 20
# print(name.expandtabs(tabsize=50))  # replace tabs with spaces (if any tabs are present)
# print(name.translate(str.maketrans("o", "a")))  # translate characters in string
# print(name.casefold())  # case insensitive version of lower() make everything lowercase
# print(name.isprintable())  # check if string is printable
# print(name.isidentifier())  # check if string is a valid identifier
# print(name.islower())  # check if all characters in string are lowercase
# print(name.isupper())  # check if all characters in string are uppercase
# print(name.istitle())  # check if string is title case (Bro Code is true, bro code is false)
print(name.join(["bro", "code"]))  # join list of strings with string as separator