import turtle
turtle.bgcolor('yellow')
turtle.speed(0)
turtle.pensize(2)
turtle.pencolor('blue')

def drawcircle(radius):
 for i in range(25):
  turtle.circle(radius)
  radius = radius-3
  
def drawdesign():
 for i in range(10):
  drawcircle(150)
  turtle.right(36)
  
drawdesign()
turtle.done()
  
