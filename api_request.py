# Import requests package
import requests

# Assign URL to variable: url
url = 'https://myhero.id/api/v1/hero'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)