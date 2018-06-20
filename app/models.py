from app import db
from sqlalchemy import func

class FeatureRequest(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(150), nullable=False)
  description = db.Column(db.String(564), default='')
  product_area = db.Column(db.String(255), default='')
  priority = db.Column(db.Integer)
  client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
  client = db.relationship("Client", back_populates="feature_requests")

  def __repr__(self):
    return self.title

  @classmethod
  def nextPriority(self):
    return db.session.query(func.max(self.priority)).scalar()

  @classmethod
  def nextPriorityByClient(self, client):
    result = db.session.query(func.max(self.priority)).filter(self.client_id==client).scalar()
    if(result):
      return (result+1)
    else:
      return 1

class Client(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(150), unique = True, nullable=False)
  feature_requests = db.relationship("FeatureRequest", back_populates="client", cascade="delete")

  def __repr__(self):
    return self.name
