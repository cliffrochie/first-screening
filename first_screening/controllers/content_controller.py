from flask import request, jsonify
from sqlalchemy.exc import IntegrityError, InvalidRequestError, ProgrammingError
from first_screening.models.db import *
from first_screening import db
from first_screening.utils.formatter import *


class ContentControllerError(Exception):
    """An exception for ContentController"""


class ContentController:
    @staticmethod
    def find(topic_id: int, sequence_number: int) -> dict:
        try:

            content = (
                Content.query.filter(Content.sequence_number == sequence_number)
                .join(Topic, Topic.id == Content.topic_id)
                .filter(Topic.id == topic_id)
                .first()
            )

            if not content:
                return jsonify({"error": "Content not found"}), 404

            return jsonify(format_content(content))

        except AttributeError:
            raise ContentControllerError("Invalid attribute")

        except ProgrammingError:
            return jsonify({"error": "There is something wrong with the server"}), 400

    @staticmethod
    def create(topic_id: int, data: dict) -> dict:
        try:

            topic = Topic.query.get(topic_id)

            if not topic:
                return jsonify({"error": "Topic not found"}), 404

            content = Content(
                data["sequence_number"], data["title"], data["body"], topic.id
            )
            db.session.add(content)
            db.session.commit()

            return jsonify(format_content(content))

        except AttributeError:
            return jsonify({"error": "Invalid attribute."}), 400

        except KeyError:
            return jsonify({"error": "Wrong key or data is missing."}), 400
            raise ContentControllerError("Data is missing")

        except TypeError:
            return jsonify({"error": "You either submit it to wrong method request or submitted an empty data."}), 400

        except InvalidRequestError:
            db.session.rollback()
            return jsonify({"error": "Invalid request"}), 400

        except ProgrammingError:
            return jsonify({"error": "There is something wrong with the server"}), 400

    @staticmethod
    def update(topic_id: int, sequence_number: int, data: dict) -> dict:
        try:

            content = (
                Content.query.filter(Content.sequence_number == sequence_number)
                .join(Topic, Topic.id == Content.topic_id)
                .filter(Topic.id == topic_id)
                .first()
            )

            if not content:
                return jsonify({"error": "Content not found"}), 404

            content.sequence_number = data["sequence_number"]
            content.title = data["title"]
            content.body = data["body"]

            db.session.commit()

            return jsonify(format_content(content))

        except KeyError:
            return jsonify({"error": "Invalid or missing key from the data"}), 400

        except AttributeError:
            return jsonify({"error": "Attribute might be missing, or mispelled"}), 400

        except ProgrammingError:
            return jsonify({"error": "There is something wrong with the server"}), 400

    @staticmethod
    def delete(topic_id: int, sequence_number: int) -> dict:
        try:

            content = (
                Content.query.filter(Content.sequence_number == sequence_number)
                .join(Topic, Topic.id == Content.topic_id)
                .filter(Topic.id == topic_id)
                .first()
            )

            if not content:
                return jsonify({"error": "Content not found"}), 404

            db.session.delete(content)
            db.session.commit()

            return jsonify({}), 204

        except ProgrammingError:
            return jsonify({"error": "There is something wrong with the server"}), 400
