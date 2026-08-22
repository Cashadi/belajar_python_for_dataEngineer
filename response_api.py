import requests

response = requests.get('https://netflix-api-g992.onrender.com/logout')

# Check the response status code
if (response.status_code == 200):
  print('The server responded succesfully!')