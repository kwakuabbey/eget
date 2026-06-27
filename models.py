from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


# ===========================
# USER TABLE
# ===========================

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(150), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    phone = db.Column(db.String(30))

    password = db.Column(db.String(255), nullable=False)

    country = db.Column(db.String(100))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    cars = db.relationship("Car", backref="owner", lazy=True)


# ===========================
# CAR TABLE
# ===========================

class Car(db.Model):
    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key=True)

    seller_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    brand = db.Column(db.String(100), nullable=False)

    model = db.Column(db.String(100), nullable=False)

    year = db.Column(db.String(10))

    colour = db.Column(db.String(50))

    transmission = db.Column(db.String(50))

    fuel_type = db.Column(db.String(50))

    body_type = db.Column(db.String(50))

    mileage = db.Column(db.Integer)

    engine_size = db.Column(db.String(30))

    condition = db.Column(db.String(30))

    price = db.Column(db.Float)

    negotiable = db.Column(db.Boolean, default=False)

    country = db.Column(db.String(100))

    region = db.Column(db.String(100))

    city = db.Column(db.String(100))

    description = db.Column(db.Text)

    status = db.Column(db.String(20), default="Available")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    images = db.relationship("CarImage", backref="car", lazy=True)


# ===========================
# CAR IMAGES
# ===========================

class CarImage(db.Model):
    __tablename__ = "car_images"

    id = db.Column(db.Integer, primary_key=True)

    filename = db.Column(db.String(255))

    car_id = db.Column(db.Integer, db.ForeignKey("cars.id"))


# ===========================
# MESSAGES
# ===========================

class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)

    sender_name = db.Column(db.String(150))

    sender_email = db.Column(db.String(120))

    message = db.Column(db.Text)

    sent_at = db.Column(db.DateTime, default=datetime.utcnow)

    car_id = db.Column(db.Integer, db.ForeignKey("cars.id"))


# ===========================
# FAVOURITES
# ===========================

class Favourite(db.Model):
    __tablename__ = "favourites"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    car_id = db.Column(db.Integer, db.ForeignKey("cars.id"))