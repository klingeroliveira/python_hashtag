# site com os scripts: https://cdnjs.com;
# pip install python-socketio flask-socketio simple-websocket

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketIO = SocketIO(app, cors_allowed_origins="*")

# funcionalidade de enviar mensagem
@socketIO.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

# criar 1 pagina = rota
@app.route("/")

def homepage():
    return render_template("index.html")


socketIO.run(app, host="localhost")
# roda o aplicativo (debug permite alterar os arquivos e f5 na página, não precisa reiniciar o projeto)
#app.run(debug=True)