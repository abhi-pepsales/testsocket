from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "Test"

@socketio.on('message')
def handle_message(message):
    print(f"Received message: {message}")
    send(f"Echo: {message}")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
