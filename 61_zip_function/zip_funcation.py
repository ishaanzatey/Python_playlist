# zip(*iterables) = aggregates elements from two or more iterables (lists, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("StrongPassword", "12345", "Password123")

users = zip(usernames, passwords)
# users = list(zip(usernames, passwords)) # this is list of tuple
# users = dict(zip(usernames, passwords)) # this is dictionary of tuple
print(type(users))

# or you can assign the value to a variable like below


# we can cast the zip objects
# # you can convert the zip object to list, tuple and dictionary
# users_list = list(users)
# print(users_list)
# users_tuple = tuple(users)
# print(users_tuple)
# for i in users:
#     print(i)



# convertin the zip object to dictionary
users_dict = dict(zip(usernames, passwords))
print(type(users_dict))
for key,value in users_dict.items():
    print(key + " : " + value)
