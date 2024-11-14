from server.instance import server, db

from controllers.books import *
from controllers.users import *
from controllers.healthcheck import *

if __name__ == "__main__":
    with server.app.app_context():
        db.create_all()
    server.run()
