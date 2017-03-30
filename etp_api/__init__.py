from flask import Flask
from .apiv0 import blueprint as apiv0

app = Flask(__name__)
app.register_blueprint(apiv0)
