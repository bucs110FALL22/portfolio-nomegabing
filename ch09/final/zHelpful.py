# import requests

# class Helpful:

#   def __init__(self):
    
#     self.url = "http://api.fungenerators.com/fact/random"

#   def __str__(self):

#     return self.url

#   def get(self):

#     r = requests.get(self.url)
#     response = r.json()

#     keys = dict.keys(response)
#     print(keys)
    
#     return response['error']

#     if response.get('success'):
#       print("LETS GOOO")
    
#     if response.get('contents'):
#       return response['contents']
      
#     else:
#       return None
    
# http://api.fungenerators.com/fact/random/