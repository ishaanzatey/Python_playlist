from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue") # in python we do not need to pass the self argument
car_2 = Car("Ford", "Mustang", 2022, "red") # these are objects

# car_1.wheels = 2 # this will only change the wheels for car_1 object
# print(car_1.wheels)
# print(car_2.wheels)
# print(Car.wheels) # this will print the class variable

Car.wheels = 2 # this will change the class variable for all objects
print(car_1.wheels)
print(car_2.wheels)