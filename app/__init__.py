from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, static_url_path='/static')

app.config.from_object('config.MainConfig')

db = SQLAlchemy(app) #flask-sqlalchemy
migrate = Migrate(app, db)

from app import views, models, schemas
