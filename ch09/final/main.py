import Helpful
import Useless

def main():
  print("What kind of fact would you like to see?")
  print("1: A Helpful One")
  print("2: A Useless One")
  userInput = int(input(""))

  if userInput == 1:

    helpfulFact = Helpful.Helpful()
    print(helpfulFact)

    helpingFacts = helpfulFact.get()

    print(helpingFacts)
    
  if userInput == 2:

    uselessFact = Useless.Useless()
    print(uselessFact)

    uselessFacts = uselessFact.get()

    print(uselessFacts)

    
  # else:
  #   print("Pick an option next time.")

main()