# zip(*iterables) = aggregates elements from two or more iterables (lists, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element


usernames = ["Dude", "Bro", "Mister"]
passwords = ("StrongPassword", "12345", "Password123")
login_date = ["2024-01-01", "2024-01-02", "2024-01-03"]

users = zip(usernames, passwords, login_date)
for i in users:
    print(i)