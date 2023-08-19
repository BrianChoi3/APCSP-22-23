def triangle():
    base = float(input("What is the base of the triangle? "))
    height = float(input("What is the height of the triangle? "))
    area = base * height / 2
    print(f"The area of the triangle is {area}")

def circle():
    radius = float(input("What is the radius of the circle? "))
    area = 3.14 * radius ** 2
    print(f"The area of the circle is {area}")

def square():
    side = float(input("What is the length of the side of the square? "))
    area = side ** 2
    print(f"The area of the square is {area}")

def rectangle():
    length = float(input("What is the length of the rectangle? "))
    width = float(input("What is the width of the rectangle? "))
    area = length * width
    print(f"The area of the rectangle is {area}")

def parallelogram():
    base = float(input("What is the base of the parallelogram? "))
    height = float(input("What is the height of the parallelogram? "))
    area = base * height
    print(f"The area of the parallelogram is {area}")

def trapezoid():
    base1 = float(input("What is the first base of the trapezoid? "))
    base2 = float(input("What is the second base of the trapezoid? "))
    height = float(input("What is the height of the trapezoid? "))
    area = (base1 + base2) * height / 2
    print(f"The area of the trapezoid is {area}")

shape = input("What shape would you like to calculate the area of? ")
if shape == "triangle":
    triangle()
elif shape == "circle":
    circle()
elif shape == "square":
    square()
elif shape == "rectangle":
    rectangle()
elif shape == "parallelogram":
    parallelogram()
elif shape == "trapezoid":
    trapezoid()
else:
    print("Error: Invalid Shape")
    exit()