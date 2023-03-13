"""
Test the supplier routes
"""
from product_api.app import db
from tests.conftest import API_VERSION


def test_supplier_endpoint_returns_all_supplier_data(client, supplier):
    """
    GIVEN the supplier endpoint
    WHEN an HTTP GET request is made to the supplier endpoint
    THEN we are returned JSON that shows the supplier name
    """

    db.drop_all()

    db.create_all()

    db.session.add(supplier)

    db.session.commit()

    response = client.get(f"/{API_VERSION}/suppliers")

    assert b'{"name":"dev_test_supplier_one"}' in response.data


def test_supplier_endpoint_returns_a_specific_supplier(client, supplier):
    """
    GIVEN the supplier endpoint
    WHEN an HTTP GET request is made to the supplier endpoint, with a specified ID
    THEN we are returned JSON the supplier name based on the ID supplied on request
    """

    db.drop_all()

    db.create_all()

    db.session.add(supplier)

    db.session.commit()

    response = client.get(f"/{API_VERSION}/suppliers/1")

    assert b'{"name":"dev_test_supplier_one"}' in response.data


def test_supplier_endpoint_shows_error_on_incorrect_id(client, supplier):
    """
    GIVEN the supplier endpoint
    WHEN an HTTP GET request is made to the supplier endpoint, with a specified ID and the supplier has not been created
    THEN we are returned that the supplier we are not looking for is not found
    """

    db.drop_all()

    db.create_all()

    db.session.add(supplier)

    db.session.commit()

    response = client.get(f"/{API_VERSION}/suppliers/900")

    assert b'{"message":"supplier 900 not found"}' in response.data