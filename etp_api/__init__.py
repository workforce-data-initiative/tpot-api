from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku

app = Flask(__name__)

heroku = Heroku(app)
db = SQLAlchemy(app)

from .apiv0 import blueprint as apiv0
app.register_blueprint(apiv0)

@app.route('/')
def redirect():
    return redirect("/api/v0", code=302)
