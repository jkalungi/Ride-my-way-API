from flask import jsonify, make_response
from flask_restful import Resource, reqparse

import re
import json

from app.api.models.requests import Request



request_list=[]
class CreateRideOffer(Resource):
    id=0
    def post(self):
        """
        Allows authenticated user to make an request from the menu
        token is required to get user Id
        """
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('date', type=str, required=True)
        args = parser.parse_args()
        
        global id():
                if len(request_list)==0:
                    id = len(request_list)+1
                else:
                    id = id+1

                new_request = Request(id, title, description, date)

                for request in request_list:
                    if title == request['title']:
                        return make_response(jsonify({"message": 'Request title already exists'}), 400)
                request = json.loads(new_request.json())
                request_list.append(request)
                return make_response(jsonify({
                    'message': 'Request successfully created and sent',
                    'status': 'success'},
                ), 201)
        return make_response(jsonify({"message": "Doesn't exist, Create an account please"}), 401)


class RequestRide(Resource):
    def post(self, request_id):
        """
        Returns an request made by authenticated user
        token is required to get user Id
        """
        parser = reqparse.RequestParser()
        parser.add_argument('token', location='headers')
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('date', type=str, required=True)
            return make_response(jsonify({"message": "Token is missing"}), 401)
        decoded = decode_token(args['token'])
        if decoded["status"] == "Failure":
            return make_response(jsonify({"message": decoded["message"]}), 401)

        for request in request_list:
            if int(request['id']) == int(request_id):
                args = parser.parse_args()
                request['title'] = args['title']
                request['description'] = args['description']
                request['department'] = args['department']
                return make_response(jsonify({"message": "request updated succesfully"}), 201)
        return make_response(jsonify({"message": "request not found"}), 404)