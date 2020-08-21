from sqlalchemy import func
import sys, os
import json
import pytest
import flask
import base64

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from factories.base_factory import TopicFactory, UserFactory, ContentFactory
from first_screening.models.db import *
from first_screening.controllers.topic_controller import TopicControllerError
from first_screening.controllers.content_controller import ContentControllerError


# def test_generate_user(test_client):
#   response = test_client.get('/api/generate_user')
#   assert response.status_code == 200


def test_login(test_client):
    credentials = base64.b64encode(b"admin:password").decode("UTF-8")
    response = test_client.get(
        "/api/login", headers={"Authorization": f"Basic {credentials}"}
    )
    assert response.status_code == 200


def test_get_ping(test_client):
    response = test_client.get(
        "/api/topics/ping", headers={"x-access-token": "example_token"}
    )
    assert response.status_code == 200


def test_post_topic(test_client):
    topic = TopicFactory.build()
    name, description = topic.name, topic.description
    payload = {"name": name, "description": description}
    response = test_client.post(
        "/api/topics/",
        data=json.dumps(payload),
        headers={"x-access-token": "example_token"},
        content_type="application/json",
    )
    assert response.status_code == 200


def test_post_topic_2(test_client):
    topic = TopicFactory.build()
    name, description = topic.name, topic.description
    payload = {"name": name, "description": description}
    response = test_client.post(
        "/api/topics/",
        data=json.dumps(payload),
        headers={"x-access-token": "example_token"},
        content_type="application/json",
    )
    assert response.status_code == 200


def test_post_topic_3(test_client):
    topic = TopicFactory.build()
    name, description = topic.name, topic.description
    payload = {"name": name, "description": description}
    response = test_client.post(
        "/api/topics/",
        data=json.dumps(payload),
        headers={"x-access-token": "example_token"},
        content_type="application/json",
    )
    assert response.status_code == 200


def test_post_topic_failed(test_client):
    with pytest.raises(TopicControllerError):
        name = "Some title"
        payload = {"name": name}
        response = test_client.post(
            "/api/topics/",
            data=json.dumps(payload),
            headers={"x-access-token": "example_token"},
            content_type="application/json",
        )


def test_get_topics(test_client):
    response = test_client.get("/api/topics/")
    assert response.status_code == 200


def test_get_topic(test_client):
    topic = Topic.query.order_by().first()
    name_id = topic.name_id
    response = test_client.get("/api/topics/" + name_id)
    assert response.status_code == 200


def test_update_topic(test_client):
    topic = Topic.query.order_by().first()
    name_id = topic.name_id
    new_topic = TopicFactory.build()
    payload = {"name": new_topic.name, "description": new_topic.description}
    response = test_client.put(
        "/api/topics/" + name_id,
        data=json.dumps(payload),
        headers={"x-access-token": "example_token"},
        content_type="application/json",
    )
    assert response.status_code == 200


def test_delete_topic(test_client):
    topic = Topic.query.order_by().first()
    name_id = topic.name_id
    response = test_client.delete("/api/topics/" + name_id)
    assert response.status_code == 401


def test_post_content(test_client):
    topic = Topic.query.order_by(Topic.id.desc()).first()
    name_id = topic.name_id
    content = ContentFactory.build()
    sequence_number = content.sequence_number
    title = content.title
    body = content.body
    topic_id = topic.id
    payload = {
        "sequence_number": sequence_number,
        "title": title,
        "body": body,
        "topic_id": topic_id,
    }
    response = test_client.post(
        "/api/topics/" + name_id,
        data=json.dumps(payload),
        headers={"x-access-token": "example_token"},
        content_type="application/json",
    )
    assert response.status_code == 200


def test_post_content_2(test_client):
    topic = Topic.query.order_by(Topic.id.desc()).first()
    name_id = topic.name_id
    content = ContentFactory.build()
    sequence_number = content.sequence_number
    title = content.title
    body = content.body
    topic_id = topic.id
    payload = {
        "sequence_number": sequence_number,
        "title": title,
        "body": body,
        "topic_id": topic_id,
    }
    response = test_client.post(
        "/api/topics/" + name_id,
        data=json.dumps(payload),
        headers={"x-access-token": "example_token"},
        content_type="application/json",
    )
    assert response.status_code == 200


def test_post_content_3(test_client):
    topic = Topic.query.order_by(Topic.id.desc()).first()
    name_id = topic.name_id
    content = ContentFactory.build()
    sequence_number = content.sequence_number
    title = content.title
    body = content.body
    topic_id = topic.id
    payload = {
        "sequence_number": sequence_number,
        "title": title,
        "body": body,
        "topic_id": topic_id,
    }
    response = test_client.post(
        "/api/topics/" + name_id,
        data=json.dumps(payload),
        headers={"x-access-token": "example_token"},
        content_type="application/json",
    )
    assert response.status_code == 200


def test_post_content_fail(test_client):
    with pytest.raises(ContentControllerError):
        payload = {"title": "test title", "body": "test body"}
        name_id = "the-four-values-of-the-agile-manifesto"
        response = test_client.post(
            "/api/topics/" + name_id,
            data=json.dumps(payload),
            headers={"x-access-token": "example_token"},
            content_type="application/json",
        )


def test_get_content(test_client):
    topic = Topic.query.order_by(Topic.id.desc()).first()
    content = Content.query.filter(Topic.id == Content.topic_id).first()
    response = test_client.get(
        "/api/topics/" + topic.name_id + "/" + str(content.sequence_number)
    )
    assert response.status_code == 200


def test_update_content(test_client):
    topic = Topic.query.order_by(Topic.id.desc()).first()
    content = Content.query.filter(Topic.id == Content.topic_id).first()
    new_content = ContentFactory.build()
    payload = {
        "sequence_number": new_content.sequence_number,
        "title": new_content.title,
        "body": new_content.body,
    }
    response = test_client.put(
        "/api/topics/" + topic.name_id + "/" + str(content.sequence_number),
        data=json.dumps(payload),
        content_type="application/json",
    )
    response.status_code == 200


def test_delete_content(test_client):
    topic = Topic.query.order_by().first()
    content = Content.query.filter(Topic.id == Content.topic_id).first()
    response = test_client.delete(
        "/api/topics/" + topic.name_id + "/" + str(content.sequence_number)
    )
    response.status_code == 204
