import pytest
from app import app


def test_app():
    response = app.app.test_client().get('/api/posts/')
    assert type(response.json) == list


def test_all():
    params = {"post_id": "1"}
    response = app.app.test_client().get('/api/posts/', query_string=params)
    assert type(response.json) == list




