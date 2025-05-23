from database import db
from datetime import datetime
from sqlalchemy import ForeignKey

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

    # foreign key to hardware information

    cpu_id = db.Column(db.Integer, ForeignKey('cpus.id'), nullable=True)
    ram_memory_id = db.Column(db.Integer, ForeignKey('ram_memories.id'), nullable=True)
    disk_id = db.Column(db.Integer, ForeignKey('disks.id'), nullable=True)
    network_id = db.Column(db.Text, ForeignKey('networks.id'), nullable=True)
    bios_id = db.Column(db.Text, ForeignKey('bios.id'), nullable=True)

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

    # relationsships

    cpu = db.relationship("CPU", foreign_keys=[cpu_id])
    ram_memory = db.relationship("ram_memory", foreign_keys=[ram_memory_id])
    disk = db.relationship("Disk", foreign_keys=[disk_id])
    network = db.relationship("Network", foreign_keys=[network_id])
    bios = db.relationship("BIOS", foreign_keys=[bios_id])
    
    def to_dict(self):
        return {
            col.name: getattr(self, col.name) for col in self.__table__.columns
        }