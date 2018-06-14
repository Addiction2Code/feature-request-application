from flask import Flask, render_template, request, jsonify, _app_ctx_stack
from sqlite3 import dbapi2 as sqlite3

DATABASE = 'main.db'
SECRET_KEY = 'TOrETxWg5BNkYVLjypZlSoI0M2hJMtX5NznZ4WebfFYd4GE9PnG7zPQeurkysOHD'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

## Helpers
def init_db():
  with app.app_context():
    db = get_db()
    with app.open_resource('schema.sql') as f:
      db.cursor().executescript(f.read())
    db.commit()

def get_db():
  top = _app_ctx_stack.top
  if not hasattr(top, 'sqlite_db'):
    top.sqlite_db = sqlite3.connect(app.config['DATABASE'])
    top.sqlite_db.row_factory = sqlite3.Row
  return top.sqlite_db

@app.teardown_appcontext
def close_database(exception):
  top = _app_ctx_stack.top
  if hasattr(top, 'sqlite_db'):
    top.sqlite_db.close()

## Routes
## Reference: REST API Design Rulebook
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/feature-requests')
def feature_requests():
  db = get_db()
  cur = db.execute('select title, description from feature_requests order by id asc')
  entries = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
  return jsonify(feature_requests=entries)

@app.route('/feature-requests/new', methods=['POST'])
def new_feature_request():
  db = get_db()
  cur = db.execute('insert into feature_requests (title, description) values (?, ?)',
         [request.json['title'], request.json['description']])
  db.commit()
  id = cur.lastrowid
  return jsonify({"title": request.json['title'],
          "description": request.json['description'],
          "id": id})

## Let's get started!
if __name__ == '__main__':
  init_db()
  app.run()
