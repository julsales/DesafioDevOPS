from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>App2 - Desafio DevOps</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                color: white;
                text-align: center;
            }
            .container {
                background: rgba(255,255,255,0.1);
                padding: 30px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            }
            h1 { margin-top: 0; }
            .info { margin: 20px 0; }
            .button {
                display: inline-block;
                background: rgba(255,255,255,0.2);
                padding: 10px 20px;
                border-radius: 5px;
                text-decoration: none;
                color: white;
                margin: 5px;
                transition: background 0.3s;
            }
            .button:hover { background: rgba(255,255,255,0.3); }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎯 App2 - Segunda Aplicação</h1>
            <p class="info">Olá! Esta é a <strong>segunda aplicação</strong> Flask!</p>
            <p>✅ Container independente</p>
            <p>🔄 Mesmo proxy, serviço diferente</p>
            <p>🌐 Rota: <code>/app2</code></p>
            
            <div>
                <a href="/app2/status" class="button">📈 Status</a>
                <a href="/app2/health" class="button">💚 Health Check</a>
                <a href="/" class="button">🏠 Voltar ao Início</a>
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return Response("OK", status=200)

@app.route("/status")
def status():
    import os
    import datetime
    return f"""
    <h2>📈 Status do App2</h2>
    <ul>
        <li><strong>Container:</strong> desafio-app2</li>
        <li><strong>Status:</strong> 🟢 Online</li>
        <li><strong>Porta:</strong> {os.environ.get('PORT', '8000')}</li>
        <li><strong>Ambiente:</strong> {os.environ.get('FLASK_ENV', 'development')}</li>
        <li><strong>Timestamp:</strong> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</li>
        <li><strong>Versão:</strong> 1.0.0</li>
    </ul>
    <p><a href="/app2/">← Voltar</a></p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(__import__('os').environ.get("PORT", 8000)))