import requests
import json

# Serveradressen mit denen der Client kommunizieren soll
URL = "http://127.0.0.1:12345/spieler"
URL2 = "http://127.0.0.1:12345/loeschen"

auftrag = 0

# Dauer abfrage ob Spieler erstellt oder gelöscht werden soll
while True:
    auftrag = int(input("1 = Spieler erstellen, 2 = Spielerliste löschen: "))

    # Spieler erstellen
    while auftrag == 1:
        spieler_daten = {
            "name": str(input("Name: ")),
            "jahrgang": int(input("Jahrgang: ")),
            "staerke": int(input("Staerke: ")),
            "torschuss": int(input("Torschuss: ")),
            "motivation": int(input("Motivation: "))
        }


        response = requests.post(URL, json=spieler_daten)
        print("Statuscode:", response.status_code)

        if response.status_code == 201:
            print("✅Spieler erfolgreich erstellt:")
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
        else:
            print("❌Fehler bei der Erstellung:")
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))

        auftrag = 0

    # Spieler löschen
    while auftrag == 2:
        response = requests.post(URL2)
        print("Statuscode:", response.status_code)

        
        if response.status_code == 201:
            print("✅Spieler erfolgreich erstellt:")
            #print(json.dumps(response.json(), indent=4, ensure_ascii=False))
        else:
            print("❌Fehler beim Löschen: ")
            #print(json.dumps(response.json(), indent=4, ensure_ascii=False))
            
        auftrag = 0