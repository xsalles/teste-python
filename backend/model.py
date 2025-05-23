from database import db
from datetime import datetime

class SystemInfo(db.Model):
    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True)

    # basic information
    hostname = db.Column(db.String(100), nullable=True)
    serial_number = db.Column(db.String(100), nullable=True)
    equipment_name = db.Column(db.String(200), nullable=True)
    model = db.Column(db.String(100), nullable=True)
    manufacturer = db.Column(db.String(100), nullable=True)
    os = db.Column(db.String(50), nullable=True)
    os_version = db.Column(db.String(100), nullable=True)
    location = db.Column(db.String(100), nullable=True)

    # hardware information

    cpu = db.Column(db.Text, nullable=True)
    ram_memory = db.Column(db.String(100), nullable=True)
    disk = db.Column(db.Text, nullable=True)
    network = db.Column(db.Text, nullable=True)
    bios = db.Column(db.Text, nullable=True)

    # software information

    installed_software = db.Column(db.Text, nullable=True)
    running_processes = db.Column(db.Text, nullable=True)
    active_services = db.Column(db.Text, nullable=True)
    updates = db.Column(db.Text, nullable=True)

    # mobile specific
    apps_installed = db.Column(db.Text, nullable=True)
    geolocation = db.Column(db.String(200), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            col.name: getattr(self, col.name) for col in self.__table__.columns
        }