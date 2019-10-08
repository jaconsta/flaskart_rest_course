from flask import Flask
from flask_cors import CORS

from routes import register_routes
from connections.db import db


def create_app(db_url='sqlite:///flaskart.sqlite'):
    app = Flask(__name__, static_url_path='')
    db.connect(db_url)
    register_routes(app)

    return app


if __name__ == '__main__':
    app = create_app()
    CORS(app)

    @app.teardown_request
    def remove_db_session(ex=None):
        # session.remove()
        db.disconnect()

    app.run(port=8000, debug=True, use_reloader=True)
