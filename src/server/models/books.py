from flask_restx import fields

from server.instance import server

model_books = server.api.model('ResponseBooks', {
    'id': fields.String(readonly=True, description='The book unique identifier.'),
    'title': fields.String(required=True, min_length=1, max_length=120, description='Title of the registered book.' ),
    'author': fields.String(required=True, min_length=1, max_length=80, description='Title of the registered book.' ),
    'description': fields.String(required=True, min_length=1, max_length=255, description='Title of the registered book.' )
})