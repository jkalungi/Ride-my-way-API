from flask import jsonify, make_response
from flask_restful import Resource
from app.api.requests.helper import help_create_rideoffer,help_request_to_join_a_ride

class createrideoffer(Resource):
    def get(self):
        return help_create_rideoffer()

class requestride(Resource):
    def get(self,id):
        return help_request_to_join_a_ride(id)
