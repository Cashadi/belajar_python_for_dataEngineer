import requests

response = requests.get('https://netflix-api-g992.onrender.com/logout')

if (response.status_code == 200):
  print('The server responded succesfully!')

# Check the response status code
elif (response.status_code == 404):
  print('Oops, that API could not be found!')