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


@pytest.fixture(name="persisted_supplier")
def persisted_supplier(supplier_instance):
    db.drop_all()

    db.create_all()

    db.session.add(supplier_instance)

    db.session.commit()


# Unit fixtures
@pytest.fixture(name="supplier_instance")
def supplier_instance() -> Supplier:
    """
    Return a Supplier instance with sensible defaults for testing
    :return: Supplier
    """
    supplier = Supplier(
        id=1,
        name="dev_test_supplier_one",
    )
    return supplier


@pytest.fixture(name="product_instance")
def product_instance(supplier_instance) -> Product:
    """
    Return a Product instance with sensible defaults for testing needs to take in a Supplier
    :param supplier_instance: Instance of Supplier
    :return: Product
    """
    product = Product(
        id=1,
        name="dev_test_cola",
        price=0.99,
        supplier=supplier_instance.id,
    )
    return product


@pytest.fixture(name="inventory_instance")
def inventory_instance() -> Inventory:
    """
    Return an Inventory instance with sensible defaults for testing
    :return: Inventory
    """
    inventory = Inventory(
        id=1,
        name="dev_test_inventory",
        address="66, Dev Test Close, London, England, SW1A 1AA",
    )
    return inventory


@pytest.fixture(name="stored_inventory_instance")
def stored_inventory_instance(inventory_instance, product_instance) -> StoredInventory:
    """
    Return an Inventory instance with sensible defaults for testing
    :param inventory_instance: an instance of Inventory
    :param product_instance: an instance of Product
    :return:
    """
    stored_inventory = StoredInventory(
        id=1,
        inventory_id=inventory_instance.id,
        product_id=product_instance.id,
        quantity=10,
    )
    return stored_inventory
