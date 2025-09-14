# heirachical inheritance ith shap class parent of all other classes
# shap -> circle, square, rectangle, sphere, cube, triangle
# triangle -> equilateral, isosceles, scalene
# circle-> semicircle

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class toDShape(Shape):
    @abstractmethod
    def perimeter(self):
        pass
class threeDShape(Shape):
    @abstractmethod
    def volume(self):
        pass
    @abstractmethod
    def surface_area(self):
        pass
    @abstractmethod
    def density(self):
        pass
class Circle(toDShape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius
class Semicircle(Circle):
    def area(self):
        return (3.14 * self.radius * self.radius) / 2
    def perimeter(self):
        return 3.14 * self.radius + 2 * self.radius
class Square(toDShape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return 4 * self.side
class Rectangle(toDShape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
class Triangle(toDShape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def area(self):
        return 0.5 * self.base * self.height
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, (3**0.5 / 2) * side, side, side, side)
    def area(self):
        return (3**0.5 / 4) * self.side1 * self.side1
    def perimeter(self):
        return 3 * self.side1
class IsoscelesTriangle(Triangle):
    def __init__(self, equal_side, base):
        height = (equal_side**2 - (base**2 / 4))**0.5
        super().__init__(base, height, equal_side, equal_side, base)
    def area(self):
        return 0.5 * self.base * self.height
    def perimeter(self):
        return 2 * self.side1 + self.base
class ScaleneTriangle(Triangle):
    def __init__(self, side1, side2, side3):
        s = (side1 + side2 + side3) / 2
        height = (s * (s - side1) * (s - side2) * (s - side3))**0.5 * 2 / side1
        super().__init__(side1, height, side1, side2, side3)
    def area(self):
        return 0.5 * self.base * self.height
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
class Sphere(threeDShape):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    def area(self):
        return 4 * 3.14 * self.radius * self.radius
    def volume(self):
        return (4/3) * 3.14 * self.radius**3
    def surface_area(self):
        return 4 * 3.14 * self.radius * self.radius
    def density(self):
        return self.mass / self.volume()
class Cube(threeDShape):
    def __init__(self, side, mass):
        self.side = side
        self.mass = mass
    def area(self):
        return 6 * self.side * self.side
    def volume(self):
        return self.side**3
    def surface_area(self):
        return 6 * self.side * self.side
    def density(self):
        return self.mass / self.volume()
class Cuboid(threeDShape):
    def __init__(self, length, breadth, height, mass):
        self.length = length
        self.breadth = breadth
        self.height = height
        self.mass = mass
    def area(self):
        return 2 * (self.length * self.breadth + self.breadth * self.height + self.height * self.length)
    def volume(self):
        return self.length * self.breadth * self.height
    def surface_area(self):
        return 2 * (self.length * self.breadth + self.breadth * self.height + self.height * self.length)
    def density(self):
        return self.mass / self.volume()
# All objects
while True:
    print("1. Circle\n2. Semicircle\n3. Square\n4. Rectangle\n5. Equilateral Triangle\n6. Isosceles Triangle\n7. Scalene Triangle\n8. Sphere\n9. Cube\n10. Cuboid\n11. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        r = float(input("Enter radius of circle: "))
        circle = Circle(r)
        print("Area:", circle.area())
        print("Perimeter:", circle.perimeter())
    elif choice == 2:
        r = float(input("Enter radius of semicircle: "))
        semicircle = Semicircle(r)
        print("Area:", semicircle.area())
        print("Perimeter:", semicircle.perimeter())
    elif choice == 3:
        s = float(input("Enter side of square: "))
        square = Square(s)
        print("Area:", square.area())
        print("Perimeter:", square.perimeter())
    elif choice == 4:
        l = float(input("Enter length of rectangle: "))
        b = float(input("Enter breadth of rectangle: "))
        rectangle = Rectangle(l, b)
        print("Area:", rectangle.area())
        print("Perimeter:", rectangle.perimeter())
    elif choice == 5:
        s = float(input("Enter side of equilateral triangle: "))
        eq_triangle = EquilateralTriangle(s)
        print("Area:", eq_triangle.area())
        print("Perimeter:", eq_triangle.perimeter())
    elif choice == 6:
        es = float(input("Enter equal side of isosceles triangle: "))
        b = float(input("Enter base of isosceles triangle: "))
        iso_triangle = IsoscelesTriangle(es, b)
        print("Area:", iso_triangle.area())
        print("Perimeter:", iso_triangle.perimeter())
    elif choice == 7:
        s1 = float(input("Enter side 1 of scalene triangle: "))
        s2 = float(input("Enter side 2 of scalene triangle: "))
        s3 = float(input("Enter side 3 of scalene triangle: "))
        scal_triangle = ScaleneTriangle(s1, s2, s3)
        print("Area:", scal_triangle.area())
        print("Perimeter:", scal_triangle.perimeter())
    elif choice == 8:
        r = float(input("Enter radius of sphere: "))
        m = float(input("Enter mass of sphere: "))
        sphere = Sphere(r, m)
        print("Area:", sphere.area())
        print("Volume:", sphere.volume())
        print("Surface Area:", sphere.surface_area())
        print("Density:", sphere.density())
    elif choice == 9:
        s = float(input("Enter side of cube: "))
        m = float(input("Enter mass of cube: "))
        cube = Cube(s, m)
        print("Area:", cube.area())
        print("Volume:", cube.volume())
        print("Surface Area:", cube.surface_area())
        print("Density:", cube.density())
    elif choice == 10:
        l = float(input("Enter length of cuboid: "))
        b = float(input("Enter breadth of cuboid: "))
        h = float(input("Enter height of cuboid: "))
        m = float(input("Enter mass of cuboid: "))
        cuboid = Cuboid(l, b, h, m)
        print("Area:", cuboid.area())
        print("Volume:", cuboid.volume())
        print("Surface Area:", cuboid.surface_area())
        print("Density:", cuboid.density())
    elif choice == 11:
        break
    else:
        print("Invalid choice")
# polymorphism
'''def compute_area(shape):
    return shape.area()
def compute_perimeter(shape):
    return shape.perimeter()
def compute_volume(shape):
    return shape.volume()
def compute_surface_area(shape):
    return shape.surface_area()
def compute_density(shape):
    return shape.density()  
# Example usage of polymorphism
circle = Circle(5)
print("Circle Area (Polymorphism):", compute_area(circle))
print("Circle Perimeter (Polymorphism):", compute_perimeter(circle))
sphere = Sphere(5, 50)
print("Sphere Volume (Polymorphism):", compute_volume(sphere))
print("Sphere Surface Area (Polymorphism):", compute_surface_area(sphere))
print("Sphere Density (Polymorphism):", compute_density(sphere))
'''
