from flask import Flask, jsonify, request
from flask_restx import Api, Resource

from server.instance import server, db
from server.sqlite import Users
from server.models.users import model_users

app, api = server.app, server.api

usersNS = api.namespace('users', description='Users operations')

@usersNS.route('/', endpoint='Users')
class UserList(Resource):
    @usersNS.doc('list_users')
    @usersNS.marshal_list_with(model_users)
    def get(self):
        users = Users.query.all()
    
        return [user.to_dict() for user in users]
    
    @usersNS.doc('create_user')
    @usersNS.expect(model_users)
    def post(self):
        name = request.json['name']
        email = request.json['email']
        phone = request.json['phone']

        user_existed = Users.query.filter_by(email = email).first()
        if user_existed:
            return {'error': 'User already exists!'}, 400
    
        user = Users(name=name, email=email, phone=phone)
        db.session.add(user)
        db.session.commit()

        return user.to_dict(), 201
    
@usersNS.route('/<int:id>')
@usersNS.response(404, 'User not found')
@usersNS.param('id', 'The user identifier')
class User(Resource):
    @usersNS.doc('get_user')
    def get(self, id):
        user_existed = Users.query.get(id)
        if not user_existed:
            return {'error': 'User does not exist!'}, 404
    
        return user_existed.to_dict(), 200

    @usersNS.doc('delete_user')
    @usersNS.response(204, 'User deleted')
    def delete(self, id):
        user_existed = Users.query.get(id)
        if not user_existed:
            return {'error': 'User does not exist!'}, 404
    
        db.session.delete(user_existed)
        db.session.commit()

        return '', 204

    @usersNS.doc('update_user')
    @usersNS.expect(model_users)
    def put(self, id):
        user_existed = Users.query.get(id)
        if not user_existed:
            return {'error': 'User does not exist!'}, 404
    
        user_existed.name = request.json['name']
        user_existed.email = request.json['email']
        user_existed.phone = request.json['phone']
        db.session.commit()

        return user_existed.to_dict(), 200
