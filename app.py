import json

from flask import Flask, jsonify, Response, make_response, request
from flask_sqlalchemy import SQLAlchemy

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


@app.route('/v1/suppliers', methods=["POST"])
def create_supplier() -> Response:
    request_data: json = request.get_json()

    print(request_data)

    if "name" not in request_data:
        return make_response(jsonify(status="error", message="supplier name not specified"), 400)

    new_supplier = Supplier(
        name = request_data["name"]
    )

    db.session.add(new_supplier)

    db.session.commit()

    return make_response(jsonify(status="success", message=f"supplier {request_data['name']} created"), 200)
