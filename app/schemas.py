from marshmallow_sqlalchemy import ModelSchema
from app.models import FeatureRequest, Client

class FeatureRequestSchema(ModelSchema):
    class Meta:
        model = FeatureRequest

class ClientSchema(ModelSchema):
    class Meta:
        model = Client
