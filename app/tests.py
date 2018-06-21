import os
import unittest
from flask import json
from flask_fixtures import FixturesMixin
from datetime import datetime
import pytest

from app import app, db
from app.models import Client, FeatureRequest

app.config.from_object('config.TestConfig')

class HighLevelTests(unittest.TestCase, FixturesMixin):

  app = app
  db = db
  fixtures = ['clients.json', 'feature-requests.json']
  persist_fixtures = True

  ##
  ## SETUP ##
  ##

  def setUp(self):
    self.app = app.test_client()

  ##
  ## TESTS ##
  ##

  ##
  ## Pages
  ##

  def test_page_main(self):
    response = self.app.get('/', follow_redirects=True)
    self.assertEqual(response.status_code, 200)

  def test_page_feature_requests(self):
    response = self.app.get('/feature-requests/%d' % 1, follow_redirects=True)
    self.assertEqual(response.status_code, 200)

  def test_page_clients(self):
    response = self.app.get('/clients', follow_redirects=True)
    self.assertEqual(response.status_code, 200)

  ##
  ## Database
  ##

  @pytest.mark.run(order=1)
  def test_db_fixtures(self):
    clients = Client.query.all()
    assert len(clients) == Client.query.count() == 4
    feature_requests = FeatureRequest.query.all()
    assert len(feature_requests) == FeatureRequest.query.count() == 6

  @pytest.mark.run(order=2)
  def test_db_add_client(self):
    client = Client()
    client.name = 'Test Client'
    self.db.session.add(client)

  @pytest.mark.run(order=3)
  def test_db_add_feature_request(self):
    feature_request = FeatureRequest()
    feature_request.title = 'Does adding a request work?'
    feature_request.priority = 1
    feature_request.client_id = 1
    feature_request.product_area = 'Billing'
    feature_request.target_date = datetime.strptime(
      '2018-06-20', "%Y-%m-%d"
    ).date()
    self.db.session.add(feature_request)

  @pytest.mark.run(order=4)
  def test_db_delete_client(self):
    client = Client.query.filter(Client.name=='Test Client')
    if client.delete():
      assert True
    else:
      assert False

  @pytest.mark.run(order=5)
  def test_db_delete_feature_request(self):
    feature_request = FeatureRequest.query.filter(
      FeatureRequest.title=='Does adding a request work?',
      FeatureRequest.client_id==1
    )
    if feature_request.delete():
      assert True
    else:
      assert False

  ##
  ## API Endpoints
  ##

  def test_api_get_feature_requests(self):
    response = self.app.get('/api/feature-requests/%d' % 1, follow_redirects=True)
    assert response.content_type == 'application/json'
    data = json.loads(response.get_data())
    assert type(data) is dict

  def test_api_get_clients(self):
    response = self.app.get('/api/clients', follow_redirects=True)
    assert response.content_type == 'application/json'
    data = json.loads(response.get_data())
    assert type(data) is dict

  def test_api_prioritize_feature_requests(self):
    # Get request with priority 1.
    pre_first = FeatureRequest.query.filter(
      FeatureRequest.priority==1,
      FeatureRequest.client_id==1
    ).first()
    # Get request with priority 3.
    pre_third = FeatureRequest.query.filter(
      FeatureRequest.priority==3,
      FeatureRequest.client_id==1
    ).first()
    # Perform reprioritization.
    response = self.app.post(
      '/api/feature-requests/prioritize',
      json={
        'client_id': 1,
        'cur_priority': 3,
        'new_priority': 1
      }
    )
    # Get priority of request with old priority 1.
    post_first = FeatureRequest.query.filter(FeatureRequest.id==pre_first.id).first()
    # Get priority of request with old priority 3.
    post_third = FeatureRequest.query.filter(FeatureRequest.id==pre_third.id).first()
    # Assert that the proper order is in place.
    assert post_first.priority == 2
    assert post_third.priority == 1

if __name__ == "__main__":
  unittest.main()
