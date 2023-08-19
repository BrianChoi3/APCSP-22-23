from turtle import *
def polygon(sides, length):
    for i in range(sides):
        forward(length)
        left(360 / sides)

shape = int(input("how many sides?"))
length = int(input("how long is each side?"))
polygon(shape, length)