"""
Testing configurations that hold fixtures that can be called for each test
"""


from typing import Generator

import pytest

from product_api.app import Inventory, Product, StoredInventory, Supplier, app

API_VERSION = "v1"


@pytest.fixture()
def client() -> Generator:
    """
    Generates a flask test client to run tests against
    :return: FlaskClient
    """
    flask_app = app

    with flask_app.test_client() as testing_client:
        yield testing_client


@pytest.fixture(name="supplier")
def new_supplier() -> Supplier:
    """
    Return a Supplier instance with sensible defaults for testing
    :return: Supplier
    """
    supplier = Supplier(
        id=1,
        name="dev_test_supplier_one",
    )
    return supplier


@pytest.fixture(name="product")
def new_product(supplier) -> Product:
    """
    Return a Product instance with sensible defaults for testing needs to take in a Supplier
    :param supplier: Instance of Supplier
    :return: Product
    """
    product = Product(
        id=1,
        name="dev_test_cola",
        price=0.99,
        supplier=supplier.id,
    )
    return product


@pytest.fixture(name="inventory")
def new_inventory() -> Inventory:
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


@pytest.fixture(name="stored_inventory")
def new_stored_inventory(inventory, product) -> StoredInventory:
    """
    Return an Inventory instance with sensible defaults for testing
    :param inventory: an instance of Inventory
    :param product: an instance of Product
    :return:
    """
    stored_inventory = StoredInventory(
        id=1,
        inventory_id=inventory.id,
        product_id=product.id,
        quantity=10,
    )
    return stored_inventory
