import turtle

my_turtle = turtle.Turtle() 
window = turtle.Screen()

my_turtle.color("purple")
my_turtle.shape("turtle")
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.penup()

my_turtle.color("red")

my_turtle.setpos(-30, 20)
my_turtle.pendown()
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.right(90)

window.bgcolor("orange")
window.exitonclick()
