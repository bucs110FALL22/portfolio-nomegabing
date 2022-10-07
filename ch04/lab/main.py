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

input("Who do you think will win, red or blue?")
mousex,mousey = pygame.mouse.get_pos()
def chooseRed():
 if 375 < mousex < 575 and 25 < mousey < 100: #and pygame.MOUSEBUTTONDOWN:
  print("You're betting on red!")
def chooseBlue():
 if 375 < mousex < 575 and 125 < mousey < 200: #and pygame.MOUSEBUTTONDOWN:
  print("You're betting on blue!")



# a window.exitonclick()