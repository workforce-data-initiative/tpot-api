from flask_restplus import Namespace, Resource, fields

api = Namespace('program', description='Program related operations')

program = api.model('Program', {
    'provider_id': fields.String(required=True, description='The provider identifier'),
    'name': fields.String(required=True, description='The program name'),
    })

PROGRAMS = [
        {'provider_id': '112', 'name': 'Program A'},
        {'provider_id': '112', 'name': 'Program B'},
        {'provider_id': '112', 'name': 'Program C'},
        {'provider_id': '113', 'name': 'Program A'},
        {'provider_id': '113', 'name': 'Program B'}
        ]


@api.route('/<provider_id>')
@api.param('provider_id', 'The provider identifier')
@api.response(404, 'Provider not found')
class Provider(Resource):
    @api.doc('get all programs from the provider')
    @api.marshal_list_with(program)
    def get(self, provider_id):
        '''Fetch all programs given the provider's identifier'''
        programs = []
        for p in PROGRAMS:
            if p['provider_id'] == provider_id:
                programs.append(p)
        return programs
        api.abort(404)
