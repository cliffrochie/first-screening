import sys, os

from factories.base_factory import *

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))



def test_create_topic(test_client):
    topic = TopicFactory.build()
    assert topic is not None
    assert type(topic.name) == str
    assert type(topic.description) == str


def test_create_content(test_client):
    content = ContentFactory.build()
    assert content is not None
    assert type(content.sequence_number) == int
    assert type(content.title) == str
    assert type(content.body) == str


def test_create_user(test_client):
    user = UserFactory.build()
    assert user is not None
    assert type(user.username) == str
    assert type(user.is_admin) == bool
