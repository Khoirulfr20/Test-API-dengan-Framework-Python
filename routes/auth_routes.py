from flask import Blueprint, request, jsonify
from database.db_connection import get_db_connection
import bcrypt

auth_bp = Blueprint('auth', __name__)

# Register User
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data['name']
    email = data['email']
    password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    role = data['role']

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)",
                       (name, email, password, role))
        conn.commit()
        return jsonify({"message": "User registered successfully!"}), 201
    except:
        return jsonify({"message": "Error during registration!"}), 500
    finally:
        cursor.close()
        conn.close()

# Login User
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()

        if user and bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):
            return jsonify({
                "message": "Login successful!",
                "user": {
                    "id": user[0],
                    "name": user[1],
                    "email": user[2],
                    "role": user[4]
                }
            }), 200
        else:
            return jsonify({"message": "Invalid credentials!"}), 401
    except:
        return jsonify({"message": "Error during login!"}), 500
    finally:
        cursor.close()
        conn.close()
