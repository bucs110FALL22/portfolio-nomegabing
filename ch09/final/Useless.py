import requests

class Useless:

  def __init__(self):

    self.url = "https://uselessfacts.jsph.pl/random.json"

  def __str__(self):

    return self.url

  def get(self):

    r = requests.get(self.url)
    response = r.json()

    return 