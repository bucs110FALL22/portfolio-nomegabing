import turtle

window = turtle.Screen()
window.bgcolor('white')
window.screensize()

turtly = turtle.Turtle()
turtly.color = ('black')
turtly.shape = ('turtle')

angle = int(360)
#print(window.screensize())

def drawShape(sides,length,startpos): #draws an equilateral shape
  turtly.up()
  turtly.goto(startpos)
  turtly.down()
  for n in range(sides):
    turtly.left(angle/sides)
    turtly.forward(length)

def drawUpsideDown(sides,length,startpos): #draws eq. shape upside down
  turtly.up()
  turtly.goto(startpos)
  turtly.down()
  for n in range(sides):
    turtly.right(angle/sides)
    turtly.forward(length)

def main(): #calls functions to draw the 5 pieces
  drawShape(sides=360,length=9/6,startpos=(0,-80)) #outer circle
  drawShape(sides=360,length=7/6,startpos=(0,-60)) #inner circle
  drawUpsideDown(sides=3,length=180,startpos=(90,65)) #big triangle
  drawShape(sides=3,length=105,startpos=(52,-20)) #small triangle
  drawShape(sides=360,length=1/2,startpos=(-1,-19)) #inmost circle

main()

window.exitonclick()