__version__ = "0.1.0"

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

db = SQLAlchemy()

def create_app():
    from first_screening.routes.data.data_route import data
    from first_screening.routes.main_route import router
    from first_screening.routes.user_route import user

    app = Flask(__name__)

    if not database_exists("mysql://root@localhost/screening"):
        create_database("mysql://root@localhost/screening")

    app.register_blueprint(data, url_prefix="/data")
    app.register_blueprint(router, url_prefix="/api")
    app.register_blueprint(user, url_prefix="/api")

    app.config.from_object("first_screening.config")

    db.init_app(app)

    with app.test_request_context():
        db.create_all()

    return app
