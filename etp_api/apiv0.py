from flask import Blueprint
from flask_restplus import Api

from .apis.provider import api as provider
from .apis.program import api as program
from .apis.outcome import api as outcome

blueprint = Blueprint('api', __name__, url_prefix='/api/v0')
api = Api(blueprint,
        title='ETP-API',
        version='0.1',
        description='API service for training providers and programs'
        )

api.add_namespace(provider)
api.add_namespace(program)
api.add_namespace(outcome)
