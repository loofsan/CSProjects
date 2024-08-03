from math import pi

class Shape:
    def getDescription(self):
        raise NotImplementedError("Method Not Implemented")

    def __str__(self):
        raise NotImplementedError("Method Not Implemented")

    def __eq__(self, other):
        if isinstance(other, Shape):
            return (self.__str__() == other.__str__() 
                    and self.get_size() == other.get_size())
        return False

    def get_size(self):
        raise NotImplementedError("Method Not Implemented")
    
    def area(self):
        raise NotImplementedError("Method Not Implemented")

class TwoDimensionalShape(Shape):
    def perimeter(self):
        raise NotImplementedError("Method Not Implemented")
    
    def perimeterCanFitInside(self, other):
        if (self.perimeter() > other.perimeter()):
            return True

class ThreeDimensionalShape(Shape):
    def volume(self):
        raise NotImplementedError("Method Not Implemented")
    
# ***Start of all the Two Dimensional Shapes Below***

class Rectangle(TwoDimensionalShape):
    def __init__(self, width, length):
        self.length = length
        self.width = width

    def area(self):
        return (self.length * self.width)

    def perimeter(self):
        return (2 * (self.length + self.width))

    def getDescription(self):
        return (f'{"Rectangle":<13} Width: {self.width:<6} Height: {self.length:<6}')

    def __str__(self):
        return (f'Rectangle: A quadrilateral with four right angles')
    
    def get_size(self):
        return sorted([self.length, self.width])
    
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def getDescription(self):
        return (f'{"Square":<13} Side Length: {self.length:<6}')

    def __str__(self):
        return (f'{super().__str__()}\nSquare: A quadrilateral with four ' + 
                'equal sides and four equal angles')

class Circle(TwoDimensionalShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius * self.radius * pi)

    def perimeter(self):
        return (2 * self.radius * pi)

    def getDescription(self):
        return (f"{'Circle':<13} Radius: {self.radius:<6}")

    def __str__(self):
        return ("Circle: A closed plane curve every point of which is " + 
                "equidistant from a fixed point within the curve")

    def get_size(self):
        return (self.radius)
    
# ***End of all the Two Dimensional Shapes Above***

# ***Start of all the Three Dimensional Shapes Below***

class Cylinder(ThreeDimensionalShape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        return (2 * pi * self.radius * (self.radius + self.height))

    def volume(self):
        return (pi * self.radius * self.radius * self.height)

    def getDescription(self):
        return (f'{"Cylinder":<13} Radius: {self.radius:<6} Height: {self.height:<6}')

    def __str__(self):
        return ("Cylinder: A solid geometric figure with straight " + 
                "parallel sides and a circular or oval cross section")

    def get_size(self):
        return (self.radius, self.height)

    def have_circle(self, circle):
        return self.radius == circle.radius
    
class Cube(ThreeDimensionalShape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return (6 * self.side * self.side)

    def volume(self):
        return (self.side**3)

    def getDescription(self):
        return (f"{'Cube':<13} Side Length: {self.side:<6}")

    def __str__(self):
        return (f"Cube: A three-dimensional solid object bounded by six " + 
                "square faces with three meeting at each vertex")

    def get_size(self):
        return (self.side)

    def have_square(self, square):
        return self.side == square.length
    
# ***End of all the Three Dimensional Shapes Above***
