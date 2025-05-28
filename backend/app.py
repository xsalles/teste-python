from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.models.model import SystemInfo
from backend.db_config import db, init_db
from dotenv import load_dotenv
import os
from client.insert_data import collect_and_insert_device_info

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db.init_app(app)
init_db(app)

def main():
    with app.app_context():
        collect_and_insert_device_info()
        
if __name__ == '__main__':
    main()