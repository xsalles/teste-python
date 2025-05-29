from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    with app.app_context():
        from backend.models.model import SystemInfo
        from backend.models.hardware import cpu, bios, disk, network, ram_memory
        from backend.models.software import installed_softwares, updates, logged_users, local_users
        from backend.models.location import Location

        db.create_all()