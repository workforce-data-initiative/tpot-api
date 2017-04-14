from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku

app = Flask(__name__)

heroku = Heroku(app)
db = SQLAlchemy(app)

from .apiv0 import blueprint as apiv0
app.register_blueprint(apiv0)

@app.route('/')
def index():
    return redirect(url_for('api.doc'), code=302)
