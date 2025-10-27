# set = collection which is unordered and unindexed, no duplicate values
# set is faster than list or tuple

utensiles = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}


# utensiles.add("napkin")  #add item to set
# utensiles.remove("fork")  #remove item from set, raises error if item not found
# utensiles.discard("fork")  #remove item from set, does not raise error if item not found
# utensiles.clear()  #clears the set
#utensiles.update(dishes)  #add items from another set (or any iterable)
#dinner_table = utensiles.union(dishes)  #returns a new set with items from both sets

# print(utensiles.difference(dishes))  #items in utensiles but not in dishes
# print(utensiles.intersection(dishes))  #items in both sets


print(utensiles)
for x in utensiles:
    print(x)