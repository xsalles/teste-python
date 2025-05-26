from db_config import db
from datetime import datetime

class LoggedUser(db.Model):
    __tablename__ = 'logged_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    logon_time = db.Column(db.String(100), nullable=True)

    def to_dict(self):
        return {
            col.name : getattr(self, col.name) for col in self.__table__.columns
        }