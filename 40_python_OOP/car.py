# this is a class which can be used as blueprint to create multiple objects 
# like car_1 & car_2 in oop_object.py

class Car: # class name should start with capital alphabet
    
    # make = None
    # model = None
    # year = None
    # color = None

    def __init__(self,make,model,year,color): # constructor
        self.make = make
        self.model = model
        self.year = year
        self.color = color 

    def drive(self): # self referes to the object using this method
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + "  is stopped")