import pygame
import json
import requests
import FoodAPI
import random
# import DrinkAPI

def main():
  pygame.init()
  screen = pygame.display.set_mode((600, 400))
  screen.fill((0,182,213))
  font = pygame.font.SysFont('Arial', 25)
  userpassfont = pygame.font.SysFont('Arial', 15)
  pygame.display.set_caption("What's for lunch?")
  pygame.display.update()

  lunchState = "mainscreen"
  
  while lunchState == "mainscreen":
    randomButt = pygame.draw.rect(screen, 'pink', [200, 250, 200, 100])
    screen.blit(font.render("What's for Lunch?", True, (0, 0, 0)), (45, 90))
    screen.blit(font.render('Randomize', True, (0, 0, 0)), (200, 300))
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if randomButt.collidepoint(pygame.mouse.get_pos()):
          lunchState = "randomizedScreen"

  if lunchState == "randomizedScreen":
    food = FoodAPI.FoodAPI()
    randomFood = random.randrange(1,10)
    typeOfFood = food.typeOfFood(randomFood)
    print(typeOfFood)

    foodImg = food.foodGet()
    print(foodImg)

    
  
  ### pygame screen setup

  
  
main()