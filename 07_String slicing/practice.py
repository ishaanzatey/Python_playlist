# validate user input
# 1. username should not be more that 12 characters
# 2. username should not contain any spaces
# 3. username should not contain any special characters

username = input("Enter your username: ")

if len(username) > 12:
    print("Username should not be more than 12 characters")
elif " " in username:
    print("Username should not contain any spaces")
elif not username.isalnum():  # checks if the string is alphanumeric
    print("Username should not contain any special characters")
else:
    print(f"welcome {username}")