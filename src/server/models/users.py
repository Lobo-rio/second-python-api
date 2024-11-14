from flask_restx import fields

from server.instance import server

model_users = server.api.model('ResponseUsers', {
    'id': fields.String(readonly=True, description='The user unique identifier.'),
    'name': fields.String(required=True, min_length=1, max_length=80, description='Name of the registered user.' ),
    'email': fields.String(required=True, min_length=1, max_length=120, description='Email of the registered user.' ),
    'phone': fields.Integer(required=True, min_length=1, max_length=9, description='Phone of the registered user.' )
})