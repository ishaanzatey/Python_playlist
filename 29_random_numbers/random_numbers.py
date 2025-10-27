import random

x =random.randint(1,6) # prints a random integer between 1 and 6
y = random.random() # prints a random float between 0 and 1

my_list = ["rock","paper","scissors"]

cards = [2,3,4,5,6,7,8,9,10,"jack","queen","king","ace"]

random.shuffle(cards) # shuffles the list in place


z = random.choice(my_list) # prints a random item from the list

print(x)
print(f"{y:.2f}")
print(z)
print(cards) # prints the shuffled list