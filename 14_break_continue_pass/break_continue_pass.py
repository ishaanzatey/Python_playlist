# loop control statements = change a loops execution from its normal sequence

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break


# phone_number = "123-456-789"

# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")  # end="" prevents new line after each print


for i in range(1,11):
    if i == 9:
        pass
    else:
        print(i)