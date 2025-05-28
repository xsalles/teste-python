from backend.db_config import db


class BIOS(db.Model):
    __tablename__ = 'bios'

    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String(100), nullable=True)
    release_date = db.Column(db.String(100), nullable=True)
    
    def to_dict(self):
        return {
            col.name: getattr(self, col.name) for col in self.__table__.columns
        }