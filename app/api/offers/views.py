from flask import jsonify, make_response
from flask_restful import Resource
from app.api.offers.helper import help_send_offers,help_send_oneoffer

class pushoffers(Resource):
    def get(self):
        return help_send_offers()

class pushsingleoffers(Resource):
    def get(self,id):
        return help_send_oneoffer




