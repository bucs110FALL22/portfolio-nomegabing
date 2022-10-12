import turtle

window = turtle.Screen()
window.bgcolor('lightblue')

num_sides = int(input("How many sides do you want?: "))
side_length = int(input("How long do you want the sides to be?: "))
angle = int(360)

def drawEqShape(a, b):
  turt = turtle.Turtle()
  turt.shape('turtle')
  turt.color('green')
  for n in range(a):
    turt.left(angle / a)
    turt.forward(b)

drawEqShape(a=num_sides, b=side_length)

input("Hit enter when done")