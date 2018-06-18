from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from app.models import FeatureRequest, Client

class ClientSchema(ModelSchema):
    class Meta:
        model = Client

class FeatureRequestSchema(ModelSchema):
    client = fields.Nested(ClientSchema)
    class Meta:
        model = FeatureRequest
