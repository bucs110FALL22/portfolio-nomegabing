import pygame
import random

class Projectile(pygame.sprite.Sprite):
  def __init__(self):
    #first line you have to put in the sprite class init
    super().__init__(self)
    self.image = pygame.image.load("assets/enemy.png") #required
    self.rect = self.image.get_rect() #also required
    self.speed = 1 # # of pixels it moves

  def update(self):
    self.rect.x += self.speed
    