from flask import Blueprint, request, jsonify
from first_screening.controllers.topic_controller import TopicController
from first_screening.controllers.content_controller import ContentController
from first_screening.utils.helper import token_required

router = Blueprint("router", __name__)

# Ping
@router.route("/ping", methods=["GET"])
@token_required(allowed_guest=False)
def ping(current_user):
    return jsonify({})


# Topic routes --
@router.route("/", methods=["GET"])
def get_topics():
    return TopicController.all()


@router.route("/<name_id>", methods=["GET"])
def get_topic(name_id):
    return TopicController.find(name_id)


@router.route("/", methods=["POST"])
@token_required(allowed_guest=False)
def create_topic(current_user):
    data = request.get_json()
    return TopicController.create(data)


@router.route("/<name_id>", methods=["PUT"])
@token_required(allowed_guest=False)
def update_topic(current_user, name_id):
    data = request.get_json()
    return TopicController.update(name_id, data)


@router.route("/<name_id>", methods=["DELETE"])
@token_required(allowed_guest=False)
def delete_topic(currennt_user, name_id):
    return TopicController.delete(name_id)


# Content routes --
@router.route("/<name_id>/<sequence_number>", methods=["GET"])
def get_content(name_id, sequence_number):
    return ContentController.find(name_id, sequence_number)


@router.route("/<name_id>", methods=["POST"])
@token_required(allowed_guest=False)
def create_content(current_user, name_id):
    data = request.get_json()
    return ContentController.create(name_id, data)


@router.route("/<name_id>/<sequence_number>", methods=["PUT"])
@token_required(allowed_guest=False)
def update_content(current_user, name_id, sequence_number):
    data = request.get_json()
    return ContentController.update(name_id, sequence_number, data)


@router.route("/<name_id>/<sequence_number>", methods=["DELETE"])
@token_required(allowed_guest=False)
def delete_content(current_user, name_id, sequence_number):
    return ContentController.delete(name_id, sequence_number)
