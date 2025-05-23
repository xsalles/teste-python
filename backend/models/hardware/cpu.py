from database import db

class CPU(db.Model):
    __tablename__ = 'cpus'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    cores = db.Column(db.Integer, nullable=True)
    usage_percent = db.Column(db.Float, nullable=True)

    def to_dict(self):
        return {
            col.name: getattr(self, col.name) for col in self.__table__.columns
        }