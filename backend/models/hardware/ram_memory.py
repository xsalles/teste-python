from database import db

class ram_emory(db.Model):
    __tablename__ = 'ram_memories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    size = db.Column(db.String(10), nullable=True)
    usage_percent = db.Column(db.Float, nullable=True)

    def to_dict(self):
        return {
            col.name: getattr(self, col.name) for col in self.__table__.columns
        }