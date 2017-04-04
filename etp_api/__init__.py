from flask import Flask
from .apiv0 import blueprint as apiv0
from flask_sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku

app = Flask(__name__)
app.register_blueprint(apiv0)

heroku = Heroku(app)
db = SQLAlchemy(app)
