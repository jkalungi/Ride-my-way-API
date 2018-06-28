from flask import Blueprint
from flask_restful import Api
from requests.views import createrideoffer, requestride

requests = Blueprint('requests',__name__)
my_app = Api(requests)
my_app.add_resource(createrideoffer,'/api/v1/rides')
my_app.add_resource(requestride,'/api/v1/rides/<rideId>/request')