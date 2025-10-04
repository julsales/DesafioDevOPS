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
        <title>App1 - Desafio DevOps</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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
            <h1>🚀 App1 - Aplicação Flask</h1>
            <p class="info">Esta é a <strong>primeira aplicação</strong> do desafio DevOps!</p>
            <p>✅ Executando em container Docker</p>
            <p>🔄 Acessível via proxy reverso Nginx</p>
            <p>🌐 Rota: <code>/app1</code></p>
            
            <div>
                <a href="/app1/info" class="button">ℹ️ Status</a>
                <a href="/app1/health" class="button">💚 Health Check</a>
                <a href="/" class="button">🏠 Voltar ao Início</a>
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return Response("OK", status=200)

@app.route("/info")
def info():
    import os
    return f"""
    <h2>📊 Informações do App1</h2>
    <ul>
        <li><strong>Container:</strong> desafio-app1</li>
        <li><strong>Porta:</strong> {os.environ.get('PORT', '8000')}</li>
        <li><strong>Ambiente:</strong> {os.environ.get('FLASK_ENV', 'development')}</li>
        <li><strong>Python:</strong> {os.sys.version}</li>
        <li><strong>Flask:</strong> Aplicação Web Framework</li>
    </ul>
    <p><a href="/app1/">← Voltar</a></p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(__import__('os').environ.get("PORT", 8000)))