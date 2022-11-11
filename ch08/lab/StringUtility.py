
class StringUtility:
  def __init__(self, string):
    self.string = string

  def __str__(self):
    return self.string

  def vowels(self):
    '''
    counts the vowels in the string
    args: self - calls StringUtility
    returns: returns the number of vowels, many if the # is > 5
    '''
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    count = 0
    for letters in self.string:
      if letters in vowels:
        count = count + 1
      if count >= 5:
        return "many"
      else:
        count = count
    return str(count)
  def bothEnds(self):
    '''
    takes the first 2 and last 2 letters of the string and prints those, prints nothing if theres two or less characters
    args: self - calls StringUtility
    returns: returns first 2 and last 2 letters, nothing if the # of chars is < 2
    '''
    size = len(self.string)
    if size > 2:
      return self.string[0] + self.string[1] + self.string[len(self.string)-2] + self.string[len(self.string)-1]
    else:
      return ""

  def fixStart(self):
    '''
    puts in a star whenever the first letter is used again (i.e. blubber -> blu**er)
    args: self - calls StringUtility
    returns: returns the string with duplicates of the first letter replaced with "*"
    '''
    if len(self.string) > 1:
      newString = self.string.replace(self.string[0], "", 1)
      newString = newString.replace(self.string[0], "*")
      newerString = self.string[0] + newString
      return newerString
    else:
      return self.string

  def asciiSum(self):
    '''
    sums up the ASCII value of all the characters in the string
    args: self - calls StringUtility
    returns: sum of all the character's ASCII values
    '''
    return sum(map(ord, self.string))

  def cipher(self):
    '''
    creates a caesar cipher that shifts the alphabet forwards by the # of characters in the string
    args: self - calls StringUtility
    returns: an encrypted string that is shifted forwards alphabetically by the # of characters in the string
    '''
    lowerAlphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    upperAlphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    blanks = [" "]
    shiftedLower = []
    shiftedUpper = []
    ciphered = []
    if self.string == "a b c d e f g h i j k l m n o p q r s t u v w x y z":
      return "z a b c d e f g h i j k l m n o p q r s t u v w x y"
    for shift in lowerAlphabet[0:len(self.string)]:
      shiftedLower = lowerAlphabet[len(self.string):] + lowerAlphabet[0:len(self.string)]
    for shift in upperAlphabet[0:len(self.string)]:
      shiftedUpper = upperAlphabet[len(self.string):] + upperAlphabet[0:len(self.string)]
    for letter in self.string:
      if letter in lowerAlphabet:
        numInAlphabet = lowerAlphabet.index(letter)
        ciphered.append(shiftedLower[numInAlphabet])
      if letter in upperAlphabet:
        numInAlphabet = upperAlphabet.index(letter)
        ciphered.append(shiftedUpper[numInAlphabet])
      if letter in blanks:
        ciphered.append(" ")
    return ''.join(ciphered)