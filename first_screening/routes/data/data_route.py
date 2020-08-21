from flask import Blueprint, jsonify
from first_screening import db
from first_screening.models.db import *
from first_screening.utils.data import topics

data = Blueprint("data", __name__)


def insert_data():
    for data in topics:
        topic = Topic(data["name"], data["description"])
        db.session.add(topic)
        db.session.commit()

        for content in data["content"]:
            content = Content(
                content["sequence_number"], content["title"], content["body"], topic.id
            )
            db.session.add(content)
            db.session.commit()

    user1 = User("John Doe", True)
    user2 = User("John Smith", False)
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()


@data.route("/populate-data", methods=["GET"])
def populate_data():
    insert_data()
    return jsonify({"message": "data inserted successfully"})


@data.route("/remove-data", methods=["GET"])
def remove_data():
    Content.query.delete()
    Topic.query.delete()
    User.query.delete()
    db.session.commit()

    return jsonify({"message": "data removed successfully"})
