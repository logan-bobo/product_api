from flask import Flask
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
    name = db.Column(db.String, unique=True)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    price = db.Column(db.Float, nullable=False)
    supplier = db.ForeignKey(Supplier.id, nullable=False)


class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    address = db.Column(db.String, unique=True)


class StoredInventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inventory_id = db.ForeignKey(Inventory.id, nullable=False)
    product_id = db.ForeignKey(Product.id, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def hello() -> str:
    return 'Hello World'

