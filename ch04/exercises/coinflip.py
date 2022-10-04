import turtle
import random

window = turtle.Screen()
coinTurtle = turtle.Turtle()
coinTurtle.color('gray')
coinTurtle.shape('turtle')
coinTurtle.up()

widthheight = turtle.screensize()
print(widthheight)

def cointoss():
  return random.choice(["Heads", "Tails"])

while (coinTurtle.xcor(),0) and (coinTurtle.ycor(),0) and (coinTurtle.xcor(),400) and (coinTurtle.ycor(),300):
  cointoss()
  if cointoss() == "Heads":
    coinTurtle.left(90)
    coinTurtle.forward(50)
  elif cointoss() == "Tails":
    coinTurtle.right(90)
    coinTurtle.forward(50)
else:
  coinTurtle.goto(200,150)

window.exitonclick()