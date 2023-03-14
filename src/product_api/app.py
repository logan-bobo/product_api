"""
Core application logica for product_api containing models and routes.
"""

from flask import Flask, Response, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy

# Instantiate Flask and SQLAlchemy
db = SQLAlchemy()
app = Flask(__name__)

# Configure SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# Initialize the app with the extension
db.init_app(app)


class Supplier(db.Model):  # type: ignore # pylint: disable=too-few-public-methods
    """
    Used to create Suppliers representing a single database row
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)

    def __repr__(self):
        return f"<Supplier {self.name}>"


class Product(db.Model):  # type: ignore # pylint: disable=too-few-public-methods
    """
    Used to create Products representing a single database row
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)
    price = db.Column(db.Float, nullable=False)
    supplier = db.ForeignKey(Supplier.id, nullable=False)

    def __repr__(self):
        return f"<Product {self.name}>"


class Inventory(db.Model):  # type: ignore # pylint: disable=too-few-public-methods
    """
    Used to create an Inventory representing a database row
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)
    address = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return f"<Inventory {self.name}>"


class StoredInventory(db.Model):  # type: ignore # pylint: disable=too-few-public-methods
    """
    Used to create a StoredInventory to map products to inventories
    """

    id = db.Column(db.Integer, primary_key=True)
    inventory_id = db.ForeignKey(Inventory.id, nullable=False)
    product_id = db.ForeignKey(Product.id, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<StoredInventory {self.id}>"


with app.app_context():
    db.create_all()


@app.route("/v1/health", methods=["GET"])
def health() -> Response:
    """
    The health endpoint that can be used to check the health on an instance
    :return: Response
    """
    return make_response(jsonify(status="healthy"), 200)


# supplier routes
@app.route("/v1/suppliers", methods=["POST"])
def create_supplier() -> Response:
    """
    Create a supplier by name with a POST reqeust containing JSON data in the following format.
    :return: Response
    """
    request_data = request.get_json()

    if "name" not in request_data:
        return make_response(jsonify(message="supplier name not specified"), 400)

    new_supplier = Supplier(name=request_data["name"])

    db.session.add(new_supplier)

    db.session.commit()

    return make_response(
        jsonify(message=f"supplier {request_data['name']} created"), 200
    )


@app.route("/v1/suppliers", methods=["GET"])
def read_suppliers() -> Response:
    """
    Read all suppliers that are registered in JSON format.
    :return: Response
    """

    supplier_data = db.session.execute(
        db.select(Supplier).order_by(Supplier.id)
    ).scalars()
    suppliers: dict = {"suppliers": {}}

    for supplier in supplier_data:
        suppliers["suppliers"][supplier.id] = {"name": supplier.name}

    return make_response(suppliers, 200)


@app.route("/v1/suppliers/<int:supplier_id>")
def read_supplier(supplier_id) -> Response:
    """
    Read an individual supplier based on ID.
    :return: Response
    """

    if request.view_args is not None:
        supplier_id: int = request.view_args["supplier_id"]
    else:
        return make_response(
            jsonify(message="invalid request to path must supply id"), 400
        )

    supplier_data: Supplier = db.session.execute(
        db.select(Supplier).where(Supplier.id == supplier_id)
    ).scalar()

    if not supplier_data:
        return make_response(jsonify(message=f"supplier {supplier_id} not found"), 400)

    supplier = {supplier_data.id: {"name": supplier_data.name}}

    return make_response(supplier, 200)
