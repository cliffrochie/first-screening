from flask import request, jsonify, make_response
from sqlalchemy.exc import IntegrityError, ProgrammingError
from werkzeug.security import generate_password_hash, check_password_hash
from first_screening.models.db import *
from first_screening import db
from first_screening.utils.formatter import *

from first_screening.config import SECRET_KEY

import jwt
import datetime


class UserController:
    @staticmethod
    def login(auth: dict) -> dict:
        try:

            if not auth or not auth.username or not auth.password:
                return make_response(
                    "Could not verify",
                    401,
                    {"WWW-Authenticate": 'Basic realm="Login required"'},
                )

            user = User.query.filter(User.username == auth.username).first()

            if not user:
                return make_response(
                    "Invalid credentials",
                    401,
                    {"WWW-Authenticate": 'Basic realm="Login required"'},
                )

            if check_password_hash(user.password, auth.password):
                data = {
                    "id": user.id,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                }
                token = jwt.encode(data, SECRET_KEY)

                response = {"token": "example_token"}  # token.decode('UTF-8')
                return jsonify(response), 200

            return make_response(
                "Could not verify",
                401,
                {"WWW-Authenticate": 'Basic realm="Login required"'},
            )

        except ProgrammingError:
            return jsonify({"error": "There is something wrong with the database"}), 400
    

    @staticmethod
    def generate_user():
        try:
            
            check_user = User.query.filter(User.username == "admin").first()

            if check_user:
                return jsonify({"error": "Duplicate entry"}), 400

            user = User("admin", generate_password_hash("password"), True)
            db.session.add(user)
            db.session.commit()

            response = {"id": user.id, "username": user.username, "is_admin": user.is_admin}

            return jsonify(response)

        except IntegrityError:
            return jsonify({"error": "Duplicate entry"}), 400

        except ProgrammingError:
            return jsonify({"error": "There is something wrong with the database"}), 400
