# list comperhension = a way to create a new list with less syntax
#                      can mimic certain lambda funcation, easier to read
#                      list = [expression for item in iterable]
#                      list = [expresusion for item in iterable if conditional]
#                      list = [expression (if/else) for item in iterable]



# # another example

students = [("Squiward" , 100) ,("Spongbob", 90), ("walter", 80) ,("bob", 70), ("Mr. Crab", 60), ("fish", 50), ("Mr.shark", 40), ("Donald", 30)]

passed_students = list(filter(lambda student: student[1] >= 60, students))
print(passed_students)

# or 

for name , grade in passed_students:
    print(f"{name} passed the exam with a grade of {grade}")



# # video example 

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]

# passed_students = list(filter(lambda student: student[1] >= 60, students))

# squares = [i * i for i in range(1,11)]  # list comprehension version 

# passed_students = [i for i in students if i >= 60] # list comprehension version

pass_students = [i if i>= 60 else "FAILED" for i in students] # list comprehension version with if/else

print(pass_students)


