
import os

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///data.db")

if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ.get("SECRET_KEY", "mysecretkey2024")