def cube(side):
    volume = side ** 3
    print(f"The volume of the cube is {volume}")
def cylinder(radius, height):
    volume = 3.14 * radius ** 2 * height
    print(f"The volume of the cylinder is {volume}")
def sphere(radius):
    volume = 4 / 3 * 3.14 * radius ** 3
    print(f"The volume of the sphere is {volume}")
def cone(radius, height):
    volume = 1 / 3 * 3.14 * radius ** 2 * height
    print(f"The volume of the cone is {volume}")
def pyramid(base, base2, height):
    volume = 1 / 3 * ((base * base2 ) * height)
    print(f"The volume of the pyramid is {volume}")
def rectangular_prism(length, width, height):
    volume = length * width * height
    print(f"The volume of the rectangular prism is {volume}")

shape = input("What shape would you like to calculate the volume of? ")
if shape == "cube":
    side = float(input("What is the length of the side of the cube? "))
    cube(side)
elif shape == "cylinder":
    radius = float(input("What is the radius of the cylinder? "))
    height = float(input("What is the height of the cylinder? "))
    cylinder(radius, height)
elif shape == "sphere":
    radius = float(input("What is the radius of the sphere? "))
    sphere(radius)
elif shape == "cone":
    radius = float(input("What is the radius of the cone? "))
    height = float(input("What is the height of the cone? "))
    cone(radius, height)
elif shape == "pyramid":
    base1 = float(input("What is the base of the pyramid? "))
    base2 = float(input("What is the other base of the pyramid? "))
    height = float(input("What is the height of the pyramid? "))
    pyramid(base1, base2, height)
elif shape == "rectangular prism":
    length = float(input("What is the length of the rectangular prism? "))
    width = float(input("What is the width of the rectangular prism? "))
    height = float(input("What is the height of the rectangular prism? "))
    rectangular_prism(length, width, height)
else:
    print("Error: Invalid Shape")
    exit()
