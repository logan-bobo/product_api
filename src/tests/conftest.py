"""
Testing configurations that hold fixtures that can be called for each test
"""


from typing import Generator

import pytest

from product_api.app import Inventory, Product, StoredInventory, Supplier, app, db

API_VERSION = "v1"


# Integration fixtures
@pytest.fixture()
def client() -> Generator:
    """
    Generates a flask test client to run tests against
    :return: FlaskClient
    """
    flask_app = app

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client


@pytest.fixture(name="_persisted_supplier")
def write_supplier(_supplier_instance):
    """
    Persist a supplier to the database for use in integration testing
    :param _supplier_instance:
    :return:
    """
    db.drop_all()

    db.create_all()

    db.session.add(_supplier_instance)

    db.session.commit()


# Unit fixtures
@pytest.fixture(name="_supplier_instance")
def supplier() -> Supplier:
    """
    Return a Supplier instance with sensible defaults for testing
    :return: dev_test_supplier
    """
    dev_test_supplier = Supplier(
        id=1,
        name="dev_test_supplier_one",
    )
    return dev_test_supplier


@pytest.fixture(name="_product_instance")
def product(_supplier_instance) -> Product:
    """
    Return a Product instance with sensible defaults for testing needs to take in a Supplier
    :param _supplier_instance: Instance of Supplier
    :return: Product
    """
    dev_test_cola = Product(
        id=1,
        name="dev_test_cola",
        price=0.99,
        supplier=_supplier_instance.id,
    )
    return dev_test_cola


@pytest.fixture(name="_inventory_instance")
def inventory() -> Inventory:
    """
    Return an Inventory instance with sensible defaults for testing
    :return: Inventory
    """
    dev_test_inventory = Inventory(
        id=1,
        name="dev_test_inventory",
        address="66, Dev Test Close, London, England, SW1A 1AA",
    )
    return dev_test_inventory


@pytest.fixture(name="_stored_inventory_instance")
def stored_inventory(_inventory_instance, _product_instance) -> StoredInventory:
    """
    Return an Inventory instance with sensible defaults for testing
    :param _inventory_instance: an instance of Inventory
    :param _product_instance: an instance of Product
    :return:
    """
    inventory_store = StoredInventory(
        id=1,
        inventory_id=_inventory_instance.id,
        product_id=_product_instance.id,
        quantity=10,
    )
    return inventory_store
