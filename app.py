from flask import Flask, jsonify, request

app = Flask(__name__)


# Home endpoint
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "application": "ACEest Fitness & Gym",
        "message": "Welcome to ACEest Fitness & Gym",
        "status": "running"
    })


# Health check endpoint
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    })


# In-memory client data
clients = []


# Get all clients
@app.route("/clients", methods=["GET"])
def get_clients():
    return jsonify(clients)


# Add a new client
@app.route("/clients", methods=["POST"])
def add_client():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    required_fields = ["name", "age", "weight"]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"{field} is required"
            }), 400

    client = {
        "id": len(clients) + 1,
        "name": data["name"],
        "age": data["age"],
        "weight": data["weight"]
    }

    clients.append(client)

    return jsonify(client), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
