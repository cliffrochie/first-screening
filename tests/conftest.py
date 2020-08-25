import sys, os
import pytest

from first_screening import create_app, db
from first_screening.models.db import *
from factories.base_factory import TopicFactory

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

# Client
@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    test_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield test_client
    ctx.pop()



# Create new topic
@pytest.fixture(scope="module")
def new_topic():
    name = "Test"
    description = "A test topic."

    topic = Topic(name, description)
    return topic
