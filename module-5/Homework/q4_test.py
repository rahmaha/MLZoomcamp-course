
import requests

url = 'http://localhost:9696/q4_predict'


client_id = 'xyz-123'
client = {"job": "unknown", "duration": 270, "poutcome": "failure"}

response = requests.post(url, json=client).json()
print(response)

if response['get_credit'] == True:
    print('Will get credit %s' % client)
else:
    print('not getting credit %s' % client_id)


