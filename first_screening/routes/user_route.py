from flask import Blueprint, request
from first_screening.controllers.user_controller import UserController

user = Blueprint("user", __name__)


@user.route("/login", methods=["GET"])
def login():
    auth = request.authorization
    return UserController.login(auth)


@user.route("/generate_user", methods=["GET"])
def generate_user():
    return UserController.generate_user()
