# ask a user for a number btwn 2-1000
# for every number btwn 1 and user upper limit:
# if multiple of 3 and 5, print "fizzbuzz"
# if multiple of 3, print "fizz"
# if multiple of 5, print "buzz"

num = int(input("Input a number between 2 and 1000: "))
for i in range(1, num):
 if i % 3 == 0 and i % 5 == 0:
   print("FizzBuzz")
 elif i % 3 == 0:
   print("Fizz")
 elif i % 5 == 0:
   print("Buzz")

