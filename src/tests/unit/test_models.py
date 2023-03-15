"""
Test database models based on class instances
"""


class TestModels:
    """
    Test class to encapsulate all model test
    """

    def test_new_supplier(self, _supplier_instance):
        """
        GIVEN a Supplier model
        WHEN a new Supplier is created
        THEN the name and id are as defined in the fixture
        """
        assert _supplier_instance.name == "dev_test_supplier_one"
        assert _supplier_instance.id == 1

    def test_new_product(self, _product_instance):
        """
        GIVEN a Product model
        WHEN a new Product is created
        THEN the id, name, price and supplier are as defined in the fixture
        """
        assert _product_instance.id == 1
        assert _product_instance.name == "dev_test_cola"
        assert _product_instance.supplier == 1
        assert _product_instance.price == 0.99

    def test_new_inventory(self, _inventory_instance):
        """
        GIVE an Inventory model
        WHEN a new Inventory is created
        THEN the id, name and address are as we defined in the fixture
        """
        assert _inventory_instance.id == 1
        assert _inventory_instance.name == "dev_test_inventory"
        assert (
            _inventory_instance.address
            == "66, Dev Test Close, London, England, SW1A 1AA"
        )

    def test_new_stored_inventory(self, _stored_inventory_instance):
        """
        GIVEN a StoredInventory model
        WHEN a new StoredInventory is created
        THEN the id, inventory_id, product_id and quantity are as defined in the fixture
        """
        assert _stored_inventory_instance.id == 1
        assert _stored_inventory_instance.inventory_id == 1
        assert _stored_inventory_instance.product_id == 1
        assert _stored_inventory_instance.quantity == 10
