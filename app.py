from flask import Flask, request, jsonify, render_template
from datetime import datetime
import os

app = Flask(__name__)

# Store history in memory
history = []

def classify(pga):
    if pga < 0.05:
        return "NONE"
    elif pga < 0.15:
        return "WEAK"
    elif pga < 0.35:
        return "MODERATE"
    elif pga < 0.60:
        return "STRONG"
    else:
        return "VIOLENT"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    pga = float(data["pga"])
    intensity = classify(pga)

    history.append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "pga": round(pga, 3),
        "intensity": intensity
    })

    return jsonify({"intensity": intensity})

@app.route("/history")
def get_history():
    return jsonify(history[-20:])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
