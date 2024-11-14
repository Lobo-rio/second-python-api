from flask import Flask
from flask_restx import Api, Resource
from sqlalchemy.sql import text
from datetime import datetime

from server.instance import server, db

app, api = server.app, server.api

healthcheckNS = api.namespace('healthcheck', description='HealthCheck operations')

@healthcheckNS.route('/', endpoint='HealthCheck')
class HealthCheck(Resource):
    @healthcheckNS.doc('root_route')
    def get(self):
        date_hour = datetime.now().isoformat()
                                                                               
        return {
            'datetime': date_hour,
            'message': 'System On line'
        }

@healthcheckNS.route('/db-status', endpoint='DBStatus')
class DBStatus(Resource):
    @healthcheckNS.doc('db_status')
    def get(self):
        try:
            result = db.session.execute(text("SELECT datetime('now')")).fetchone()
            db_time = result[0] if result else 'Unknown'
            return {
                'status': 'Database is online',
                'db_time': db_time
            }
        except Exception as e:
            return {
                'status': 'Database is offline',
                'error': str(e)
            }, 500
