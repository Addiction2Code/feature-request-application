from app import db

class FeatureRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique = True, nullable=False)
    description = db.Column(db.String(564), default='')
    priority = db.Column(db.Integer)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    client = db.relationship("Client", back_populates="feature_requests")

    def __repr__(self):
        return '<FeatureRequest(name={self.name!r})>'.format(self=self)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique = True, nullable=False)
    feature_requests = db.relationship("FeatureRequest", back_populates="client")

    def __repr__(self):
        return self.name
