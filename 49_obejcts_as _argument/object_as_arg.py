class Motorcycle:

    color = None


class Car:

    color = None 

def change_color(vehical,color): # car and color are the arguments and we dont neccerily want car we can also keep vehical
    
    vehical.color = color

# objects

bike_1 = Motorcycle()

car_1 = Car()
car_2 = Car()       
car_3 = Car()


change_color(car_1, "red")
change_color(car_2, "white")
change_color(car_3, "blue")
change_color(bike_1, "black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)

