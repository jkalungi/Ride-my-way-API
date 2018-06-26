from flask import jsonify, make_response
from app.api.models.models import offers, response_msg, response_fail
from flask import jsonify, make_response



def help_send_offers():
    Content = jsonify([{'content':offers},{'status':response_msg}])
return Content

def help_send_oneoffer(id):
    for info in offers :
        if info["id"] == int(id):
            content = jsonify([{'content':info}, {'status':response_msg}])
            return content
            #con = offers[0]
            #cont1 = con[id]
            return jsonify({'status':response_fail})