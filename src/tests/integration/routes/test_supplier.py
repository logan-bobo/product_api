"""
Test the supplier routes
"""
from product_api.app import db
from tests.conftest import API_VERSION


class TestSupplier:
    def test_supplier_endpoint_returns_all_supplier_data(
        self, client, persisted_supplier
    ):
        """
        GIVEN the supplier endpoint
        WHEN an HTTP GET request is made to the supplier endpoint
        THEN we are returned JSON that shows the supplier name
        """
        response = client.get(f"/{API_VERSION}/suppliers")

        assert b'{"name":"dev_test_supplier_one"}' in response.data

    def test_supplier_endpoint_returns_a_specific_supplier(
        self, client, persisted_supplier
    ):
        """
        GIVEN the supplier endpoint
        WHEN an HTTP GET request is made to the supplier endpoint, with a specified ID
        THEN we are returned JSON the supplier name based on the ID supplied on request
        """
        response = client.get(f"/{API_VERSION}/suppliers/1")

        assert b'{"name":"dev_test_supplier_one"}' in response.data

    def test_supplier_endpoint_shows_error_on_incorrect_id(
        self, client, persisted_supplier
    ):
        """
        GIVEN the supplier endpoint
        WHEN an HTTP GET request is made to the supplier endpoint, with a specified ID and the supplier has not been created
        THEN we are returned that the supplier we are not looking for is not found
        """
        response = client.get(f"/{API_VERSION}/suppliers/900")

        assert b'{"message":"supplier 900 not found"}' in response.data
