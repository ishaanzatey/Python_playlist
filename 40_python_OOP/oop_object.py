from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue") # in python we do not need to pass the self argument
car_2 = Car("Ford", "Mustang", 2022, "red") # these are objects

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_1.drive()
car_2.stop()