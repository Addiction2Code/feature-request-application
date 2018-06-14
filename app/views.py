from app import app, db
from app.models import FeatureRequest, Client
from app.schemas import FeatureRequestSchema, ClientSchema
from flask import render_template, request, jsonify, _app_ctx_stack

## Routes
## Reference: REST API Design Rulebook
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/clients')
def clients():
  return render_template('clients.html')

@app.route('/api/feature-requests')
def get_feature_requests():
  feature_requests = FeatureRequest.query.all()
  feature_requests_schema = FeatureRequestSchema(many=True)
  result = feature_requests_schema.dump(feature_requests).data
  return jsonify(feature_requests=result);

@app.route('/api/feature-requests/new', methods=['POST'])
def create_feature_request():
  feature_request = FeatureRequest(
    title=request.json['title'],
    description=request.json['description']
  )
  db.session.add(feature_request)
  db.session.commit()
  id = feature_request.id
  return jsonify({
    "title": request.json['title'],
    "description": request.json['description'],
    "id": id
  })

@app.route('/api/clients')
def get_clients():
  clients = Client.query.all()
  clients_schema = ClientSchema(many=True)
  result = clients_schema.dump(clients).data
  return jsonify(clients=result)

@app.route('/api/clients/new', methods=['POST'])
def create_client():
  client = Client(
    name=request.json['name'],
  )
  db.session.add(client)
  db.session.commit()
  id = client.id
  return jsonify({
    "name": request.json['name'],
    "id": id
  })
