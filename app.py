from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "name": "Chaitan Divagi",
        "message": "Assignment 3 demo app is running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "cpu": psutil.cpu_percent(interval=0.1),
        "memory": psutil.virtual_memory().percent
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
