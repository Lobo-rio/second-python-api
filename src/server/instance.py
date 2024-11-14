from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app, 
            version='1.0.0',
            title='Second Python API',
            description='Rest API, developed for the purpose of studying and understanding the Python language and its ecosystem.',
            doc='/docs'
        )

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///second_database.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db = SQLAlchemy(self.app)
        
    def run(self, ):
        self.app.run(
            debug=True
        )

server = Server()
db = server.db