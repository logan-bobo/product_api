import pytest

from src.product_api.app import app, Supplier, Product, Inventory, StoredInventory

API_VERSION = "v1"


@pytest.fixture()
def client():
    flask_app = app

    with flask_app.test_client() as testing_client:
        yield testing_client


@pytest.fixture()
def new_supplier():
    supplier = Supplier(
        id=1,
        name="dev_test_supplier_one",
    )
    return supplier


@pytest.fixture()
def new_product(new_supplier):
    product = Product(
        id=1,
        name="dev_test_cola",
        price=0.99,
        supplier=new_supplier.id,
    )
    return product


@pytest.fixture()
def new_inventory():
    inventory = Inventory(
        id=1,
        name="dev_test_inventory",
        address="66, Dev Test Close, London, England, SW1A 1AA",
    )
    return inventory


@pytest.fixture()
def new_stored_inventory(new_inventory, new_product):
    stored_inventory = StoredInventory(
        id=1,
        inventory_id=new_inventory.id,
        product_id=new_product.id,
        quantity=10,
    )
    return stored_inventory
