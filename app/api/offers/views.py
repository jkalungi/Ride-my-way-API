from app.models import offers

from flask import jsonify, make_response
from flask_restful import Resource

class PushOffers(Resource):
    def get(self):
        data = {"offers_many":offers}


