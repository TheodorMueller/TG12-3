from flask import Flask, request,jsonify
import json
import os

app = Flask(__name__)


# Definition der Spieler-Klasse
class Spieler:

    def __init__(self, name:str, jahrgang:int, staerke:int, torschuss:int, motivation:int):
        self.name: str = name
        self.jahrgang: int = jahrgang
        if 0 > staerke > 10:
            raise ValueError("Stärke muss zwischen 0 und 10 liegen.")
        self.staerke: int = staerke
        if 0 > torschuss > 10:
            raise ValueError("Torschuss muss zwischen 0 und 10 liegen.")
        self.torschuss: int = torschuss
        if 0 > motivation > 10:
            raise ValueError("Motivation muss zwischen 0 und 10 liegen.")
        self.motivation: int = motivation
    
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "jahrgang": self.jahrgang,
            "staerke": self.staerke,
            "torschuss": self.torschuss,
            "motivation": self.motivation
        }

    @staticmethod
    def from_dict(data):
        return Spieler(data.get("name"), 
                       int(data.get("jahrgang")),
                       int(data.get("staerke")),
                       int(data.get("torschuss")),
                       int(data.get("motivation"))
                       )


# Route für die Hauptseite
@app.route('/')
def home():
    return "<html><h1>Server ist bereit und wartet auf Anfragen</h1><p>Legen wir los</p></html>"

# Route für Spieler
@app.route('/spieler', methods=['POST'])
def handle_spieler():
    data = request.json
    S1 = Spieler(
        data.get('name'),
        int(data.get('jahrgang')),
        int(data.get('staerke')),
        int(data.get('torschuss')),
        int(data.get('motivation'))
    )
    spieler_dict = S1.to_dict()
    if os.path.exists('daten.jason'):
        with open('daten.json', 'r') as f:
            try: 
                spieler_liste = json.load(f)
            except json.JSONDecodeError:
                spieler_liste = []
    else: 
        spieler_liste = []
    spieler_liste.append(spieler_dict)
    with open('daten.json', 'w') as f:
        json.dump(spieler_liste, f, indent=4)
    return jsonify({"responser": "Spieler gespeichert!"})

# Spieler laden
@app.route('/players', methods=['GET', 'POST'])
def show_players():
    #...


    # HTML-Seite mit Team- und Positions-Auswahl
    html = """
    <html>
        <head>
            <title>Alle Spieler</title>
        </head>
        <body>
            <h1>Gespeicherte Spieler</h1>
            <form method="post">
            <table border="1" cellpadding="5">
                <tr>
                    <th>Name</th>
                    <th>Jahrgang</th>
                    <th>Stärke</th>
                    <th>Torschuss</th>
                    <th>Motivation</th>
                    <th>Team</th>
                    <th>Position</th>
                </tr>
    """
    for idx, spieler in enumerate(spieler_liste):
        html += f"""
                <tr>
                    <td>{spieler['name']}</td>
                    <td>{spieler['jahrgang']}</td>
                    <td>{spieler['staerke']}</td>
                    <td>{spieler['torschuss']}</td>
                    <td>{spieler['motivation']}</td>
                    <td>
                        <select name="team_{idx}">
        """
        for team in teams:
            selected = "selected" if spieler.get("team", "") == team else ""
            html += f'<option value="{team}" {selected}>{team if team else "Bank"}</option>'
        html += """
                        </select>
                    </td>
                    <td>
                        <select name="position_{idx}">
        """
        for pos in positionen:
            selected = "selected" if spieler.get("position", "Feldspieler") == pos else ""
            html += f'<option value="{pos}" {selected}>{pos}</option>'
        html += """
                        </select>
                    </td>
                </tr>
        """
    html += """
            </table>
            <br>
            <input type="submit" value="Teams speichern">
            </form>
            <br>
            <form action="/spiel" method="post">
                <input type="submit" value="Teams gegeneinander spielen lassen">
            </form>
        </body>
    </html>
    """
    return html

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
    return jsonify({"response": response_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)  # Server starten
    