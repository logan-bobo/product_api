"""
Test health endpoint of the flask application
"""

from tests.conftest import API_VERSION


class TestHealth:
    """
    Test class to encapsulate all health route tests
    """

    def test_health_endpoint_returns_health_message(self, _client):
        """
        GIVEN the health endpoint
        WHEN an HTTP GET request is made to the root endpoint
        THEN we are returned JSON that shows a key of status with the value of healthy
        """
        response = _client.get(f"/{API_VERSION}/health")

        assert b'{"status":"healthy"}' in response.data

    def test_health_endpoint_returns_status_200(self, _client):
        """
        GIVEN the health endpoint
        WHEN an HTTP GET request is made to the health endpoint
        THEN we are returned HTTP 200 from the endpoint
        """
        response = _client.get(f"/{API_VERSION}/health")

        assert response.status_code == 200
