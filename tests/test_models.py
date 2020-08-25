import sys, os

from first_screening import create_app, db
from first_screening.models.db import *
from werkzeug.security import generate_password_hash, check_password_hash

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

def test_new_user(test_client):
    user = User("johndoe", generate_password_hash("password"), True)
    assert user.username == "johndoe"
    assert user.is_admin == True


def test_new_topic(test_client):
    name = "Somewhere down the road"
    description = "Great music!"
    topic = Topic(name, description)
    assert topic.name is not None
    assert topic.name == "Somewhere down the road"


def test_new_content(test_client, new_topic):
    content = Content(
        1, "Our roads are gonna cross again", "Doesn't matter when", new_topic.id
    )
    assert content is not None
    assert content.topic_id == new_topic.id
