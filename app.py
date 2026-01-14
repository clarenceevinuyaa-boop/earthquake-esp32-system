from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

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
    return jsonify({"intensity": classify(pga)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
