from flask import Flask
from flask_restx import Api, Resource

from server.instance import server

app, api = server.app, server.api

@api.route('/books')
class BooList(Resource):
    def get(self, ):
        return {
            'books': [
                {
                  'id': 1,
                  'title': 'War and Peace'
                },
                {
                  'id': 2,
                  'title': 'War and Goalang'
                }
            ]
        }