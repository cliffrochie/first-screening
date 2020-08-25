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
@router.route("/topics", methods=["GET"])
def get_topics():
    return TopicController.all()


@router.route("/topics/<topic_id>", methods=["GET"])
def get_topic(topic_id):
    return TopicController.find(topic_id)


@router.route("/topics", methods=["POST"])
@token_required(allowed_guest=False)
def create_topic(current_user):
    data = request.get_json()
    return TopicController.create(data)


@router.route("/topics/<topic_id>", methods=["PUT"])
@token_required(allowed_guest=False)
def update_topic(current_user, topic_id):
    data = request.get_json()
    return TopicController.update(topic_id, data)


@router.route("/topics/<topic_id>", methods=["DELETE"])
@token_required(allowed_guest=False)
def delete_topic(current_user, topic_id):
    return TopicController.delete(topic_id)


# Content routes --
@router.route("/topics/<topic_id>/<sequence_number>", methods=["GET"])
def get_content(topic_id, sequence_number):
    return ContentController.find(topic_id, sequence_number)


@router.route("/topics/<topic_id>", methods=["POST"])
@token_required(allowed_guest=False)
def create_content(current_user, topic_id):
    data = request.get_json()
    return ContentController.create(topic_id, data)


@router.route("/topics/<topic_id>/<sequence_number>", methods=["PUT"])
@token_required(allowed_guest=False)
def update_content(current_user, topic_id, sequence_number):
    data = request.get_json()
    return ContentController.update(topic_id, sequence_number, data)


@router.route("/topics/<topic_id>/<sequence_number>", methods=["DELETE"])
@token_required(allowed_guest=False)
def delete_content(current_user, topic_id, sequence_number):
    return ContentController.delete(topic_id, sequence_number)
