import requests

url = 'http://127.0.0.1:22222/message'

while True:
    text = input("Nachricht an Server: ")
    response = requests.post(url, json={'message':text})
    
    if response.status_code == 200:
        data = response.json()
        print(data['response'])
    else: 
        print("Fehler", response.status_code)