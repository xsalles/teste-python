from backend.db_config import db


class Disk(db.Model):
    __tablename__ = 'disks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    size = db.Column(db.String(100), nullable=True)
    type = db.Column(db.String(50), nullable=True)
    usage_percent = db.Column(db.String(10), nullable=True)


    def to_dict(self):
        return {
            col.name: getattr(self, col.name) for col in self.__table__.columns
        }