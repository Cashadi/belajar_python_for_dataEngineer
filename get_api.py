import requests

response = requests.get('https://bibit.id/')
print(response.text)