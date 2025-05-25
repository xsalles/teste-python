from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    with app.app_context():
        from models.hardware import cpu, bios, disk, network, ram_memory
        from models.software import installed_softwares, updates
        from models.location import Location

        db.create_all()