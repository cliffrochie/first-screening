from flask import request, jsonify
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from first_screening.models.db import *
from first_screening import db
from first_screening.utils.formatter import *


class TopicControllerError(Exception):
    """For TopicController errors"""


class TopicController:
    @staticmethod
    def all():
        try:
            topics = Topic.query.all()

            if not topics:
                return jsonify({"error": "Topics not found"}), 404

            data = {}
            result = []

            for topic in topics:
                result.append(format_topic(topic))

            data = {"data": result}

            return jsonify(data)

        except AttributeError:
            return jsonify({"error": "No topics found"}), 404

    @staticmethod
    def find(name_id):
        topic = Topic.query.filter(Topic.name_id == name_id).first()

        if not topic:
            return jsonify({"error": "Topic not found"}), 404

        return jsonify(format_topic(topic))

    @staticmethod
    def create(data):
        try:

            topic = Topic(data["name"], data["description"])
            db.session.add(topic)
            db.session.commit()

            return jsonify(format_topic(topic))

        except AssertionError as e:
            raise TopControllerError("Data needed to submit") from e

        except AttributeError as e:
            raise TopicControllerError("Request has no attribute") from e

        except KeyError as e:
            raise TopicControllerError("Missing key") from e

        except InvalidRequestError as e:
            raise TopicControllerError("Invalid request") from e

        except IntegrityError as e:
            raise TopicControllerError(
                "Integrity Error: Duplicate entry of data"
            ) from e

    @staticmethod
    def update(name_id, data):
        if not data:
            return jsonify({"error": "No data submitted"}), 400

        topic = Topic.query.filter(Topic.name_id == name_id).first()
        topic.name_id = format_name_id(data["name"])
        topic.name = data["name"]
        topic.description = data["description"]

        db.session.commit()

        return jsonify(format_topic(topic))

    @staticmethod
    def delete(id):
        topic = Topic.query.filter(Topic.name_id == id).first()

        if not topic:
            return jsonify({"error": "Topic not found"}), 404

        db.session.delete(topic)
        db.session.commit()

        return jsonify({}), 204
