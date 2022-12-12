# import Helpful
import FunFact
import Insult

def main():
  print("Wanna hear a cool fun fact I just learned? I really really wanna tell you!")
  print("1 for Yes")
  print("2 for No")
  userInput = int(input(""))
  print("")

  if userInput == 1:

    funFact = FunFact.FunFact() # grabs url
    # print(funFact)

    fact = funFact.get() # puts the get() function into variable

    print(fact)
    
    print("")
    print("Pretty cool, huh? Aren't you glad you said yes?")
    
  else:

    print("You really don't want to hear my fun fact?! Well, here's what I think about you, since you were so rude to me!")
    print("")
    
    insult = Insult.Insult() # grabs url
    # print(insult)

    insults = insult.get() # puts the get() function into variable

    print(insults)
    
    print("")
    print("That's what you get, nerd.")

main()