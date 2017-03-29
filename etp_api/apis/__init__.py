from flask_restplus import Api

from .provider import api as provider
from .program import api as program

api = Api(
        title='ETP-API',
        version='1.0',
        description='API service for training providers and programs'
        )

api.add_namespace(provider)
api.add_namespace(program)
