import turtle #1. import modules
import random
import pygame
import math
import time

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
time.sleep(1)
## 5. Your PART A code goes here
# part A option 1
michelangeloSpeed = random.randrange(1,101)
leonardoSpeed = random.randrange(1,101)
michelangelo.forward(michelangeloSpeed)
leonardo.forward(leonardoSpeed)
time.sleep(1) #delays program so i can see what happened before the second example starts

michelangelo.up() #reset option 1
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
time.sleep(.1)

for speed in range(11):
 michelangelo.forward(random.randint(1,10))
 leonardo.forward(random.randint(1,10))
 time.sleep(.15) #delays movements so i can watch the program work


# PART B - complete part B here

pygame.init()
window = pygame.display.set_mode()

triangleCoords = []
equiTriangle = (3)
side_length = (60)
offset = (70) #offset from the top left corner

for n in range(equiTriangle + 1):
 theta = (2.0 * math.pi * (n)) / equiTriangle
 x = side_length * math.cos(theta) + offset
 y = side_length * math.sin(theta) + offset
 triangleCoords.append((x, y))
  
pygame.draw.polygon(window, [255, 0, 0], triangleCoords, 10)
pygame.display.flip()
pygame.time.wait(3000)
window.fill([0, 0, 0])

squareCoords = []
square = (4)

for n in range(square + 1):
 theta = (2.0 * math.pi * (n)) / square
 x = side_length * math.cos(theta) + offset
 y = side_length * math.sin(theta) + offset
 squareCoords.append((x, y))
  
pygame.draw.polygon(window, [255, 0, 0], squareCoords, 10)
pygame.display.flip()
pygame.time.wait(3000)
window.fill([0, 0, 0])

hexCoords = []
hexagon = (6)

for n in range(hexagon + 1):
 theta = (2.0 * math.pi * (n)) / hexagon
 x = side_length * math.cos(theta) + offset
 y = side_length * math.sin(theta) + offset
 hexCoords.append((x, y))
  
pygame.draw.polygon(window, [255, 0, 0], hexCoords, 10)
pygame.display.flip()
pygame.time.wait(3000)
window.fill([0, 0, 0])

nonCoords = []
nonagon = (9)

for n in range(nonagon + 1):
 theta = (2.0 * math.pi * (n)) / nonagon
 x = side_length * math.cos(theta) + offset
 y = side_length * math.sin(theta) + offset
 nonCoords.append((x, y))
  
pygame.draw.polygon(window, [255, 0, 0], nonCoords, 10)
pygame.display.flip()
pygame.time.wait(3000)
window.fill([0, 0, 0])

circleCoords = []
circle = (9)

for n in range(circle + 1):
 theta = (2.0 * math.pi * (n)) / circle
 x = side_length * math.cos(theta) + offset
 y = side_length * math.sin(theta) + offset
 circleCoords.append((x, y))
  
pygame.draw.polygon(window, [255, 0, 0], circleCoords, 10)
pygame.display.flip()
pygame.time.wait(3000)
window.fill([0, 0, 0])

window.exitonclick()

# goto(x, y)
#   x: x coordinate along the x axis
#   y: y coordinate along the y axis
# forward(n)
#   n: The number of units forward to move
#  example: myturtle.forward(20)

