# sort() method = used with lists
# sort() function = used with iterables

# this is tuple of tuples

students = (("Squidward", "F", 21), 
            ("sandy", "A", 22), 
            ("Patrick", "D", 20), 
            ("Spongbob", "B", 19), 
            ("Mr.krabs", "C", 23))

age = lambda age:age[2]

sorted_students = sorted(students,key=age)
for i in sorted_students:
    print(i)