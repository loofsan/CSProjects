from math import pi

class Shape:
    def get_description(self):
        raise NotImplementedError("Method Not Implemented")

    def __str__(self):
        raise NotImplementedError("Method Not Implemented")

    def __eq__(self, other):
        if isinstance(other, Shape):
            return (self.__str__() == other.__str__() and self.get_size() == other.get_size())
        return False

    def get_size(self):
        raise NotImplementedError("Method Not Implemented")
        
    def area(self):
        raise NotImplementedError("Method Not Implemented")

class TwoDimensionalShape(Shape):
    def perimeter(self):
        raise NotImplementedError("Method Not Implemented")
        
    def can_fit_inside(self):
        raise NotImplementedError("Method Not Implemented")


class ThreeDimensionalShape(Shape):
    def volume(self):
        raise NotImplementedError("Method Not Implemented")

class Rectangle(TwoDimensionalShape):
    def __init__(self, width, length):
        self.length = length
        self.width = width

    def area(self):
        return float(self.length * self.width)

    def perimeter(self):
        return float(2 * (self.length + self.width))

    def get_description(self):
        width, length = self.width, self.length
        return f'{"Rectangle":<13} Width: {width:<6} Height: {length:<6}'

    def __str__(self):
        return "Rectangle: A quadrilateral with four right angles"
    
    def get_size(self):
        return sorted([self.length, self.width])
        
    def can_fit_inside(self, other):
        if isinstance(other, Rectangle):
            return self.length <= other.length and self.width <= other.width
        elif isinstance(other, Square):
            return self.length <= other.length and self.width <= other.width
        elif isinstance(other, Circle):
            return self.length**2 + self.width**2 <= (2 * other.radius)**2

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def get_description(self):
        return f'{"Square":<13} Side Length: {self.length:<6}'

    def __str__(self):
        return f'{super().__str__()}\nSquare: A quadrilateral with four ' + 'equal sides and four equal angles'
        
    def can_fit_inside(self, other):
        if isinstance(other, Square):
            return self.length <= other.length
        elif isinstance(other, Rectangle):
            return self.length <= other.length and self.length <= other.width
        elif isinstance(other, Circle):
            return self.length**2 + self.length**2 <= (2 * other.radius)**2

class Circle(TwoDimensionalShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return float(self.radius * self.radius * pi)

    def perimeter(self):
        return float(2 * self.radius * pi)

    def get_description(self):
        return f'{"Circle":<13} Radius: {self.radius:<6}'

    def __str__(self):
        return "Circle: A closed plane curve every point of which is equidistant from a fixed point within the curve"

    def get_size(self):
        return [self.radius]
    
    def can_fit_inside(self, other):
        if isinstance(other, Circle):
            return self.radius <= other.radius
        elif isinstance(other, Rectangle):
            return self.radius * 2 <= min(other.length, other.width)
        elif isinstance(other, Square):
            return self.radius * 2 <= other.length

class Cylinder(ThreeDimensionalShape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        return float(2 * pi * self.radius * (self.radius + self.height))

    def volume(self):
        return float(pi * self.radius * self.radius * self.height)

    def get_description(self):
        return f'{"Cylinder":<13} Radius: {self.radius:<6} Height: {self.height:<6}'

    def __str__(self):
        return "Cylinder: A solid geometric figure with straight parallel sides and a circular or oval cross section"

    def get_size(self):
        return [self.radius, self.height]

    def can_hold_circle(self, circle):
        return self.radius == circle.radius

class Cube(ThreeDimensionalShape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return float(6 * self.side * self.side)

    def volume(self):
        return float(self.side**3)

    def get_description(self):
        return f'{"Cube":<13} Side Length: {self.side:<6}'

    def __str__(self):
        return "Cube: A three-dimensional solid object bounded by six square faces with three meeting at each vertex"

    def get_size(self):
        return [self.side]

    def can_hold_square(self, square):
        return self.side == square.length
