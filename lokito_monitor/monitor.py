
from flask import Flask, jsonify, render_template
import json
from collections import Counter

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('monitor.html')

@app.route('/dados-campanhas')
def dados():
    try:
        with open('lokito_memoria.json') as f:
            dados = json.load(f)
        modos = [d['modo'] for d in dados]
        contagem = Counter(modos)
        return jsonify({
            "labels": list(contagem.keys()),
            "counts": list(contagem.values())
        })
    except:
        return jsonify({"labels": [], "counts": []})

if __name__ == "__main__":
    app.run(debug=True)
