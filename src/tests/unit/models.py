
def test_new_supplier(new_supplier):
    """
    GIVEN a Supplier model
    WHEN a new Supplier is created
    THEN the name and id are as defined in the fixture
    """
    assert new_supplier.name == "dev_test_supplier_one"
    assert new_supplier.id == 1


def test_new_product(new_product):
    """
    GIVEN a Product model
    WHEN a new Product is created
    THEN the id, name, price and supplier are as defined in the fixture
    """
    assert new_product.id == 1
    assert new_product.name == "dev_test_cola"
    assert new_product.supplier == 1
    assert new_product.price == 0.99


def test_new_inventory(new_inventory):
    """
    GIVE an Inventory model
    WHEN a new Inventory is created
    THEN the id, name and address are as we defined in the fixture
    """
    assert new_inventory.id == 1
    assert new_inventory.name == "dev_test_inventory"
    assert new_inventory.address == "66, Dev Test Close, London, England, SW1A 1AA"


def test_new_stored_inventory(new_stored_inventory):
    """
    GIVEN a StoredInventory model
    WHEN a new StoredInventory is created
    THEN the id, inventory_id, product_id and quantity are as defined in the fixture
    """
    assert new_stored_inventory.id == 1
    assert new_stored_inventory.inventory_id == 1
    assert new_stored_inventory.product_id == 1
    assert new_stored_inventory.quantity == 10
