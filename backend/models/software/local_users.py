from backend.db_config import db

class LocalUsers(db.Model):
    __tablename__ = 'local_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'), nullable=False)