# filter() = creates a collection of elements from an iterable for which a funcation returns true

# filter(function, iterable)

friends = [("Rachel" , 19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Ross", 20),
           ("Chandler", 21),
           ("Joey", 18)]

age = lambda data:data[1] >= 18
# age = lambda yoo:yoo[1] >= 21

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)


