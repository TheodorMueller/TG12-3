from flask import Flask, request,jsonify
from pydantic import BaseModel, Field, ValidationError 
from model import Spieler


app = Flask(__name__)

spieler_liste = []

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

# Route zum Empfangen von Nachrichten
@app.route('/message', methods=['POST'])
def handle_message():
    data = request.json
    message = data.get('message', '')
    print(f"Empfangen: {message}")
    response_message = f"Echo: {message}"

    print(Anzeige())
    
    return jsonify({"response": response_message})


# Spieler
@app.route("/spieler", methods=["POST"])
def handle_Spieler():
    """Erstellt einen neuen Spieler"""
    try:
        data = request.get_json()
        spieler = Spieler(**data)
        spieler_liste.append(spieler)
        return jsonify({
            "status": "ok",
            "message": "Spieler erfolgreich erstellt!",
            "spieler": spieler.model_dump()
        }), 201
    except ValidationError as e:
        return jsonify({
            "status": "error",
            "message": "Validierung fehlgeschlagen",
            "details": e.errors()
        }), 400



@app.route("/anzeigeSpieler")
def Anzeige_Spieler():
    line = ""
    d = ""
    for d in spieler_liste:
        line = (f"{d} <br> {line} <br> ")
    return f"<html><body><h1>Vorhandene Spieler</h1><br>{line}</body></html>"




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)  # Server starten

# Ab hier darf nichts mehr stehen!!!
