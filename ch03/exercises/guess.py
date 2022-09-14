import random

rand = random.randint(1, 10)

guess1 = float(input("Guess a number 1 to 10: "))
if guess1 == rand:
  print("Correct")
  exit()
elif guess1 > rand:
  print("Too High")
elif guess1 < rand:
  print("Too Low")

guess2 = float(input("Try again!: "))
if guess2 == rand:
  print("Correct")
  exit()
elif guess2 > rand:
  print("Too High")
elif guess2 < rand:
  print("Too Low")

guess3 = float(input("Last try: "))
if guess3 == rand:
  print("Correct")
elif guess3 > rand:
  print("Too High")
elif guess3 < rand:
  print("Too Low")