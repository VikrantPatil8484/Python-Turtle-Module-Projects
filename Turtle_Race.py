from random import *
from turtle import *
penup()

#  positioning the pen
goto(-140, 140)

#  loop for creating the lines labelling with numbers
for sp in range(15):
    #  setting the speed
    speed(10)

    #  writing the integer
    write(sp)

    #  setting the right angle at 90 degrees
    right(90)

    #  moving forward at 10  units
    forward(10)

    #  ready to draw
    pendown()

    #  moving forward at 150 units
    forward(150)

    #  not ready to draw
    penup()

    #  moving back at 160 units
    backward(160)

    #  setting the angle at 90 degrees
    left(90)

    #  MOVING forward at 20 units
    forward(20)

ankur = Turtle()  # inheriting the turtle

ankur.color('green')  # setting the color to green for the first turtle

ankur.shape('turtle')  # setting the shape to "turtle"

ankur.penup()  # not ready to draw

ankur.goto(-160, 100)  # positioning the turtle

ankur.pendown()  # ready todraw


gajurel = Turtle()  # inheriting another turtle

gajurel.color('red')  # setting the color og the turtle to red

gajurel.shape('turtle')  # declaring the shape of the turtle to "turtle"

gajurel.penup()  # not ready to draw

gajurel.goto(-160, 80)  # positioning

gajurel.pendown()  # ready to draw

turtleVar = Turtle()  # inheriting the last turtle

turtleVar.color('blue')  # setting the color of the turtle as "blue"

turtleVar.shape('turtle')  # declaring the s+99hape of the turtle

turtleVar.penup()  # not ready to draw

turtleVar.goto(-160, 60)  # positioning

turtleVar.pendown()  # ready

for turn in range(100):  # loop for the racew
  
    # setting the speed randomly with the "random" module
    ankur.forward(randint(1, 5))
    
    # setting the speed randomly with the "random" module
    gajurel.forward(randint(1, 5))
    
    # setting the speed randomly with the "random" module
    turtleVar.forward(randint(1, 5))

turtle.done()
