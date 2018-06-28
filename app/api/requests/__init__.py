from flask import Blueprint
from flask_restful import Api
from app.api.models.requests.requests import createrideoffer, requestride
cont = Blueprint('cont',__name__)
my_app = Api(cont)
my_app.add_resource(createrideoffer,'/api/v1/rides')
my_app.add_resource(requestride,'/api/v1/rides/<rideId>/request')