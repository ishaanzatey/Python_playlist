# index operator [] = access a sequence's element (string, list, tuple)

name = 'bro code!'

# if(name[0].islower()):
#     name = name.capitalize()

first_name = name[:3].upper()
last_name = name[4:].lower()
last_char = name[-1] # returns only the last character


print(first_name)
print(last_name)
print(last_char)