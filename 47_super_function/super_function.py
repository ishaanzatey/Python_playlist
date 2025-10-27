# super() = Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used


class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        # self.height = height # we can mention the height as height is a method not used in the Square class
class Square(Rectangle):

    def __init__(self,length,width):
        # self.length = length
        # self.width = width # we dont need these 2 functions as we have mentioned this in the super class
        super().__init__(length,width)

    def area(self):
        return self.length * self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        # self.length = length
        # self.width = width    # self.width and self.length these are replaced with the super class
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height
    

square = Square(3,3)
cube = Cube(3,3,3)

print(square.area())
print(cube.volume())