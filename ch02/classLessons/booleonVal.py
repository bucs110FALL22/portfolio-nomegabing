#not a math operation, logic that evaluates to True/False
#These are BOOLEON EXPRESSIONS
# - only 2 possible answers: T/F

var = True
other_var = False
print(type(var))

print("True") #string
print(True) #booleon value

print(type("True"))
print(type(True))
print("True" == True)

#any object in python can be evaluated as a bool
#False Values -> False/None/0/Empty Container
#True Values -> anything else lol

#Bool operators:
x = 1
y = 5
  # == -> equality
  # checking for equality means DOUBLE ==
print(x==x)
print(y==x)
  # != -> not equal, a "!" is called a "bang"
print(x!=y)

print("- - - - - -")
print("Hello" == "Hello")
print("Hello" == "Goodbye")
print("Hello" > "Goodbye") #h before g, alphabetical and will print
print("Hello" < "Goodbye")
print("hello" == "Hello") #case sensitive

### SEMANTIC OPERATORS
# and / or / not / in / is
# and : True and True == True
# or : True or True == True
# not : True == False
# in : 5 in [1,2,3,4,5] == True
# is : '"Hello"' is '"Hello"'

### if statements
# allows for algorithmic selection
print("- - - If Statement Code - - -")
money = 5
cost = 3.5
if money >= cost:
    print("Here is your change: ", float(money) - float(cost))
else:
    print("Insufficient Funds")

g = int(input("What's your number?: "))
if g >= 20:
  print("yup")
elif g > 10:
  print("too much L")
else:
  print("nope lol")