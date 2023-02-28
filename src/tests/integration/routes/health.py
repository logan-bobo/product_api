API_VERSION = "v1"


def test_health_endpoint_returns_desired_message(client):
    response = client.get(f"/{API_VERSION}/health")
    assert b'{"status":"healthy"}' in response.data


def test_health_endpoint_returns_status_200(client):
    response = client.get(f"/{API_VERSION}/health")
    assert response.status_code == 200