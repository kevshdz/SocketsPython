from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room, rooms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "SocketIO Server is Running"

clients = {}


@socketio.on('connect')
def handle_connect(connect):
    sid = request.sid
    clients[sid] = request.namespace
    print(f'Client connected: {connect}')



@app.route('/clients')
def get_clients():
    return {'connected_clients': len(clients)}

@socketio.on('message')
def get_messages(message):
    print('received message: ' + message)
    emit('message',message,broadcast=True)





# @socketio.on('geocoding')
# def handle_geocoding(id, latitude, longitude, status, zone):
#     print(f'Received data: ID={id}, Latitude={latitude}, Longitude={longitude}, Status={status}, Zone={zone}')
    



if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001)
