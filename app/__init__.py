from flask import Flask
from flask_restful import Api, Resource

#local imports
from .api.v1.views.redflags import RedFlags, RedFlag

def create_app():
    app = Flask(__name__)
    api = Api(app)
    # The add_resource function registers the routes with the framework using the given endpoint
    api.add_resource(RedFlags, '/api/v1/red-flags')  #for the list of redflags
    api.add_resource(RedFlag, '/api/v1/red-flags/<int:redflag_id>') #for an individual red-flag
    return app 