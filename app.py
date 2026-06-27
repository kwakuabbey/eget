from flask import Flask, render_template
from config import Config
from models import db

# Create Flask app
app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Create database tables automatically
with app.app_context():
    db.create_all()


# ===========================
# ROUTES
# ===========================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/add-car")
def add_car():
    return render_template("add_car.html")


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/messages")
def messages():
    return render_template("messages.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/favourites")
def favourites():
    return render_template("favourites.html")


@app.route("/car/<int:car_id>")
def car_details(car_id):
    return render_template("car_details.html", car_id=car_id)


# ===========================
# RUN APPLICATION
# ===========================

if __name__ == "__main__":
    app.run(debug=True)