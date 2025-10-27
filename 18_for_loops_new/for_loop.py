# for loops = execute a block of code for a fixed number of times
# you can iterate over a range of numbers, a string, a list, and more
str = "Happy new year"
palindrome = []
print(str)

for x in str[::-1]:  # reverses the string
    print(x)
    palindrome.append(x)


for x in palindrome:
    print(x)
