import pygame

pygame.init()

# gets the display and makes it full screen
# no arguments means full screen
screen = pygame.display.set_mode()

# RGB Scheme
screen.fill([255, 0, 0])
pygame.display.flip()

pygame.time.wait(500) #waits 500 ms so we can see result

screen.fill([0, 255, 0])
pygame.display.flip()

pygame.time.wait(500)

screen.fill([0, 0, 255])
pygame.display.flip()