import requests

response = requests.get('http://localhost:3000/albums')

# Check if the status code on the response object matches a successful response
if(response.status_code == 200):
    print("Success!")
# Check if the status code indicates a failed authentication attempt
elif(response.status_code == 401):
    print('Authentication failed')
else:
    print('Another error occurred')