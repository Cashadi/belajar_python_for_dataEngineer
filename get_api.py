import requests

# response = requests.get('https://bibit.id/')
# print(response.text)

investment_data = {'Name': 'Robo Advisor', 'Investment Amount': 1000000, 'Risk Level': 'Moderate', 'Investment Duration': 12}

response = requests.post('https://bibit.id/', data=investment_data)
print(response.text)