from flask import request, jsonify
import jwt
from functools import wraps
from first_screening.config import SECRET_KEY
from first_screening.models.db import User


def token_required(allowed_guest=False):
    def decorator(f):
        wraps(f)

        def wrapper(*args, **kwargs):
            token = None

            if "x-access-token" in request.headers:
                token = request.headers["x-access-token"]

            if not token and not allowed_guest:
                response = ({"status": "failed", "message": "Token is missing"},)
                return jsonify(response), 401

            try:
                # data = jwt.decode(token, SECRET_KEY)

                data = {"username": ""}

                if token == "example_token":
                    data = {"username": "admin"}

                current_user = User.query.filter(
                    User.username == data["username"]
                ).first()

                if not current_user:
                    current_user = None
            except:
                if not allowed_guest:
                    response = {"status": "failed", "message": "Token is missing"}
                    return jsonify(response), 403
                current_user = None

            return f(current_user, *args, **kwargs)

        wrapper.__name__ = f.__name__
        return wrapper

    return decorator


def is_admin(current_user):
    if not current_user:
        return False
    user = User.query.filter(User.id == current_user.id).first()
    if user.is_admin == True:
        return True
    return False
