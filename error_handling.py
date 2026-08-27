import requests
# Import the correct exception class
from requests.exceptions import HTTPError

url ="https://pintu.co.id/"
try: 
    r = requests.get(url) 
    
    # Enable raising errors for all error status_codes
    r.raise_for_status()
    
    print(r.status_code)

# Intercept the error 
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')