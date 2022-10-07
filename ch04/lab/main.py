import pygame
import random
import math

pygame.init()

## PART A
window_width = 600
window_height = 400
window = pygame.display.set_mode([window_width, window_height])
window.fill("dimgray")

pygame.draw.circle(window, "bisque1", (175, 175), 150) #dartboard
pygame.draw.circle(window, "black", (175, 175), 5) # marker points
pygame.draw.circle(window, "black", (0,0), 5) # marker points
pygame.draw.circle(window, "black", (350,0), 5) # marker points
pygame.draw.circle(window, "black", (0,350), 5) # marker points
pygame.draw.circle(window, "black", (350,350), 5) # marker points
pygame.draw.rect(window, "black", (0, 0, 350, 350), 3) # border region
pygame.display.flip()

## PART B

screen = [300, 300]
x2 = 175
y2 = 175
width = 350

for dartHits in range(11):
  randomx = random.randrange(0, 350)
  randomy = random.randrange(0, 350)
  distance_from_center = math.hypot(randomx-x2, randomy-y2)
  pygame.display.flip()
  if distance_from_center <= 150:
    pygame.draw.circle(window, "green", (randomx, randomy), 3)
    pygame.time.wait(100)
    pygame.display.flip()
  else:
    pygame.draw.circle(window, "red", (randomx, randomy), 3)
    pygame.time.wait(100)
    pygame.display.flip()

pygame.time.wait(3000)

## PART C

window.fill("dimgray")
pygame.draw.circle(window, "bisque1", (175, 175), 150) #dartboard
pygame.draw.circle(window, "black", (175, 175), 5) # center point
pygame.draw.rect(window, "black", (0, 0, 350, 350), 3) # board region
pygame.display.flip()

pygame.draw.rect(window, "red", (375, 25, 200, 75)) # player red selection window
pygame.draw.rect(window, "blue", (375, 125, 200, 75)) # player blue selection window
pygame.display.flip()

bet = 0

choice = input("Who do you think will win? Red or Blue: ")
if choice == "Red":
  bet = 1
if choice == "red":
  bet = 1
if choice == "Blue":
  bet = 2
if choice == "blue":
  bet = 2
print("The game will start in 1 second!")
print("Your bet value is ",bet)
pygame.time.wait(1000)

redScore = 0
blueScore = 0

for redvsblue in range(11):
  redx = random.randrange(0, 350)
  redy = random.randrange(0, 350)
  bluex = random.randrange(0, 350)
  bluey = random.randrange(0, 350)
  distanceRed = math.hypot(redx-x2, redy-y2)
  distanceBlue = math.hypot(bluex-x2, bluey-y2)
  pygame.display.flip()
  if distanceRed <= 150:
    pygame.draw.circle(window, "firebrick1", (redx, redy), 3)
    pygame.time.wait(500)
    redScore = redScore + 1
    pygame.display.flip()
  else:
    pygame.draw.circle(window, "firebrick4", (redx, redy), 3)
    pygame.time.wait(500)
    pygame.display.flip()
  if distanceBlue <= 150:
    pygame.draw.circle(window, "dodgerblue1", (bluex, bluey), 3)
    pygame.time.wait(500)
    blueScore = blueScore + 1
    pygame.display.flip()
  else:
    pygame.draw.circle(window, "dodgerblue4", (bluex, bluey), 3)
    pygame.time.wait(500)
    pygame.display.flip()

pygame.time.wait(500)
print("Red's score was ",redScore)
print("Blue's score was ",blueScore)

if redScore > blueScore:
  print("Red wins!")
if blueScore > redScore:
  print("Blue wins!")

if redScore > blueScore and bet == 1:
  print("You predicted correctly!")
if blueScore > redScore and bet == 2:
  print("You predicted correctly!")


# a window.exitonclick()