import sys, os
import factory.alchemy

from first_screening import db
from first_screening.models.db import *
from werkzeug.security import generate_password_hash

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class TopicFactory(BaseFactory):
    class Meta:
        model = Topic

    name = factory.Faker("sentence")
    description = name = factory.Faker("sentence")


class ContentFactory(BaseFactory):
    class Meta:
        model = Content

    sequence_number = 1
    title = factory.Faker("sentence")
    body = factory.Faker("sentence")
    topic_id = 1


class UserFactory(BaseFactory):
    class Meta:
        model = User

    username = "johnsmith"
    password = generate_password_hash("password")
    is_admin = True
