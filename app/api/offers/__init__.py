from flask import Blueprint
from flask_restful import Api
from app.api.offers import pushoffers, pushsingleoffers
cont = Blueprint('cont',__name__)
my_app = Api(cont)
my_app.add_resource(pushoffers,'/api/v1/rides')
my_app.add_resource(pushsingleoffers,'/api/v1/rides/<id>')

