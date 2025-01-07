from flask import Blueprint, request, jsonify
from database.db_connection import get_db_connection

material_bp = Blueprint('materials', __name__)

# Upload Materi
@material_bp.route('/upload', methods=['POST'])
def upload_material():
    data = request.json
    title = data['title']
    description = data['description']
    file_url = data['file_url']
    uploaded_by = data['uploaded_by']

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO materials (title, description, file_url, uploaded_by) VALUES (%s, %s, %s, %s)",
                       (title, description, file_url, uploaded_by))
        conn.commit()
        return jsonify({"message": "Material uploaded successfully!"}), 201
    except:
        return jsonify({"message": "Error uploading material!"}), 500
    finally:
        cursor.close()
        conn.close()

# Lihat Semua Materi
@material_bp.route('/', methods=['GET'])
def get_all_materials():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM materials")
    materials = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(materials)
