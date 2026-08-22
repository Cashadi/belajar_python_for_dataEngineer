import requests

response = requests.get('https://netflix-api-g992.onrender.com/logout')

# Print the response content-type header
print(response.headers['content-type'])