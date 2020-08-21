from flask import request, jsonify
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from first_screening.models.db import *
from first_screening import db
from first_screening.utils.formatter import *


class ContentControllerError(Exception):
    """An exception for ContentController"""


class ContentController:
    @staticmethod
    def find(name_id, sequence_number):
        try:
            content = (
                Content.query.filter(Content.sequence_number == sequence_number)
                .join(Topic, Topic.id == Content.topic_id)
                .filter(Topic.name_id == name_id)
                .first()
            )

            if not content:
                return jsonify({"error": "Content not found"}), 404

            return jsonify(format_content(content))

        except AttributeError:
            raise ContentControllerError("Invalid attribute")

    @staticmethod
    def create(name_id, data):
        try:
            topic = Topic.query.filter(Topic.name_id == name_id).first()

            content = Content(
                data["sequence_number"], data["title"], data["body"], topic.id
            )
            db.session.add(content)
            db.session.commit()

            return jsonify(format_content(content))
        except AttributeError:
            raise ContentControllerError("Invalid attribute")

        except KeyError:
            raise ContentControllerError("Data is missing")

        except TypeError:
            raise ContentControllerError("TypeError")

        except InvalidRequestError:
            db.session.rollback()

    @staticmethod
    def update(name_id, sequence_number, data):
        try:

            content = (
                Content.query.filter(Content.sequence_number == sequence_number)
                .join(Topic, Topic.id == Content.topic_id)
                .filter(Topic.name_id == name_id)
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
            raise ContentControllerError("Key error, double check the data.")

        except AttributeError:
            raise ContentControllerError("Attribute might be missing, or mispelled")

    @staticmethod
    def delete(name_id, sequence_number):
        content = (
            Content.query.filter(Content.sequence_number == sequence_number)
            .join(Topic, Topic.id == Content.topic_id)
            .filter(Topic.name_id == name_id)
            .first()
        )

        if not content:
            return jsonify({"error": "Content not found"}), 404

        db.session.delete(content)
        db.session.commit()

        return jsonify({}), 204
