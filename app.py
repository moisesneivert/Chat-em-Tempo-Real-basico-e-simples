from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from datetime import datetime

app = Flask(__name__)

socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('templates_index.html')


@socketio.on('message')
def handle_message(data):
    username = data.get('username', 'Anônimo')
    message = data.get('message', '')
    timestamp = datetime.now().strftime('%H:%M')

    emit('message', {
        'username': username,
        'message': message,
        'timestamp': timestamp
    }, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
