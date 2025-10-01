from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>App1 — Bem-vinda/o!</h1><p>Esta é a aplicação 1.</p>"

@app.route("/health")
def health():
    return Response("OK", status=200)

@app.route("/info")
def info():
    return "<p>App1 - info</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(__import__('os').environ.get("PORT", 8000)))