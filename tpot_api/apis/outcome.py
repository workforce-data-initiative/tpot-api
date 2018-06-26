from flask_restplus import Namespace, Resource, fields
from tpot_api.database import model

api = Namespace('outcome', description='TPOT outcome scorecards')


@api.route('/<int:provider_id>/<int:program_id>')
@api.param('provider_id', 'The provider identifier')
@api.param('program_id', 'The program CIP code')
@api.response(404, 'Program not found')
class Program(Resource):
    @api.doc("get TPOT scorecard for a provider's program")
    def get(self, provider_id, program_id):
        '''Fetch all programs given the provider's identifier'''
        try:
            return model.get_outcomes_for_program(provider_id, program_id)
        except:
            api.abort(404)
