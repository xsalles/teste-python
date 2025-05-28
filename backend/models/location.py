from flask_sqlalchemy import SQLAlchemy
from backend.db_config import db

class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(200), nullable=True)
    loc = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            col.name: getattr(self, col.name) for col in self.__table__.columns
        }