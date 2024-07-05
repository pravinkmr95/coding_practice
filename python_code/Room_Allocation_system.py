from flask import Flask, request, jsonify

app = Flask(__name__)

rooms = []
reservations = []
users = []

# Function to find an item by id in a list
def find_by_id(items, id):
    return next((item for item in items if item['id'] == id), None)

@app.route('/rooms', methods=['GET'])
def get_rooms():
    return jsonify(rooms)

@app.route('/rooms', methods=['POST'])
def add_room():
    room = request.json
    rooms.append(room)
    return jsonify(room), 201

@app.route('/rooms/<int:id>', methods=['GET'])
def get_room(id):
    room = find_by_id(rooms, id)
    return jsonify(room) if room else ('Room not found', 404)

@app.route('/rooms/<int:id>', methods=['PUT'])
def update_room(id):
    room = find_by_id(rooms, id)
    if not room:
        return 'Room not found', 404
    room.update(request.json)
    return jsonify(room)

@app.route('/rooms/<int:id>', methods=['DELETE'])
def delete_room(id):
    global rooms
    rooms = [room for room in rooms if room['id'] != id]
    return '', 204

@app.route('/reservations', methods=['GET'])
def get_reservations():
    return jsonify(reservations)

@app.route('/reservations', methods=['POST'])
def add_reservation():
    reservation = request.json
    reservations.append(reservation)
    return jsonify(reservation), 201

@app.route('/reservations/<int:id>', methods=['GET'])
def get_reservation(id):
    reservation = find_by_id(reservations, id)
    return jsonify(reservation) if reservation else ('Reservation not found', 404)

@app.route('/reservations/<int:id>', methods=['PUT'])
def update_reservation(id):
    reservation = find_by_id(reservations, id)
    if not reservation:
        return 'Reservation not found', 404
    reservation.update(request.json)
    return jsonify(reservation)

@app.route('/reservations/<int:id>', methods=['DELETE'])
def delete_reservation(id):
    global reservations
    reservations = [reservation for reservation in reservations if reservation['id'] != id]
    return '', 204

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    user = request.json
    users.append(user)
    return jsonify(user), 201

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = find_by_id(users, id)
    return jsonify(user) if user else ('User not found', 404)

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = find_by_id(users, id)
    if not user:
        return 'User not found', 404
    user.update(request.json)
    return jsonify(user)

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    global users
    users = [user for user in users if user['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
