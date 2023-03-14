"""
Test database models based on class instances
"""


class TestModels:
    def test_new_supplier(self, supplier):
        """
        GIVEN a Supplier model
        WHEN a new Supplier is created
        THEN the name and id are as defined in the fixture
        """
        assert supplier.name == "dev_test_supplier_one"
        assert supplier.id == 1

    def test_new_product(self, product):
        """
        GIVEN a Product model
        WHEN a new Product is created
        THEN the id, name, price and supplier are as defined in the fixture
        """
        assert product.id == 1
        assert product.name == "dev_test_cola"
        assert product.supplier == 1
        assert product.price == 0.99

    def test_new_inventory(self, inventory):
        """
        GIVE an Inventory model
        WHEN a new Inventory is created
        THEN the id, name and address are as we defined in the fixture
        """
        assert inventory.id == 1
        assert inventory.name == "dev_test_inventory"
        assert inventory.address == "66, Dev Test Close, London, England, SW1A 1AA"

    def test_new_stored_inventory(self, stored_inventory):
        """
        GIVEN a StoredInventory model
        WHEN a new StoredInventory is created
        THEN the id, inventory_id, product_id and quantity are as defined in the fixture
        """
        assert stored_inventory.id == 1
        assert stored_inventory.inventory_id == 1
        assert stored_inventory.product_id == 1
        assert stored_inventory.quantity == 10
