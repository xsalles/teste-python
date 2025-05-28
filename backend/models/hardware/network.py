from backend.db_config import db


class Network(db.Model):
    __tablename__ = 'networks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    ip_address = db.Column(db.String(100), nullable=True)
    mac_address = db.Column(db.String(100), nullable=True)


    def to_dict(self):
        return {
            col.name: getattr(self, col.name) for col in self.__table__.columns
        }