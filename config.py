import os

# Base folder of the project
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Secret key for forms and sessions
    SECRET_KEY = "EGET_SUPER_SECRET_KEY_2026"

    # SQLite database
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "database.db")

    # Disable modification tracking (improves performance)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Folder for uploaded car images
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")

    # Maximum upload size (16 MB)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # Allowed image types
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}