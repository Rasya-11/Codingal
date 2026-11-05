from flask import Flask, jsonify, request, render_template
import json
app = Flask(__name__)
def get_sneakers():
    with open("sneakers.json", "r") as file:
        return json.load(file)
    @app.route("/")
    def home():
        return render_template("index.html")
    @app.route("/sneakers", methods=["GET"])
    def sneakers():
        data = get_sneakers()
        return jsonify(data)
    @app.route("/sneakers", methods=["POST"])
    def add_sneakers():
        new_sneaker = request.get_json()
        data = get_sneakers()
        new_sneaker["id"] = len(data) + 1
        data.append(new_sneaker)
        with open("sneakers.json", "w") as file:
            json.dump(data, file, indent=4)
        return jsonify(new_sneaker)
    if __name__== "__main__":
        app.run(debug=True)