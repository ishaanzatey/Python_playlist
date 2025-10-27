# list = used to store multiple items in a single variable
# ordered, changeable, allows duplicate values

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
print(food)
print(food[1])

for i in food:
    print(i)

print(food[0:3])  #slicing
print(len(food))  #length
food.append("ice cream")  #add to the end of the list
food.remove("hotdog")  #remove from the list
food.insert(0, "cake")  #insert at a specific index
food.pop()  #removes the last item
food.sort()  #sorts the list in alphabetical order
food.clear()  #clears the list
food2 = food.copy()  #copies the list
food.reverse()  #reverses the list
food.extend(["donut", "cookie"])  #adds multiple items to the end of the list

food.count("pizza")  #counts the number of occurrences of an item in the list
print(food.count("pizza"))

food.index("hotdog")  #returns the index of the first occurrence of an item in the list
print(food.index("hotdog"))

print(food)
print(food2)