from app import app, db
from app.models import FeatureRequest, Client
from app.schemas import FeatureRequestSchema, ClientSchema
from flask import render_template, request, jsonify, redirect, url_for
from sqlalchemy import update
from datetime import datetime

##
## Important Functions
##

# This function works like a revolver
def rotate_list(items, up=True):
  # If there are no items in list, do not reorder.
  if len(items):
    if up:
      # Priority of current Increasing (in n to 1 direction)
      items.insert(0, items.pop(-1))
    else:
      # Priority of current Decreasing (in 1 to n direction)
      items.append(items.pop(0))
  return items

# Update feature_requests with priority according to index+start_priority
def store_feature_request_order(feature_requests, start_priority=1):
  for index, item in enumerate(feature_requests):
    if item != None:
      feature_requests[index]["priority"] = (index + start_priority)
      update = db.session.query(FeatureRequest).filter_by(id=item['id']).update({
        "priority": feature_requests[index]["priority"]
      })
      db.session.commit()
  return feature_requests


def reprioritize_feature_requests(client_id, cur_priority, new_priority, rotate=True):
  priorities = sorted([int(cur_priority), int(new_priority)])
  feature_requests = FeatureRequest.query.filter(
    FeatureRequest.client_id==client_id,
    FeatureRequest.priority.between(*priorities)
  ).order_by(
    FeatureRequest.priority.asc()
  )
  feature_requests_schema = FeatureRequestSchema(many=True)
  # The second param determines if the current item is being moved up or not.
  revolver = feature_requests_schema.dump(feature_requests).data
  # Should we rotate? When deleting it doesn't make sense to.
  if(rotate):
    revolver = rotate_list(
      revolver,
      (int(cur_priority) > int(new_priority))
    )
  return store_feature_request_order(revolver, priorities[0])


##
## Routes
## Reference: REST API Design Rulebook
##

##
## Page Related
##

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/clients')
def clients():
  return render_template('clients.html')

@app.route('/feature-requests/<client_id>')
def feature_requests(client_id):
  client = Client.query.filter(Client.id==client_id).first()
  if client:
    return render_template('requests.html', client=client)
  else:
    return redirect(url_for('index'), code=302)

@app.errorhandler(404)
def page_not_found(e):
  # note that we set the 404 status explicitly
  return render_template('notfound.html'), 404


##
## API Related
##


## Feature Requests

@app.route('/api/feature-requests')
@app.route('/api/feature-requests/<int:client_id>')
def get_feature_requests(client_id=None):
  feature_requests = FeatureRequest.query
  if(isinstance(client_id, int)):
    feature_requests = feature_requests.filter(FeatureRequest.client_id==client_id)
  feature_requests = feature_requests.order_by(FeatureRequest.priority.asc()).all()
  feature_requests_schema = FeatureRequestSchema(many=True)
  result = feature_requests_schema.dump(feature_requests).data
  return jsonify(feature_requests=result)

@app.route('/api/feature-requests/new', methods=['POST'])
def create_feature_request():
  # Grab the highest priority (for this client).
  initial_priority = FeatureRequest.nextPriorityByClient(request.json['client_id'])
  feature_request = FeatureRequest(
    title=request.json['title'],
    product_area=request.json['product_area'],
    target_date=datetime.strptime(request.json['target_date'], "%Y-%m-%d").date(),
    description=(request.json['description'] if 'description' in request.json.keys() else ""),
    priority=initial_priority,
    client_id=request.json['client_id']
  )
  db.session.add(feature_request)
  db.session.commit()
  id = feature_request.id

  # We'll return all records with adjusted priority.
  return jsonify(
    feature_requests=reprioritize_feature_requests(request.json['client_id'], initial_priority, request.json['priority'])
  )

@app.route('/api/feature-requests/prioritize', methods=['POST'])
def prioritize_feature_request():
  result = reprioritize_feature_requests(
    request.json['client_id'],
    request.json['cur_priority'],
    request.json['new_priority']
  )
  return jsonify(feature_requests=result);

# @app.route('/api/feature-requests/reprioritize', methods=['POST'])
# def prioritize_feature_request():
#   result = store_feature_request_order(
#     response.json['items']
#   )
#   return jsonify(feature_requests=result);

@app.route('/api/feature-requests/delete/<int:feature_request_id>', methods=['DELETE'])
def delete_feature_request(feature_request_id):
  feature_request = FeatureRequest.query.filter(FeatureRequest.id==feature_request_id).first()
  db.session.delete(feature_request)
  db.session.commit()
  # Should re-prioritize...
  result = reprioritize_feature_requests(
    feature_request.client_id,
    feature_request.priority,
    (FeatureRequest.nextPriorityByClient(feature_request.client_id)-1),
    False
  )
  return jsonify(feature_requests=result)

## Clients

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

@app.route('/api/clients/delete/<client_id>', methods=['DELETE'])
def delete_client(client_id):
  client = Client.query.filter(Client.id==client_id).first()
  result = db.session.delete(client)
  db.session.commit()
  return jsonify(success=result)
