from flask import Flask
from routes.auth_routes import auth_bp
from routes.material_routes import material_bp
from routes.assignment_routes import assignment_bp
from routes.submission_routes import submission_bp
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY  # Menggunakan SECRET_KEY dari config.py

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(material_bp, url_prefix='/materials')
app.register_blueprint(assignment_bp, url_prefix='/assignments')
app.register_blueprint(submission_bp, url_prefix='/submissions')

if __name__ == "__main__":
    app.run(debug=True)
