import requests
p = True
f = False

# Server-URL
server_url = 'http://localhost:12345/message'
spieler_server = 'http://localhost:12345/spieler'

while f == True:
    # Nachricht vom Benutzer eingeben
    message = input("Nachricht an den Server: ")
    # Nachricht an den Server senden
    response = requests.post(server_url, json={"message": message})
    # Antwort vom Server anzeigen
    if response.status_code == 200:
        data = response.json()
        print(f"Antwort vom Server: {data['response']}")
    else:
        print("Fehler bei der Anfrage:", response.status_code)

while p == True:
    spieler = input("Erstelle einen Spieler: ")
    response = requests.post(spieler_server, json={"spieler":spieler})
    # Antwort vom server
    if response.status_code == 200:
        data = response.json()
        print(f"Antwort vom Server: {data['response']}")
    else:
        print("Fehler bei der Anfrage:", response.status_code)