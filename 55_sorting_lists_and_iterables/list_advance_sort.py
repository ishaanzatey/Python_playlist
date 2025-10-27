# sort() method = used with lists
# sort() function = used with iterables

students = [("Squidward", "F", 21), 
            ("sandy", "A", 22), 
            ("Patrick", "D", 20), 
            ("Spongbob", "B", 19), 
            ("Mr.krabs", "C", 23)]


# # how can we sort the students based on their names, grades or age?

# # this will sort based on the names (1st element of the tuple)
# students.sort()

# for i in students:
#     print(i)



# # sorting the list using the grades(2nd element of the tuple)
# grade = lambda grades:grades[1]
# students.sort(key=grade)

# for i in students:
#     print(i)


# # if you want to sort based on the reverse we can add the reverse = True argument
# grade = lambda grades:grades[1]
# students.sort(key=grade, reverse = True) # it will help to print in reverse order

# for i in students:
#     print(i)


# sorting the list using the age (3rd element of the tuple)

age = lambda age:age[2]
students.sort(key=age, reverse=True) # if we add the reverse = True argument it will help to print in the reverse order

for i in students:
    print(i)

