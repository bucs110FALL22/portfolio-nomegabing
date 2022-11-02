import time

class Animal:
  def __init__(self, name, type):
    self.id = time.strftime("%d%m%M%S") #unique ID through time
    self.name = name
    self.type = type
    self.arrived = time.strftime("%d/%m/%Y")
    self.adopted = None # can use in if statement
  def set_adopted(self):
    self.adopted = time.strftime("%d/%m/%Y")
  def __str__(self):
    result_str = f"{self.name}[{self.type}]"
    result_str += f"\narroved: {self.arrived}"
    result_str += f"\nadpoted: {self.adopted}"
    return result_str
    
def main():
  pochita = Animal("Pochita", "Dog")
  pochita.set_adopted()
  print(pochita)

  winston = Animal("Winston", "Monkey")
  winston.set_adopted()
  print(winston)

main()