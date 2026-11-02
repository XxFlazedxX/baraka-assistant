from flask import Flask, render_template, request, jsonify
from main import process_message, AgentState, seed_products, get_all_products

app = Flask(__name__)
seed_products()
sessions = {}

def get_or_create_session(session_id):
    if session_id not in sessions:
        sessions[session_id] = AgentState()
    return sessions[session_id]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = (data.get("message") or "").strip()
    session_id = data.get("session_id", "default")

    if not user_message:
        return jsonify({"error": "empty message"}), 400

    state = get_or_create_session(session_id)
    try:
        response = process_message(user_message, state)
    except Exception as e:
        print(f"[chat error] {e}")
        response = "Sorry, something went wrong. Please try again."

    return jsonify({"response": response, "session_id": session_id})

@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(get_all_products())

@app.route("/healthz")
def healthz():
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)