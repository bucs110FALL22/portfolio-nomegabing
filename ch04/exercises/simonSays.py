import random
import pygame

pygame.init()
screen = pygame.display.set_mode()

red = [255, 0, 0]
purple = [255, 0, 255]
green = [0, 255, 0]
blue = [0, 0, 255]
black = [0, 0, 0]

direction = ["UP","DOWN", "LEFT", "RIGHT"]

print("Your arrow keys correspond to the following colors:")
for i in direction:
  if i == "UP":
    print("UP: red")
    screen.fill(red)
  elif i == "DOWN":
    print("DOWN: purple")
    screen.fill(purple)
  elif i == "LEFT":
    print("LEFT: green")
    screen.fill(green)
  elif i == "RIGHT":
    print("RIGHT: blue")
    screen.fill(blue)
  pygame.display.flip()
  pygame.time.wait(500)

screen.fill(black)   
pygame.display.flip()

input("Press enter when you are ready to continue...")

random.shuffle(direction)
print("Simon says to enter the following sequence:")
for i in direction:
  if i == "UP":
    screen.fill(red)
  elif i == "DOWN":
    screen.fill(purple)
  elif i == "LEFT":
    screen.fill(green)
  elif i == "RIGHT":
    screen.fill(blue)
  pygame.display.flip()
  pygame.time.wait(1000)
  screen.fill(black)
  pygame.display.flip()
  pygame.time.wait(500)

result = []

input("Click on the window, enter the sequence, then press enter in the console:")

print("You pressed:")
for event in pygame.event.get():
  #print(event)
  if event.type == pygame.KEYDOWN:
    if(event.key == pygame.K_UP):
      screen.fill(red)
      result.append("UP")
      print("UP")
    elif(event.key == pygame.K_DOWN):
      screen.fill(purple)
      result.append("DOWN")
      print("DOWN")
    elif(event.key == pygame.K_LEFT):
      screen.fill(green)
      result.append("LEFT")
      print("LEFT")
    elif(event.key == pygame.K_RIGHT):
      screen.fill(blue)
      result.append("RIGHT")
      print("RIGHT")
    pygame.display.flip()
    pygame.time.wait(1000)
    
print("You Entered:", result)
print("The correct pattern was", direction)
if result == direction:
  print("Correct! You win.")
else:
  print("Were you even paying attention?")