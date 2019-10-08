"""
Stores global fixtures testing files
"""
import pytest

from .server import create_app
from connections.db import db


@pytest.fixture(scope='module')
def test_create_client():
    app = create_app('sqlite:///test_flaskart.sqlite')
    client = app.test_client()

    context = app.app_context()
    context.push()

    yield client

    context.pop()


@pytest.fixture(scope='module')
def test_create_tables():
    db.init_db()
    yield
    db.drop_db()
