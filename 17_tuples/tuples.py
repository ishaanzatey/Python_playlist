# tuple = collection which is ordered and unchangeable
# used to group together related data

student = ("Bro" , 21, "male")

# print(student.count("Bro"))
# print(student.index("male"))


for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here")

#student[1] = 23

#print(student) #tuples are immutable, you cannot change the values in a tuple