from flask import Blueprint, request, jsonify
from database.db_connection import get_db_connection

assignment_bp = Blueprint('assignments', __name__)

# Upload Tugas
@assignment_bp.route('/upload', methods=['POST'])
def upload_assignment():
    data = request.json
    title = data['title']
    description = data['description']
    file_url = data['file_url']
    deadline = data['deadline']
    uploaded_by = data['uploaded_by']

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO assignments (title, description, file_url, deadline, uploaded_by) VALUES (%s, %s, %s, %s, %s)",
            (title, description, file_url, deadline, uploaded_by)
        )
        conn.commit()
        return jsonify({"message": "Assignment uploaded successfully!"}), 201
    except:
        return jsonify({"message": "Error uploading assignment!"}), 500
    finally:
        cursor.close()
        conn.close()
