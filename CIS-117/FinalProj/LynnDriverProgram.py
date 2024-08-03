import LynnPythonFinalProj

    rectangle1 = Rectangle(3, 4)
    rectangle2 = Rectangle(4, 3)
    rectangle3 = Rectangle(5, 6)
    square1 = Square(2)
    square2 = Square(4)
    square3 = Square(4)
    circle1 = Circle(3)
    circle2 = Circle(5)
    cylinder1 = Cylinder(3, 5)
    cylinder2 = Cylinder(4, 6)
    cylinder3 = Cylinder(6, 4)
    cube1 = Cube(2)
    cube2 = Cube(3)

    shapeList = [
        rectangle1, rectangle2, rectangle3,
        square1, square2, square3,
        circle1, circle2,
        cylinder1, cylinder2, cylinder3,
        cube1, cube2
    ]

    print("*****PRINTING OUT THE TEXT REPRESENTATION, DESCRIPTION, AREA, AND PERIMETER/VOLUME OF EACH SHAPE")
    for shape in shapeList:
        print(shape.get_description())
        print(shape)
        if isinstance(shape, TwoDimensionalShape):
            print("\tArea:", shape.area())
            print("\tPerimeter:", shape.perimeter())
        elif isinstance(shape, ThreeDimensionalShape):
            print("\tArea:", shape.area())
            print("\tVolume:", shape.volume())
        print("")

    print("\n*****PRINTING ALL EQUAL, NON-ALIAS SHAPES")
    for firstShape in shapeList:
        for secondShape in shapeList:
            if firstShape is not secondShape and firstShape == secondShape:
                print(f"Equal Shapes Found:")
                print(f"\t{firstShape.get_description()}")
                print(f"\t{secondShape.get_description()}")

    print("\n*****PRINTING ALL CUBE/SQUARE COMBINATIONS WHERE THE SQUARE IS A SIDE FOR THE CUBE")
    for firstShape in shapeList:
        for secondShape in shapeList:
            if isinstance(firstShape, Cube) and isinstance(secondShape, Square):
                if firstShape.can_hold_square(secondShape):
                    print(f"Square-Cube Match Found: ")
                    print(f"\t{secondShape.get_description()}")
                    print(f"\t{firstShape.get_description()}")
                    
    print("\n*****PRINTING ALL CYLINDER/CIRCLE COMBINATIONS WHERE THE CIRCLE IS A TOP OR BOTTOM FOR THE CYLINDER")
    for firstShape in shapeList:
        for secondShape in shapeList:
            if isinstance(firstShape, Cylinder) and isinstance(secondShape, Circle):
                if firstShape.can_hold_circle(secondShape):
                    print(f"Square-Cube Match Found: ")
                    print(f"\t{secondShape.get_description()}")
                    print(f"\t{firstShape.get_description()}")

    # Extra credit: printing all combinations of two-dimensional shapes that can fit inside another
    def perimeter_can_fit_inside(shape1, shape2):
        return shape1.perimeter() < shape2.perimeter()

    print("\n*****PRINTING ALL COMBINATIONS OF TWO-DIMENSIONAL SHAPES THAT CAN FIT INSIDE ANOTHER")
    for firstShape in shapeList:
        for secondShape in shapeList:
            if isinstance(firstShape, TwoDimensionalShape) and isinstance(secondShape, TwoDimensionalShape):
                if firstShape.can_fit_inside(secondShape):
                    print(f"Nested Shapes Found:")
                    print(f"Outer: {secondShape.get_description()}")
                    print(f"Inner: {firstShape.get_description()}")
                    print("")
