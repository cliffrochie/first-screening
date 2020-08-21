import sys, os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

import pytest
from first_screening import create_app, db
from first_screening.models.db import *
from first_screening.utils.formatter import format_name_id

from factories.base_factory import TopicFactory

# Client
@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    test_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield test_client
    ctx.pop()


# DB
@pytest.fixture(scope="module")
def init_database():
    db.create_all()
    yield db
    db.drop_all()


# Create new topic
@pytest.fixture(scope="module")
def new_topic():
    name = "Test"
    description = "A test topic."

    topic = Topic(name, description)
    return topic
