# Imports
from flask import Flask, request, jsonify, render_template
from pydantic import BaseModel, Field, ValidationError 
from model import Spieler
import json 
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


dateiname = "spieler.json"

# schaut ob datei schon existiert->läd daten in spieler_liste
if os.path.exists(dateiname):
    with open(dateiname, "r", encoding="utf-8") as f:
        daten = json.load(f)
    spieler_liste = [Spieler(**s) for s in daten]
    print("📂Geladene Spieler: ")
    for s in spieler_liste:
        print(s)
else:
    spieler_liste = []
    print("Leere Spielerliste erstellt!")


# Funktion
def Anzeige():
    return f"Methode: {request.method}<br>Args: {request.args}<br>Form: {request.form}<br>Data: {request.data}<br>Headers: {request.headers}<br>Cookies: {request.cookies}<br>Path: {request.path}<br>URL: {request.url}<br>Addr: {request.remote_addr}"


# Route für die Hauptseite
@app.route('/')
def home():
    anz = Anzeige()
    return anz

# Impressum-Seite
@app.route('/profil')
def impressum():
    return "<html><body><h1>Impressum</h1><p>Ich bin Theodor</p></body></html>"

# HTML Seite
@app.route('/steckbrief')
def steckbrief():
    return render_template('index.html')


# Route zum Empfangen von Nachrichten
@app.route('/message', methods=['POST'])
def handle_message():
    data = request.json
    message = data.get('message', '')
    print(f"Empfangen: {message}")
    response_message = f"Echo: {message}"

    print(Anzeige())
    
    return jsonify({"response": response_message})


# Spieler erstellen
@app.route('/spieler', methods=['POST'])
def handle_Spieler():
    """Erstellt einen neuen Spieler"""
    try:
        data = request.get_json()
        spieler = Spieler(**data)
        spieler_liste.append(spieler)
        # Spielerdaten in Json-datei speichern
        with open("spieler.json", "w", encoding="utf-8") as f:
            json.dump([s.model_dump() for s in spieler_liste], f, ensure_ascii=False, indent=4)
        print("✅ Spieler wurden in 'spieler.json' gespeichert.")

        return jsonify({
            "status": "ok",
            "message": "Spieler erfolgreich erstellt und gespeichert!",
            "spieler": spieler.model_dump()
        }), 201
    except ValidationError as e:
        return jsonify({
            "status": "error",
            "message": "Validierung fehlgeschlagen",
            "details": e.errors()
        }), 400
    

# Spieler anzeigen
@app.route('/anzeigeSpieler')
def Anzeige_Spieler():
    line = ""
    d = ""
    b = 1
    for d in spieler_liste:
        line = (f"{line} <br> Spieler {b}: {d} <br> ")
        b+=1
    return f"<html><body><h1>Vorhandene Spieler</h1><br>{line}</body></html>"


# Soieler löschen
@app.route('/loeschen', methods=['POST'])
def Liste_loeschen():
    global spieler_liste 
    spieler_liste = []
    with open("spieler.json", "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False ,indent=4)
    return jsonify({"": ""}), 201
        
 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)  # Server starten

# Ab hier darf nichts mehr stehen!!!
