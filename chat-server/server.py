from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
# Replace with your own secret key
app.config['SECRET_KEY'] = 'your_secret_key'
# Allow all origins for simplicity
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def index():
    return "Chat Server"


@socketio.on('connect')
def handle_connect():
    username = request.args.get('username')
    print(f'Client {username} has connected to the server')


@socketio.on('message')
def handle_message(data):
    print('Received message: ' + data)
    emit('message', data, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
