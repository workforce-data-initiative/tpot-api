from flask_restplus import Namespace, Resource, fields
from etp_api.database import model

api = Namespace('program', description='Program related operations')

program = api.model('Program', {
    'provider_id': fields.String(required=True, description='The provider identifier'),
    'name': fields.String(required=True, description='The program name'),
    })


@api.route('/<provider_id>')
@api.param('provider_id', 'The provider identifier')
@api.response(404, 'Provider not found')
class Program(Resource):
    @api.doc('get all programs from the provider')
    @api.marshal_list_with(program)
    def get(self, provider_id):
        '''Fetch all programs given the provider's identifier'''
        try:
            return model.get_programs_for_provider(provider_id)
        except:
            api.abort(404)
