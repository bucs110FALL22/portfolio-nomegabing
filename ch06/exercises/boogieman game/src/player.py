import pygame
import random

# like an import for classes instead of modules, called inheriting from a class
class Player(pygame.sprite.Sprite):
  def __init__(self):
    #first line you have to put in the sprite class init
    super().__init__(self)
    self.health = 3
    self.direction = 3 #as in 3:00 on a clock
    self.image = pygame.image.load("assets/image.png") #required
    self.rect = self.image.get_rect() #also required
    self.speed = 3 # # of pixels it moves
    

  def move_up(self):
    self.rect.y -= self.speed
  def move_down(self):
    self.rect.y += self.speed
  def move_right(self):
    self.rect.x += self.speed
  def move_left(self):
    self.rect.y -= self.speed

  def fight(self, opponent):
    return random.randrange(3) # 2/3 chance of winning