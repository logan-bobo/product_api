from tests.conftest import API_VERSION


def test_health_endpoint_returns_desired_message(client):
    """
    GIVEN the health endpoint
    WHEN an HTTP GET request is made to the root endpoint
    THEN we are returned JSON that shows a key of status with the value of healthy
    """
    response = client.get(f"/{API_VERSION}/health")
    assert b'{"status":"healthy"}' in response.data


def test_health_endpoint_returns_status_200(client):
    """
    GIVEN the health endpoint
    WHEN an HTTP GET request is made to the health endpoint
    THEN we are returned HTTP 200 from the endpoint
    """
    response = client.get(f"/{API_VERSION}/health")
    assert response.status_code == 200
