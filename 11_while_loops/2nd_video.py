# while loops 

# food = input("What is your favorite food? ")
# food_list = []

# while food != "q":
#     print("I like " + food)
#     food_list.append(food)
#     food = input("What is your favorite food? ")

# print(f"Your favorite foods are: {food_list}")




# 2nd example

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Thank you! {num} is a valid number")