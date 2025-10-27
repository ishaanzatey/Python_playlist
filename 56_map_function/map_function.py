# map() = applieas a function to each iteam in an iterable (list, tuple, etc.)

# map(function, iterable)

# from os import pathconf_names


store = [("shirt", 120.00),
         ("pathconf_names", 225.00),
         ("socks", 310.00),
         ("jacket", 220.00)]

to_euro = lambda data: (data[0], data[1]*0.0098)
to_dollars = lambda data: (data[0], data[1]*0.011)

print("Prices in euros are:")

store_euro = list(map(to_euro, store))

for i in store_euro:
    print(i)

print("\n\nPrices in dollars are:")

store_dollar = list(map(to_dollars, store))

for i in store_dollar:
    print(i)