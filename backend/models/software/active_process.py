from backend.db_config import db

class ActiveProcess(db.Model):
    __tablename__ = 'active_processes'
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'), nullable=False)