import turtle 
p = turtle.getscreen() #getting basic canvas screen to create graphics has one turtle

t1 = turtle.Turtle()#creating t1 turtle
'''t1.forward(200) #or t1.fd
t1.backward(400) #or t1.bk
#t1.hideturtle()
t1.left(90)
t1.forward(200)
t1.right(90)
t1.forward(400)
t1.right(90)
t1.forward(200)

t2 = turtle.Turtle()
t2.goto(200,100)
t2.left(180)
t2.forward(400)
t2.left(135)
t2.goto(0,0)
t2.goto(0,200) 

#TO DRAW CIRCLE USE PREDIFINED FUNCTION CIRCLE
t1.circle(100) #t1.circle(radius)
t1.dot(200) #t1.dot(diameter) 

#TO DRAW TRIANGLE
t1.goto(200,0)
t1.goto(0,200)
t1.goto(-150,0)
t1.forward(150) # or t1.goto(0,0) or t1.home

#SHOW AND HIDE TURTLE 
turtle.hideturtle() #Center turtle Hide
t1.hideturtle() #Hiding t1 turtle 
t1.goto(188,8)
t1.st() #t1.st()

#t1.pensize,(thickness)
#t1.pencolor("color-name") as a string
#t1.penup(no line will be drawn)
#t1.pendown(line will be drawn)

t1.pencolor("green")
t1.pensize(5)
t1.penup()
t1.goto(200,100)
t1.pendown()
t1.right(45)
t1.goto(150,100)
t1.left(90) '''

#SETTING TITLE AND TURTLE COLOR
p.title("Let's Move Turtle like Fan!")
t1.pencolor("green")
t1.shape("turtle")
#t1.shape("square")
#t1.shape("circle")
#t1.shape("arrow")
#t1.shape("triangle")

t1.shapesize(18,14,12)
for angle in range(0,901,90):
 t1.left(90)
 t1.speed(1)
 