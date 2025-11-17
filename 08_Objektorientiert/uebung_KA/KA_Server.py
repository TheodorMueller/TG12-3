from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "<html><body><h1>Willkommen Du</h1></body></html>"


@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    Nachricht = data.get('message','')
    print(f"Empfangen: {Nachricht}")
    rest = f"Echo {Nachricht}"

    return jsonify({'response':rest})


@app.route('/keineAhnung')
def keineAhnung():
    return "<html><body><h1>Theo liebt Mia mehr</h1></body></html>"






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=22222)