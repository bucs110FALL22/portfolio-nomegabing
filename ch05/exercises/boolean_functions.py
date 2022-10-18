
def percentage_to_letter(score=0):
  num_grade = float(input("What did you score on your test?: "))
  if num_grade >= 90:
    return "A"
  elif 80 <= num_grade < 90:
    return "B"
  elif 70 <= num_grade < 80:
    return "C"
  elif 60 <= num_grade < 70:
    return "D"
  elif num_grade < 60:
    return "F"

letter = percentage_to_letter()
grade = letter
print(grade)

def is_passing(grade):
  if letter == "A" or "B" or "C":
    return True
  elif letter == "C" or "F":
    return False

pass_fail = is_passing(letter)
print(pass_fail)