"""
Test the supplier routes
"""
from tests.conftest import API_VERSION


class TestSupplier:
    """
    Test class to encapsulate all supplier route tests
    """

    def test_supplier_endpoint_returns_all_supplier_data(
        self, client, _persisted_supplier
    ):
        """
        GIVEN the supplier endpoint
        WHEN an HTTP GET request is made to the supplier endpoint
        THEN we are returned JSON that shows all suppliers
        """
        response = client.get(f"/{API_VERSION}/suppliers")

        assert b'{"name":"dev_test_supplier_one"}' in response.data

    def test_supplier_endpoint_returns_a_specific_supplier(
        self, client, _persisted_supplier
    ):
        """
        GIVEN the supplier endpoint
        WHEN an HTTP GET request is made to the supplier endpoint, with a specified ID
        THEN we are returned JSON the supplier name based on the ID supplied on request
        """
        response = client.get(f"/{API_VERSION}/suppliers/1")

        assert b'{"name":"dev_test_supplier_one"}' in response.data

    def test_supplier_endpoint_shows_error_on_incorrect_id(
        self, client, _persisted_supplier
    ):
        """
        GIVEN the supplier endpoint
        WHEN an HTTP GET request is made to the supplier endpoint,
        with a specified ID and the supplier has not
        been created
        THEN we are returned that the supplier we are not looking for is not found
        """
        response = client.get(f"/{API_VERSION}/suppliers/900")

        assert b'{"message":"supplier 900 not found"}' in response.data

    def test_supplier_can_be_created(self, client):
        """
        GIVEN the supplier endpoint
        WHEN an HTTP POST reqeust is made to create a new supplier based on name
        THEN the supplier is persisted to the database and can be called via GET request based on ID
        """

        post_response = client.post(f"/{API_VERSION}/suppliers", json={"name": "fanta_industries_inc"})
        get_response = client.get(f"/{API_VERSION}/suppliers/2")

        assert b'{"message":"supplier fanta_industries_inc created"}' in post_response.data
        assert b'{"name":"fanta_industries_inc"}' in get_response.data

