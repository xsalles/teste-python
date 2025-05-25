from db_config import db

class InstalledSoftware(db.Model):
    __tablename__ = 'installed_softwares'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    installation_date = db.Column(db.DateTime, nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.id'), nullable=False)

    def to_dict(self):
        return {
            col.name: getattr(self, col.name) for col in self.__table__.columns
        }