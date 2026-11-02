from datetime import datetime
from flask import Flask, render_template, request, jsonify
from main import process_message, AgentState, seed_products, get_all_products, db

app = Flask(__name__)
seed_products()
sessions_col = db["sessions"]


def load_state(session_id):
    state = AgentState()
    doc = sessions_col.find_one({"_id": session_id})
    if doc:
        state.conversation_history = doc.get("history", [])
        state.inquiry_saved = doc.get("inquiry_saved", False)
    return state


def save_state(session_id, state):
    sessions_col.update_one(
        {"_id": session_id},
        {"$set": {
            "history": state.conversation_history,
            "inquiry_saved": state.inquiry_saved,
            "updatedAt": datetime.utcnow(),
        }},
        upsert=True,
    )


@app.after_request
def no_cache(resp):
    resp.headers["Cache-Control"] = "no-store"
    return resp


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

    try:
        state = load_state(session_id)
        response = process_message(user_message, state)
        save_state(session_id, state)
    except Exception as e:
        print(f"[chat error] {e}")
        response = "Sorry, something went wrong. Please try again."

    return jsonify({"response": response, "session_id": session_id})


@app.route("/api/products", methods=["GET"])
def get_products():
    products = get_all_products()
    for p in products:
        p["_id"] = str(p["_id"])
    return jsonify(products)


@app.route("/healthz")
def healthz():
    return jsonify({"ok": True})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)