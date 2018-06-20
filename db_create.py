from app import app, db

import glob
from flask_fixtures.loaders import JSONLoader
from flask_fixtures import load_fixtures

# Destroy
db.drop_all()
# Recreate Structure
db.create_all()

# Import fixture data
for fixture_dir in app.config.get('FIXTURES_DIRS', ['./app/fixtures']):
  for fixture_file in glob.glob(fixture_dir + '/*.json'):
    fixtures = JSONLoader().load(fixture_file)
    load_fixtures(db, fixtures)
