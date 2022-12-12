import requests

class FunFact:

  def __init__(self):
   
    '''
    Initializes the FunFact class
    args: self
    return: none
    '''

    self.url = "https://uselessfacts.jsph.pl/random.json?language=en"

  def __str__(self):

    '''
    Gives me better access to the url for testing purposes
    args: self
    return: API's url as a string
    '''

    return self.url

  def get(self):

    '''
    Uses the request module to get data from my url
    args: self
    return: The text argument from the API, which is the fun fact
    '''

    r = requests.get(self.url)
    response = r.json()

    return response['text']