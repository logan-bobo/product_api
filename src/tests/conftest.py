import pytest

from src.product_api.app import app


@pytest.fixture()
def client():
    flask_app = app

    with flask_app.test_client() as testing_client:
        yield testing_client
