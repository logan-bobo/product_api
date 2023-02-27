import json

from flask import Flask, jsonify, Response, make_response, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import Result, ScalarResult

# Instantiate Flask and SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy()

# Configure SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# Initialize the app with the extension
db.init_app(app)


class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)
    price = db.Column(db.Float, nullable=False)
    supplier = db.ForeignKey(Supplier.id, nullable=False)


class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)
    address = db.Column(db.String(100), unique=True)


class StoredInventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inventory_id = db.ForeignKey(Inventory.id, nullable=False)
    product_id = db.ForeignKey(Product.id, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/v1/health', methods=["POST"])
def health() -> Response:
    return make_response(jsonify(status="healthy"), 200)


# Create suppliers
@app.route('/v1/suppliers', methods=["POST"])
def create_supplier() -> Response:
    """
    Create a supplier by name with a POST reqeust containing JSON data in the following format.
    {
        "name":"foo"
    }
    :return: Response
    """
    request_data: json = request.get_json()

    if "name" not in request_data:
        return make_response(jsonify(message="supplier name not specified"), 400)

    new_supplier = Supplier(
        name = request_data["name"]
    )

    db.session.add(new_supplier)

    db.session.commit()

    return make_response(jsonify(message=f"supplier {request_data['name']} created"), 200)


# Read suppliers
@app.route('/v1/suppliers', methods=["GET"])
def read_suppliers() -> Response:
    """
    Read all suppliers that are registered in JSON format.
    {
       "suppliers":{
          "1":{
             "name":"foo"
          },
          "2":{
             "name":"bar"
          }
       }
    }
    :return: Response
    """
    supplier_data: ScalarResult = db.session.scalars(db.select(Supplier).order_by(Supplier.id))

    suppliers: dict = {"suppliers": {}}

    for supplier in supplier_data:
        suppliers["suppliers"][supplier.id]: str = {"name": supplier.name}

    return make_response(suppliers, 200)


# Read an individual supplier
@app.route('/v1/suppliers/<int:supplier_id>')
def read_supplier(supplier_id: int) -> Response:
    """
    Read an individual supplier based on ID and be returned information about that supplier in JSON format
    {
        "1": {
            name: "foo"
        }
    }
    :return: Response
    """

    supplier_id: int = request.view_args['supplier_id']

    supplier_data: Supplier = db.session.scalar(db.select(Supplier).where(Supplier.id == supplier_id))

    supplier = {
        supplier_data.id:
            {
                "name": supplier_data.name
            }
    }

    return make_response(supplier, 200)
