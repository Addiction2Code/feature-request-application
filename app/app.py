# from flask import Flask, render_template, request, jsonify, _app_ctx_stack
# from sqlite3 import dbapi2 as sqlite3
#
# ## Helpers
# def init_db():
#   with app.app_context():
#     db = get_db()
#     with app.open_resource('schema.sql') as f:
#       db.cursor().executescript(f.read())
#     db.commit()
#
# def get_db():
#   top = _app_ctx_stack.top
#   if not hasattr(top, 'sqlite_db'):
#     top.sqlite_db = sqlite3.connect(app.config['DATABASE'])
#     top.sqlite_db.row_factory = sqlite3.Row
#   return top.sqlite_db
#
# @app.teardown_appcontext
# def close_database(exception):
#   top = _app_ctx_stack.top
#   if hasattr(top, 'sqlite_db'):
#     top.sqlite_db.close()
