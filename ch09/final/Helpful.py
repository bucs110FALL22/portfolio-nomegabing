import requests

class Helpful:

  def __init__(self):
    
    self.url = "http://api.fungenerators.com/fact/random/"

  def __str__(self):

    return self.url

  def get(self):

    r = requests.get(self.url)
    response = r.json()

    return 
    
# http://api.fungenerators.com/fact/random/