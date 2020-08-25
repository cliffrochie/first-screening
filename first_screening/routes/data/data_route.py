from flask import Blueprint, jsonify
from first_screening import db
from first_screening.models.db import *
from first_screening.utils.data import topics
import mysql.connector

data = Blueprint("data", __name__)


@data.route('/generate-db', methods=['GET'])
def create_db():
    try:

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )

        with conn.cursor() as cursor:
            cursor.execute("DROP DATABASE IF EXISTS screening")
            cursor.execute("CREATE DATABASE screening")

        conn.close()

        return jsonify({"message": "database created successfully"})

    except ProgrammingError:
        return jsonify({"error": "There is something wrong with the database"}), 400


@data.route("/populate-data", methods=["GET"])
def populate_data():
    try:

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
        return jsonify({"message": "data inserted successfully"})

    except ProgrammingError:
        return jsonify({"error": "There is something wrong with the database"}), 400


@data.route("/remove-data", methods=["GET"])
def remove_data():
    try:

        Content.query.delete()
        Topic.query.delete()
        User.query.delete()
        db.session.commit()

        return jsonify({"message": "data removed successfully"})

    except ProgrammingError:
        return jsonify({"error": "There is something wrong with the database"}), 400
