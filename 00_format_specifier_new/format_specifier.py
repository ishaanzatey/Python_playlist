# format specifier = {value:flags} formatting of value based on what flasg are inserted

price1 = 33123.141
price2 = -8921231.213
price3 = 12.34

# print(f"Price 1 is {price1:.3f}")  # rounds to 2 decimal places
# print(f"Price 2 is {price2:.2f}")  # rounds to 2 decimal places
# print(f"Price 3 is {price3:.1f}")  # rounds to 1 decimal places


# print(f"Price 1 is {price1:4f}") 
# print(f"Price 2 is {price2:1f}")   
# print(f"Price 3 is {price3:1f}") 


# print(f"Price 1 is {price1:<10}") 
# print(f"Price 2 is {price2:<10}") 
# print(f"Price 3 is {price3:<10}") 

# print(f"Price 1 is {price1:>10}") 
# print(f"Price 2 is {price2:>10}")
# print(f"Price 3 is {price3:>10}") 

# print(f"Price 1 is {price1:^10}")  
# print(f"Price 2 is {price2:^10}") 
# print(f"Price 3 is {price3:^10}") 


print(f"Price 1 is {price1:+,.2f}") 
print(f"Price 2 is {price2:+,.2f}") 
print(f"Price 3 is {price3:+,.2f}") 

