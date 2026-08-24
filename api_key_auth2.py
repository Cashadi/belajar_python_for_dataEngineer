import requests

# Create the headers dictionary
headers = {
    'Authorization': 'Bearer 8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3'
}

# Pass the headers to the request
response = requests.get(
    'http://localhost:3000/albums',
    headers=headers
)

if(response.status_code == 200):
    print("Success!")
elif(response.status_code == 401):
    print('Authentication failed')
else:
    print('Another error occurred')