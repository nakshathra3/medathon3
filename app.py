from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory database for demonstration
users = []
medicines = []

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    users.append(data)
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    for user in users:
        if user['username'] == data['username'] and user['password'] == data['password']:
            return jsonify({'message': 'Login successful!'}), 200
    return jsonify({'message': 'Invalid credentials!'}), 401

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return jsonify({'message': 'Welcome to your dashboard!'}), 200

@app.route('/profile', methods=['GET'])
def profile():
    return jsonify({'message': 'User profile data'}), 200

@app.route('/add-medicine', methods=['POST'])
def add_medicine():
    data = request.json
    medicines.append(data)
    return jsonify({'message': 'Medicine added successfully!'}), 201

@app.route('/patient-history', methods=['GET'])
def patient_history():
    return jsonify({'message': 'Patient history data'}), 200

@app.route('/pharmacy-map', methods=['GET'])
def pharmacy_map():
    return jsonify({'message': 'Pharmacy map data'}), 200

@app.route('/notes', methods=['GET'])
def notes():
    return jsonify({'message': 'Notes data'}), 200

@app.route('/medicines', methods=['GET'])
def get_medicines():
    return jsonify(medicines), 200

@app.route('/medicine/<int:medicine_id>', methods=['PUT'])
def update_medicine(medicine_id):
    data = request.json
    medicines[medicine_id] = data
    return jsonify({'message': 'Medicine updated successfully!'}), 200

@app.route('/medicine/<int:medicine_id>', methods=['DELETE'])
def delete_medicine(medicine_id):
    medicines.pop(medicine_id)
    return jsonify({'message': 'Medicine deleted successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)