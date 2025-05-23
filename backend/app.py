from flask import Flask, request, jsonify
from flask_cors import CORS
from models.model import SystemInfo
from db_config import db, init_db
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db.init_app(app)
init_db(app)

@app.route('/')
def index():
    return "Welcome to the System Information API!"

@app.route('/system_info', methods=['POST'])
def create_system_info():
    data = request.get_json()
    
    system = SystemInfo(**data)
    
    db.session.add(system)
    
    db.session.commit()
    
    return jsonify({"message": "System information received successfully!"}), 201

@app.route('/system_info', methods=['GET'])
def get_system_info():
    systems = SystemInfo.query.all()
    
    return jsonify([s.to_dict() for s in systems]), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')