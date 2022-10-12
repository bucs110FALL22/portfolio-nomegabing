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


def star2():
  levels = int(input("Enter the desired pyramid height: "))
  for i in range(1, levels + 1):
    print("*" * i)

def rstar2():
  levels = int(input("Enter the desired pyramid height: "))
  for i in range(levels, 0, -1):
    print("*" * i)

star2()
rstar2()