# compound intrest calculator

principle = 0
rate = 0
time = 0


while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle amount should be greater than 0")


while rate <= 0:
    rate = float(input("Enter the rate of interest: ")) 
    if rate <= 0:
        print("Rate of interest should be greater than 0") 

while time <= 0:
    time = float(input("Enter the time in years: "))
    if rate <= 0:
        print("Time in years cant be less than or equal to zero") 


total = principle * pow((1 + rate/100), time)


print(f"Balance after {time} years: ${total:.2f}")
