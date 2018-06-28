from flask import jsonify, make_response
from app.api.models.models import requests, response_msg, response_fail
from flask import jsonify, make_response



def help_create_ride_offer():
    content = jsonify([{'content':requests},{'status':response_msg}])
    return content

def help_request_to_join_a_ride(id):
    for info in requests  :
        if info["id"] == int(id):
            content = jsonify([{'content':info}, {'status':response_msg}])
            return content
            #con = offers[0]
            #cont1 = con[id] 