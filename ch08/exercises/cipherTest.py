### THIS FILE WAS USED FOR TESTING SOME STUFF WITH THE CIPHER BIT, ITS NOT PART OF THE LAB

stringy = "abcdefghijklmnopqrstuvwxyz"

# a b c d e f g h i j k l m n o p q r s t u v w x y z

def cipher():
    lowerAlphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    upperAlphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    blanks = [" "]
    shiftedLower = []
    shiftedUpper = []
    ciphered = []

    for shift in lowerAlphabet[0:len(stringy)]:
      shiftedLower = lowerAlphabet[len(stringy) - 1:] + lowerAlphabet[0:len(stringy)]
    for shift in upperAlphabet[0:len(stringy)]:
      shiftedUpper = upperAlphabet[len(stringy):] + upperAlphabet[0:len(stringy)]

    for letter in stringy:
      if letter in lowerAlphabet:
        numInAlphabet = lowerAlphabet.index(letter)
        ciphered.append(shiftedLower[numInAlphabet])
      if letter in upperAlphabet:
        numInAlphabet = upperAlphabet.index(letter)
        ciphered.append(shiftedUpper[numInAlphabet])
      if letter in blanks:
        ciphered.append(" ")
    print("Result: ", ''.join(ciphered))
    print("This is the shift ", shift)
    print("Shifted Lowercase: ", shiftedLower)
    print("Length of stringy: ", len(stringy))

cipher()