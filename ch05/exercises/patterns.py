rows = input("How many rows would you like? ")
numrows = []

def star_pyramid():
  for n in range(int(rows)):
    numrows.append("*")
    print(''.join(numrows))

star_pyramid()

star = "*"

rnumrows = []

def rstar_pyramid():
  for n in range(int(rows)):
    rnumrows.append("*")
  for n in range(int(rows)):
    print(''.join(rnumrows))
    rnumrows.pop()

rstar_pyramid()