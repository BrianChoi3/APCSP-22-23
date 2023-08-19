
def triangle(side1, side2, side3):

    perimeter = side1 + side2 + side3
    print(f"The perimeter of the triangle is {perimeter}")

def circle(radius):
    perimeter = 2 * 3.14 * radius
    print(f"The perimeter of the circle is {perimeter}")

def square(side):
    perimeter = side * 4
    print(f"The perimeter of the square is {perimeter}")

def rectangle(length, width):
    perimeter = (length + width) * 2
    print(f"The perimeter of the rectangle is {perimeter}")

def parallelogram(base, side):
    perimeter = (base + side) * 2
    print(f"The perimeter of the parallelogram is {perimeter}")

def trapezoid(base1, base2, side1, side2):
    perimeter = base1 + base2 + side1 + side2
    print(f"The perimeter of the trapezoid is {perimeter}")

shape = input("what shape would you like to calculate the perimeter of? ")
if shape == "triangle":
    side1 = float(input("What is the first side of the triangle? "))
    side2 = float(input("What is the second side of the triangle? "))
    side3 = float(input("What is the third side of the triangle? "))
    triangle(side1, side2, side3)
elif shape == "circle":
    radius = float(input("What is the radius of the circle? "))
    circle(radius)
elif shape == "square":
    side = float(input("What is the length of the side of the square? "))
    square(side)
elif shape == "rectangle":
    length = float(input("What is the length of the rectangle? "))
    width = float(input("What is the width of the rectangle? "))
    rectangle(length, width)
elif shape == "parallelogram":
    base = float(input("What is the base of the parallelogram? "))
    side = float(input("What is the side of the parallelogram? "))
    parallelogram(base, side)
elif shape == "trapezoid":
    base1 = float(input("What is the first base of the trapezoid? "))
    base2 = float(input("What is the second base of the trapezoid? "))
    side1 = float(input("What is the first side of the trapezoid? "))
    side2 = float(input("What is the second side of the trapezoid? "))
    trapezoid(base1, base2, side1, side2)
else:
    print("Error: Invalid Shape")
    exit()
    