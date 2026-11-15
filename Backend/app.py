
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Backend is Running!"

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    course = data.get("course")

    print("Received Form Data:")
    print("Name:", name)
    print("Email:", email)
    print("Course:", course)

    return jsonify({
        "message": f"Thank you {name}! Your form was submitted successfully."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
