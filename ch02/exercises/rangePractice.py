print(list( range(11)))
print(list( range(3, 11, 2)))
print(list( range(0, 101)))
print(list( range(100, -1, -1)))
print(list( range(10, -11, -5)))

#use RANGE to loop a specific number of times

n = int(input("How many times should it loop?: "))
for _ in range(n):
  print("Ay yo")

print("end of loop")