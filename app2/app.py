from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>App2 — Olá!</h1><p>Isto é o app2, não o app1 :D.</p>"

@app.route("/health")
def health():
    return Response("OK", status=200)

@app.route("/status")
def status():
    return "<p>App2 - status</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(__import__('os').environ.get("PORT", 8000)))