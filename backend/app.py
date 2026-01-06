from flask import Flask, jsonify
from flask_cors import CORS
from db import get_connection

app = Flask(__name__)
CORS(app)   # 🔥 THIS LINE FIXES IT

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/message")
def message():
    return jsonify(message="Hello from Backend API")

@app.route("/db-check")
def db_check():
    try:
        conn = get_connection()
        conn.close()
        return jsonify(database="Connected")
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
