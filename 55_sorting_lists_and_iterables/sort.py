# sort() method = used with lists
# sort() function = used with iterables

students_list = ["Squidward", "sandy", "Patrick", "Spongbob", "Mr.krabs"]

# students_list.sort() # sorts the list in the ascending order by default

# for i in students_list:
#     print(i)


# students_list.sort(reverse=True) # reverse and the other function only works with the sort() method for the lists and does not work with the tuple or sets and dictonaries

# for i in students_list:
#     print(i)


students_tuple = ("Squidward", "sandy", "Patrick", "Spongbob", "Mr.krabs")

sorted_students_tuple = sorted(students_tuple)  # sorts the tuple in the ascending order by default and returns a list
for i in sorted_students_tuple:
    print(i)


sorted_students_tuple = sorted(students_tuple, reverse=True)  # sorts the tuple in the descding order as the reverse = True argumentand returns a list
for i in sorted_students_tuple:
    print(i)