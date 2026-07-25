from flask import Flask, render_template, request, jsonify
from ai_service import generate_code

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    language = data["language"]
    prompt = data["prompt"]

    result = generate_code(language, prompt)

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
