from flask import Blueprint, request, jsonify
from database.db_connection import get_db_connection

submission_bp = Blueprint('submissions', __name__)

# Upload Pengumpulan Tugas
@submission_bp.route('/upload', methods=['POST'])
def upload_submission():
    data = request.json
    assignment_id = data['assignment_id']
    student_id = data['student_id']
    file_url = data['file_url']
    submitted_at = data['submitted_at']

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO submissions (assignment_id, student_id, file_url, submitted_at) VALUES (%s, %s, %s, %s)",
            (assignment_id, student_id, file_url, submitted_at)
        )
        conn.commit()
        return jsonify({"message": "Submission uploaded successfully!"}), 201
    except:
        return jsonify({"message": "Error uploading submission!"}), 500
    finally:
        cursor.close()
        conn.close()
