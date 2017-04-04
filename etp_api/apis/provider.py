from flask_restplus import Namespace, Resource, fields
from etp_api.database import model

api = Namespace('provider', description='Providers related operations')

provider = api.model('Provider', {
    'provider_id': fields.String(required=True, description='The provider identifier'),
    'provider_name': fields.String(required=True, description='The provider name'),
    'provider_type': fields.String(required=True, description='The provider type'),
    })


@api.route('/')
class ProviderList(Resource):
    @api.doc('list_providers')
    @api.marshal_list_with(provider)
    def get(self):
        '''
        List all providers
        Get all training providers.
        '''
        return model.get_all_providers()

@api.route('/<id>')
@api.param('id', 'The provider identifier')
@api.response(404, 'Provider not found')
class Provider(Resource):
    @api.doc('get provider')
    @api.marshal_with(provider)
    def get(self, id):
        '''Fetch a provider given its identifier'''
        # try:
            return model.get_provider(id)
        # except:
        #     api.abort(404)
