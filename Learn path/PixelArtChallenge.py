from turtle import *

def drawBrownSquare():
    color("brown")
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()

def drawGreenSquare():
    color("green")
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()

def drawGraySquare():
    color("gray")
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()

def drawOrangeSquare():
    color("orange")
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()

def drawYellowSquare():
    color("yellow")
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()

speed(0)

drawBrownSquare()
forward(10)
drawGreenSquare()
forward(10)
drawBrownSquare()
forward(10)
drawGreenSquare()
forward(10)
drawBrownSquare()
forward(10)
drawGreenSquare()
forward(10)
drawBrownSquare()
forward(10)
drawGreenSquare()
forward(10)
drawBrownSquare()
forward(10)
drawGreenSquare()
forward(10)
drawBrownSquare()

left(180)
forward(100)
left(90)
forward(10)
left(90)

drawGreenSquare()
forward(10)
drawBrownSquare()
forward(10)
drawGreenSquare()
forward(10)
drawBrownSquare()
forward(10)
drawGreenSquare()
forward(10)
drawBrownSquare()
forward(10)
drawGreenSquare()
forward(10)
drawBrownSquare()
forward(10)
drawGreenSquare()
forward(10)
drawBrownSquare()
forward(10)
drawGreenSquare()

left(180)
forward(100)
left(90)
forward(10)
left(90)

for x in range(10):
    drawBrownSquare()
    forward(10)
    drawBrownSquare()



left(180)
forward(100)
left(90)
forward(10)
left(90)
for x in range(7):
    for x in range(10):
        drawGraySquare()
        forward(10)
        drawGraySquare()
    left(180)
    forward(100)
    left(90)
    forward(10)
    left(90)

done()