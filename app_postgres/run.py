# Ponto de entrada: cria o app e sobe o servidor de desenvolvimento.
# Fica separado para o "app" em si não depender de como é executado.
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)