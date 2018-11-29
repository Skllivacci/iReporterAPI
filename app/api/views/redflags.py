from flask_restful import Resource
from flask import jsonify, make_response, request, abort

import datetime

incidents = [] 

class RedFlags(Resource):
    """docstring for RedFlags"""
    
    def __init__(self):
        self.db = incidents
        self.id = len(incidents) + 1
       
    
    def post(self):
        
        data = {
            'id' : self.id,
            'createdOn' : datetime.datetime.utcnow(),
            'createdBy' : request.json['createdBy'],
            'type' : 'red-flags',
            'location' : request.json['location'],
            'status' : "Under Investigation",
            'images' : request.json['images'],
            'videos' : request.json['videos'],
            'title' : request.json['title'],
            'comment' : request.json['comment']
        }
        self.db.append(data)
        
        success_message = {
            'id' : self.id,
            'message' : 'Thank You for Creating a Red-Flag'
        }

        return make_response(jsonify({
            "status" : 201,
            "data" : success_message
        }), 201)

    def get(self):

        return make_response(jsonify({
            "status" : 200,
            "data" : self.db
        }), 200) 


class RedFlag(Resource):
    """docstring of RedFlag"""
    def __init__(self):
        self.db = incidents
        self.id = len(incidents) + 1
    def get(self, redflag_id):

        for incident in incidents:
            if incident['id'] == redflag_id:
                return make_response(jsonify({
                    "status" : 200,
                    "data" : incident
                }), 200)
       