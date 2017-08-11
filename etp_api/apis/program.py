from flask_restplus import Namespace, Resource, fields
from etp_api.database import model

api = Namespace('program', description='Program related operations')

program = api.model('Program', {
    'program_cip': fields.String(
        required=True, description='The program CIP code'),
    'program_type': fields.String(
        required=True, description='The program type'),
    })


@api.route('/<int:provider_id>')
@api.param('provider_id', 'The provider identifier')
@api.response(404, 'Program not found')
class Program(Resource):
    @api.doc('get all programs from the provider')
    @api.marshal_list_with(program)
    def get(self, provider_id):
        '''Fetch all programs given the provider's identifier'''
        try:
            return model.get_programs_for_provider(provider_id)
        except:
            api.abort(404)
