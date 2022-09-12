import turtle

leTurtle = turtle.Turtle() 
window = turtle.Screen()

n = int(input("How many sides does the shape have? "))
l = int(input("How long should the sides be? "))
angle = int(360)

leTurtle.color("blue")
for i in range(0, n+1):
  leTurtle.left(angle / n)
  leTurtle.forward(l)
window.exitonclick()