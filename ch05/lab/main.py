import pygame

pygame.init()
display = pygame.display.set_mode()
font = pygame.font.Font(None, 50)

upper_limit = 20
iters = {}
start = 2
max_so_far = 0
scale = 10

for n in range(start, upper_limit + 1):
  pygame.display.flip()
  count = 0
  while n != 1:
   if n % 2 > 0:
     n = 3*n + 1
     count = count + 1
   else:
     n = n / 2
     count = count + 1
  iters[start * scale] = count * scale
  start = start + 1
  pygame.display.flip()
  if len(iters) >= 2:
    pygame.draw.lines(display, "red", False, list(iters.items()))
    new_display = pygame.transform.flip(display, False, True)
    display.blit(new_display, (0, 0))
  pygame.display.flip()
  if max_so_far < count:
    max_so_far = count
    max_val = count

rendered_message = font.render(str(max_so_far), False, "purple")
display.blit(rendered_message, (10, 10))

pygame.display.flip()

print(iters)

pygame.time.wait(5000)