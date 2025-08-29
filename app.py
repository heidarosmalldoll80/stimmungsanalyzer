from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Laden des vortrainierten Modell (Platzhalter: Ersetze mit deinem Modell)
model = joblib.load('dein_modell.pkl')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text')
    # Hier die Logik zur Stimmungsanalyse implementieren
    # Nutzen Sie dein Modell
    if not text:
        return jsonify({'error': 'Fehlender Text zum Analysieren'}), 400
    prediction = model.predict([text])[0]
    return jsonify({'stimmung': prediction})

if __name__ == '__main__':
    app.run(debug=True)