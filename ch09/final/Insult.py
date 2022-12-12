import requests

class Insult:

  def __init__(self):

    '''
    Initializes the Insult class
    args: self
    return: none
    '''

    self.url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"

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
    return: The insult argument from the API, which is a randomly generated insult
    '''

    r = requests.get(self.url)
    response = r.json()

    return response['insult']