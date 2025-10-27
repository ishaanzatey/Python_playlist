#nested loop = a loop inside another loop 
# the inner loop will finish all of its iterations before finishing one iteration of the outer loop

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") # end="" prevents new line after each print
    print() # new line after each row)