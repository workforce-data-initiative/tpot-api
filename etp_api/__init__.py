from flask import Flask
from etp_api.apis import api

app = Flask(__name__)
api.init_app(app)
