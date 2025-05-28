from backend.db_config import db
from datetime import datetime

class Updates(db.Model):
    __tablename__ = 'updates'
    
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=True)
    hotfix_id = db.Column(db.String(50), nullable=True)
    installed_on = db.Column(db.String(50), nullable=True)
    device_id = db.Column(db.String(100), nullable=True)
    
    def to_dict(self):
        return {
            col.name: getattr(self, col.name) for col in self.__table__.columns
        }