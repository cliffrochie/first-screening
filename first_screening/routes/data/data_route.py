from flask import Blueprint, jsonify
from first_screening import db
from first_screening.models.db import *
from first_screening.utils.data import topics
from first_screening.controllers.user_controller import UserController
from sqlalchemy.exc import ProgrammingError
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

        cursor = conn.cursor()
        cursor.execute("DROP DATABASE IF EXISTS screening")
        cursor.execute("CREATE DATABASE screening")

        conn.close()

        return jsonify({"message": "database created successfully"})

    except ProgrammingError:
        return jsonify({"error": "There is something wrong with the server"}), 400


@data.route('/generate-tables', methods=['GET'])
def create_tables():
    try:
        db.create_all()
        return jsonify({"message": "tables created successfully"})
        
    except ProgrammingError:
        return jsonify({"error": "There is something wrong with the server"}), 400



@data.route("/populate-data", methods=["GET"])
def populate_data():
    try:

        for data in topics:
            check_topic = Topic.query.filter(Topic.name == data["name"]).first()
            if check_topic:
                return jsonify({"error": "Duplicate entry"}), 400
                
            topic = Topic(data["name"], data["description"])
            db.session.add(topic)
            db.session.commit()

            for content in data["content"]:
                content = Content(
                    content["sequence_number"], content["title"], content["body"], topic.id
                )
                db.session.add(content)
                db.session.commit()

        user = UserController.generate_user()

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
