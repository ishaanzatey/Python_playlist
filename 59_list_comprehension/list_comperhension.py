# list comperhension = a way to create a new list with less syntax
#                      can mimic certain lambda funcation, easier to read
#                      list = [expression for item in iterable]
#                      list = [expresusion for item in iterable if conditional]
#                      list = [expression (if/else) for item in iterable]

squares = []                    # create an empty list
for i in range(1,11):           # create a for loop
    squares.append(i * i)     # define what to do in the loop
print(squares)                # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# the above code can also be written as:

# using the list to store the condition which will be printed in the final list

squares = [i * i for i in range(1,11)]  # list comprehension version    
print(squares)
