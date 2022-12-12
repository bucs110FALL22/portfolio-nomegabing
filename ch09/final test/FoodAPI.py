import requests

class FoodAPI:
  
  def __init__(self, foodtype=''):

    self.url = f'https://foodish-api.herokuapp.com/images/{foodtype}/{foodtype}1.jpg'

  def __str__(self):

    return self.url
    
  def foodGet(self):
    
    r = requests.get(self.url)
    #response is just a json dictonary of values after .json() call
    response = r.json()

    return response

  def change_category(self, category):
    pass
    #self.url = #...

# {"image":"https://foodish-api.herokuapp.com/images/burger/burger101.jpg"}

  def urlstring(self, foodtype=''):
    return self.url
    
  def typeOfFood(self, type):
    if type == 1:
      return 'biryani'
    if type == 2:
      return 'burger'
    if type == 3:
      return 'butter-chicken'
    if type == 4:
      return 'dessert'
    if type == 5:
      return 'dosa'
    if type == 6:
      return 'idly'
    if type == 7:
      return 'pasta'
    if type == 8:
      return 'pizza'
    if type == 9:
      return 'rice'
    if type == 10:
      return 'samosa'