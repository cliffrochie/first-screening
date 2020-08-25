from flask import request, jsonify
from sqlalchemy.exc import IntegrityError, InvalidRequestError, ProgrammingError
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

            result = []

            for topic in topics:
                data = format_topic(topic)
                data['contents'] = []
                for content in topic.content:
                    data['contents'].append(format_content(content))
                result.append(data)

            return jsonify(result)
   
        except AttributeError:
            return jsonify({"error": "No topics found"}), 404

        except ProgrammingError:
            return jsonify({"error": "There is something wrong with the server"}), 400

        

    @staticmethod
    def find(topic_id: int) -> dict:
        try:

            topic = Topic.query.get(topic_id)

            if not topic:
                return jsonify({"error": "Topic not found"}), 404
            
            result = format_topic(topic)
            result['contents'] = []
            for content in topic.content:
                result['contents'].append(format_content(content))

            return jsonify(result)

        except ProgrammingError:
            return jsonify({"error": "There is something wrong with the server"}), 400

    @staticmethod
    def create(data: dict) -> dict:
        try:
            
            check_topic = Topic.query.filter(Topic.name == data["name"]).first()

            if check_topic:
                return jsonify({"error": "Duplicate entry"}), 400

            topic = Topic(data["name"], data["description"])
            db.session.add(topic)
            db.session.commit()

            return jsonify(format_topic(topic))

        except TypeError as e:
            return jsonify({"error": "No data submitted"}), 400

        except AssertionError as e:
            return jsonify({"error": "Data needed to submit"}), 400

        except AttributeError as e:
            return jsonify({"error": "Request has no attribute"}), 400

        except KeyError as e:
            return jsonify({"error": "Invalid or missing key from the data"}), 400

        except InvalidRequestError as e:
            return jsonify({"error": "Invalid request"}), 400

        except IntegrityError as e:
            db.session.rollback()

            if "Duplicate entry" in str(e):
                return jsonify9({"error": "Duplicate entry"}), 400

        except ProgrammingError:
            return jsonify({"error": "There is something wrong with the server"}), 400

    @staticmethod
    def update(topic_id: int, data: dict) -> dict:
        try:

            if not data:
                return jsonify({"error": "No data submitted"}), 400

            topic = Topic.query.get(topic_id)
            topic.name = data["name"]
            topic.description = data["description"]

            db.session.commit()

            return jsonify(format_topic(topic))
            
        except ProgrammingError:
            return jsonify({"error": "There is something wrong with the server"}), 400

    @staticmethod
    def delete(topic_id: int) -> dict:
        try:

            topic = Topic.query.get(topic_id)

            if not topic:
                return jsonify({"error": "Topic not found"}), 404

            db.session.delete(topic)
            db.session.commit()

            return jsonify({}), 204

        except ProgrammingError:
            return jsonify({"error": "There is something wrong with the server"}), 400
