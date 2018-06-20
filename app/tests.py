import os
import unittest
from flask import json

# import glob
# from flask_fixtures.loaders import JSONLoader
# from flask_fixtures import load_fixtures

from app import models, app, db

app.config.from_object('config.TestConfig')

class HighLevelTests(unittest.TestCase):

  ## SETUP ##

  def setUp(self):
    self.app = app.test_client()
    db.drop_all()
    db.create_all()

    # for fixture_dir in app.config.get('FIXTURES_DIRS', ['./fixtures']):
    #   for fixture_file in glob.glob(fixture_dir + '/*.json'):
    #     fixtures = JSONLoader().load(fixture_file)
    #     load_fixtures(db, fixtures)

    # executed after each test
    def tearDown(self):
      db.drop_all()

  ## TESTS ##

  ## Pages
  def test_main_page(self):
    response = self.app.get('/', follow_redirects=True)
    self.assertEqual(response.status_code, 200)

  def test_feature_requests_page(self):
    response = self.app.get('/feature-requests/%d' % 1, follow_redirects=True)
    self.assertEqual(response.status_code, 200)

  def test_clients_page(self):
    response = self.app.get('/clients', follow_redirects=True)
    self.assertEqual(response.status_code, 200)

  ## API Endpoints
  def test_get_feature_requests(self):
    response = self.app.get('/api/feature-requests/%d' % 1, follow_redirects=True)
    assert response.content_type == 'application/json'
    data = json.loads(response.get_data())
    assert type(data) is dict

  def test_get_clients(self):
    response = self.app.get('/api/clients', follow_redirects=True)
    assert response.content_type == 'application/json'
    data = json.loads(response.get_data())
    assert type(data) is dict

if __name__ == "__main__":
  unittest.main()
