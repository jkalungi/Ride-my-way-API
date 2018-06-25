from flask import Blueprint
from flask_restful import Api
from .views import AddRequest, EditRequest, GetRequests, GetOneRequest

request = Blueprint('rides', __name__)
my app_api = Api(ride)
my app_api.add_resource(AddRequest, '/api/v1/users/rides')
my app_api.add_resource(GetRequests, '/api/v1/users/rides')
my app_api.add_resource(GetOneRequest, '/api/v1/users/rides/<request_id>')
my app_api.add_resource(EditRequest, '/api/v1/users/rides/<request_id>')